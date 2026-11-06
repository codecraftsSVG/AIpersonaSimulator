from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import uuid, json
from datetime import datetime
from database import init_db, get_db
from ai_engine import generate_ai_response, stream_ai_response, evaluate_simulation


app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.on_event("startup")
def startup(): init_db()

class ScenarioCreate(BaseModel):
    title: str; category: str; background: str; user_role: str; ai_role: str; objective: str; difficulty: str; personality: str; expected_outcome: str

class SimStart(BaseModel):
    scenario_id: str; mode: str; personality: Optional[str] = None; difficulty: Optional[str] = None

class ChatMsg(BaseModel):
    content: str

@app.get("/api/scenarios")
def get_scenarios(category: Optional[str] = None):
    conn = get_db(); cur = conn.cursor()
    if category and category != "All": cur.execute("SELECT * FROM scenarios WHERE category = ?", (category,))
    else: cur.execute("SELECT * FROM scenarios")
    rows = [dict(r) for r in cur.fetchall()]; conn.close(); return rows

@app.post("/api/scenarios")
def create_scenario(p: ScenarioCreate):
    sid = "custom-" + str(uuid.uuid4())[:8]
    conn = get_db(); cur = conn.cursor()
    cur.execute("INSERT INTO scenarios VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1, ?)",
                (sid, p.title, p.category, p.background, p.user_role, p.ai_role, p.objective, p.difficulty, p.personality, p.expected_outcome, datetime.now().isoformat()))
    conn.commit(); conn.close(); return {"id": sid}

@app.post("/api/simulations/start")
def start_sim(p: SimStart):
    conn = get_db(); cur = conn.cursor()
    cur.execute("SELECT * FROM scenarios WHERE id = ?", (p.scenario_id,))
    row = cur.fetchone()
    if not row: conn.close(); raise HTTPException(404, "Not found")
    sc = dict(row); pers = p.personality or sc["personality"]; diff = p.difficulty or sc["difficulty"]
    sim_id = str(uuid.uuid4())
    cur.execute("INSERT INTO simulations VALUES (?, ?, ?, ?, ?, 'active', ?, NULL, NULL)",
                (sim_id, p.scenario_id, p.mode, pers, diff, datetime.now().isoformat()))
    cur.execute("INSERT INTO messages (simulation_id, sender, content, timestamp) VALUES (?, 'ai', ?, ?)", (sim_id, f"Hello. Ready to discuss: {sc['title']}.", datetime.now().isoformat()))
    conn.commit(); conn.close()
    return {"simulation_id": sim_id, "scenario": sc, "mode": p.mode, "personality": pers, "difficulty": diff}

@app.get("/api/simulations/{sim_id}")
def get_sim(sim_id: str):
    conn = get_db(); cur = conn.cursor()
    cur.execute("SELECT * FROM simulations WHERE id = ?", (sim_id,))
    sim = cur.fetchone()
    if not sim: conn.close(); raise HTTPException(404, "Not found")
    sim_d = dict(sim)
    cur.execute("SELECT * FROM scenarios WHERE id = ?", (sim_d["scenario_id"],))
    sc = dict(cur.fetchone())
    cur.execute("SELECT * FROM messages WHERE simulation_id = ? ORDER BY id ASC", (sim_id,))
    msgs = [dict(r) for r in cur.fetchall()]
    conn.close()
    return {"simulation": sim_d, "scenario": sc, "messages": msgs, "evaluation": json.loads(sim_d["evaluation_json"]) if sim_d["evaluation_json"] else None}

@app.post("/api/simulations/{sim_id}/chat")
def chat_sim(sim_id: str, p: ChatMsg):
    conn = get_db(); cur = conn.cursor()
    cur.execute("SELECT * FROM simulations WHERE id = ?", (sim_id,))
    sim = cur.fetchone()
    if not sim: conn.close(); raise HTTPException(404, "Not found")
    sim_d = dict(sim)
    if sim_d["status"] != "active": conn.close(); raise HTTPException(400, "Completed")
    cur.execute("SELECT * FROM scenarios WHERE id = ?", (sim_d["scenario_id"],))
    sc = dict(cur.fetchone())
    cur.execute("SELECT sender, content FROM messages WHERE simulation_id = ? ORDER BY id ASC", (sim_id,))
    history = [dict(r) for r in cur.fetchall()]
    cur.execute("INSERT INTO messages (simulation_id, sender, content, timestamp) VALUES (?, 'user', ?, ?)", (sim_id, p.content, datetime.now().isoformat()))
    conn.commit()
    history.append({"sender": "user", "content": p.content})
    reply = generate_ai_response(sc, sim_d["personality"], sim_d["mode"], sim_d["difficulty"], history, p.content)
    cur.execute("INSERT INTO messages (simulation_id, sender, content, timestamp) VALUES (?, 'ai', ?, ?)", (sim_id, reply, datetime.now().isoformat()))
    conn.commit(); conn.close()
    return {"user_message": p.content, "ai_message": reply}

