import subprocess
import sys
import os
import time

def start_services():
    backend_dir = os.path.join(os.path.dirname(__file__), "backend")
    frontend_dir = os.path.join(os.path.dirname(__file__), "frontend")
    
    print("Starting AI Conversation Simulator Backend (FastAPI on port 8000)...")
    backend_proc = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"],
        cwd=backend_dir
    )
    
    print("Starting Frontend Static Server (HTTP on port 3000)...")
    frontend_proc = subprocess.Popen(
        [sys.executable, "-m", "http.server", "3000"],
        cwd=frontend_dir
    )
    
    print("\n------------------------------------------------------------")
    print("🚀 AI Conversation Simulator is now running!")
    print("Frontend UI: http://localhost:3000/index.html")
    print("Backend API: http://localhost:8000/api/scenarios")
    print("API Docs:    http://localhost:8000/docs")
    print("------------------------------------------------------------\n")
    print("Press Ctrl+C to stop servers.")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping servers...")
        backend_proc.terminate()
        frontend_proc.terminate()
        backend_proc.wait()
        frontend_proc.wait()
        print("Servers stopped successfully.")

if __name__ == "__main__":
    start_services()
