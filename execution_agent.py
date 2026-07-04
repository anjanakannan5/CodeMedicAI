import subprocess
from datetime import datetime

def execute_code(file_path):
    print("[Execution Agent]")
    print("→ Running program...")
    run_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result = subprocess.run(
        ["python", file_path], 
        capture_output=True, 
        text=True
    )
    print("✓ Program execution completed.\n")
    return {
        "result": result, 
        "timestamp" : run_timestamp
        }