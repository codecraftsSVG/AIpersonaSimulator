import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "backend"))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_scenarios():
    response = client.get("/api/scenarios")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 6
    print("Scenarios test passed. Count:", len(data))

def test_start_simulation():
    response = client.post("/api/simulations/start", json={
        "scenario_id": "work-1",
        "mode": "Roleplay Mode",
        "personality": "Dismissive",
        "difficulty": "Intermediate"
    })
    assert response.status_code == 200
    data = response.json()
    assert "simulation_id" in data
    sim_id = data["simulation_id"]
    print("Start simulation test passed. ID:", sim_id)
    
    # Test chat
    chat_resp = client.post(f"/api/simulations/{sim_id}/chat", json={
        "content": "Hi, I wanted to discuss our meeting request."
    })
    assert chat_resp.status_code == 200
    chat_data = chat_resp.json()
    assert "ai_message" in chat_data
    print("Chat test passed. AI reply:", chat_data["ai_message"])
    
    # Test end simulation & evaluation
    end_resp = client.post(f"/api/simulations/{sim_id}/end")
    assert end_resp.status_code == 200
    end_data = end_resp.json()
    assert "evaluation" in end_data
    assert "overall_score" in end_data["evaluation"]
    print("Evaluation test passed. Overall score:", end_data["evaluation"]["overall_score"])

if __name__ == "__main__":
    test_get_scenarios()
    test_start_simulation()
    print("All backend tests passed successfully!")