@app.post("/api/simulations/{sim_id}/chat-stream")
def chat_stream(sim_id: str, p: ChatMsg):
    conn = get_db(); cur = conn.cursor()
    cur.execute("SELECT * FROM simulations WHERE id = ?", (sim_id,))
    sim = cur.fetchone()
    if not sim: conn.close(); raise HTTPException(404, "Not found")
    sim_d = dict(sim)
    if sim_d["status"] != "active": conn.close(); raise HTTPException(400, "Completed")
    cur.execute("SELECT * FROM scenarios WHERE id = ?", (sim_d["scenario_id"],))
    sc = dict(cur.fetchone())
    cur.execute("SELECT sender, content FROM messages WHERE simulation_id = ? ORDER BY id ASC", (sim_id,))
    history = [dict(r) for r in cur.fetchall()]
    cur.execute("INSERT INTO messages (simulation_id, sender, content, timestamp) VALUES (?, 'user', ?, ?)", (sim_id, p.content, datetime.now().isoformat()))
    conn.commit()
    history.append({"sender": "user", "content": p.content})
    conn.close()

    def generate():
        full_text = ""
        for chunk in stream_ai_response(sc, sim_d["personality"], sim_d["mode"], sim_d["difficulty"], history, p.content):
            full_text += chunk
            yield chunk
        # Save complete message to DB after stream finishes
        c2 = get_db()
        c2.execute("INSERT INTO messages (simulation_id, sender, content, timestamp) VALUES (?, 'ai', ?, ?)", (sim_id, full_text, datetime.now().isoformat()))
        c2.commit(); c2.close()

    return StreamingResponse(generate(), media_type="text/plain")

@app.post("/api/simulations/{sim_id}/end")
def end_sim(sim_id: str):
    conn = get_db(); cur = conn.cursor()
    cur.execute("SELECT * FROM simulations WHERE id = ?", (sim_id,))
    sim = cur.fetchone()
    if not sim: conn.close(); raise HTTPException(404, "Not found")
    sim_d = dict(sim)
    cur.execute("SELECT * FROM scenarios WHERE id = ?", (sim_d["scenario_id"],))
    sc = dict(cur.fetchone())
    cur.execute("SELECT sender, content FROM messages WHERE simulation_id = ? ORDER BY id ASC", (sim_id,))
    history = [dict(r) for r in cur.fetchall()]
    eval_res = evaluate_simulation(sc, history)
    cur.execute("UPDATE simulations SET status = 'completed', ended_at = ?, evaluation_json = ? WHERE id = ?", (datetime.now().isoformat(), json.dumps(eval_res), sim_id))
    conn.commit(); conn.close()
    return {"status": "completed", "evaluation": eval_res}

@app.get("/api/dashboard/stats")
def stats():
    conn = get_db(); cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM simulations WHERE status = 'completed'")
    total = cur.fetchone()[0]
    cur.execute("SELECT evaluation_json FROM simulations WHERE status = 'completed' AND evaluation_json IS NOT NULL")
    scores = [json.loads(r[0]).get("overall_score", 0) for r in cur.fetchall() if r[0]]
    avg = int(sum(scores) / len(scores)) if scores else 0
    cur.execute("SELECT s.id, sc.title, s.mode, s.personality, s.started_at, s.evaluation_json FROM simulations s JOIN scenarios sc ON s.scenario_id = sc.id WHERE s.status = 'completed' ORDER BY s.started_at DESC LIMIT 5")
    recent = [{"id": d["id"], "title": d["title"], "mode": d["mode"], "personality": d["personality"], "started_at": d["started_at"], "overall_score": json.loads(d["evaluation_json"]).get("overall_score", 0) if d["evaluation_json"] else 0} for d in [dict(r) for r in cur.fetchall()]]
    conn.close()
    return {"total_simulations": total, "average_score": avg, "recent_simulations": recent}
