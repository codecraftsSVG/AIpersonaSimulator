import sqlite3
import json
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "simulator.db")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scenarios (
        id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        category TEXT NOT NULL,
        background TEXT NOT NULL,
        user_role TEXT NOT NULL,
        ai_role TEXT NOT NULL,
        objective TEXT NOT NULL,
        difficulty TEXT NOT NULL,
        personality TEXT NOT NULL,
        expected_outcome TEXT NOT NULL,
        is_custom BOOLEAN DEFAULT 0,
        created_at TEXT
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS simulations (
        id TEXT PRIMARY KEY,
        scenario_id TEXT,
        mode TEXT NOT NULL,
        personality TEXT NOT NULL,
        difficulty TEXT NOT NULL,
        status TEXT NOT NULL,
        started_at TEXT,
        ended_at TEXT,
        evaluation_json TEXT,
        FOREIGN KEY (scenario_id) REFERENCES scenarios(id)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        simulation_id TEXT,
        sender TEXT NOT NULL,
        content TEXT NOT NULL,
        timestamp TEXT,
        FOREIGN KEY (simulation_id) REFERENCES simulations(id)
    )
    """)
    
    conn.commit()
    cursor.execute("SELECT COUNT(*) FROM scenarios")
    if cursor.fetchone()[0] == 0:
        seed_scenarios(cursor, conn)
    conn.close()

def seed_scenarios(cursor, conn):
    default_scenarios = [
        ("work-1", "Requesting a meeting with a senior leader", "Workplace Communication", 
         "You want to pitch a new workflow optimization project to the VP of Engineering.", "Senior Engineer", "VP of Engineering", 
         "Secure a 20-minute meeting by clearly articulating business value.", "Intermediate", "Dismissive", "VP agrees to a brief meeting."),
        ("work-2", "Asking for career progression", "Workplace Communication",
         "You have been performing at a senior level for over a year without formal title bump.", "Software Engineer", "Engineering Manager",
         "Initiate a clear timeline and requirements for promotion.", "Advanced", "Critical", "Manager sets measurable milestones."),
        ("conf-1", "Dealing with a defensive colleague", "Conflict Management",
         "A deployment failed due to configuration issues, colleague blames your pipeline.", "DevOps Engineer", "Senior Backend Developer",
         "Resolve blame constructively and establish shared post-mortem.", "Advanced", "Defensive", "Colleague takes responsibility."),
        ("lead-1", "Managing underperforming employees", "Leadership",
         "A key team member has missed sprint deadlines for three consecutive weeks.", "Team Lead", "Underperforming Developer",
         "Address performance gaps empathetically while setting clear expectations.", "Intermediate", "Defensive", "Developer agrees to improvement plan."),
        ("nego-1", "Salary negotiation", "Negotiation",
         "You received a new job offer and want a 15% increase above initial band.", "Candidate", "Recruitment Director",
         "Negotiate higher base salary without jeopardizing offer.", "Advanced", "Accepting", "Company adjusts compensation package."),
        ("pers-1", "Saying no without feeling guilty", "Personal Communication",
         "A peer asks you to take over weekend on-call rotation during personal commitments.", "Team Member", "Peer Colleague",
         "Decline request firmly and respectfully.", "Beginner", "Accepting", "Colleague looks for alternative coverage.")
    ]
    
    for s in default_scenarios:
        cursor.execute("""
        INSERT OR IGNORE INTO scenarios (id, title, category, background, user_role, ai_role, objective, difficulty, personality, expected_outcome, is_custom, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0, ?)
        """, (*s, datetime.now().isoformat()))
    conn.commit()

# Auto initialize on module import
init_db()

