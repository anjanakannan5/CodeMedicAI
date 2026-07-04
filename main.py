import sys
import database
import execution_agent
import analysis_agent
import root_cause_agent
import repair_loop_agent
import llm_client

# Create the SQLite database and required tables (if they don't already exist)
database.create_database()

USER_FILE = "sandbox/user_code.py"
REPAIRED_FILE = "sandbox/repaired_user_code.py"
MAX_ATTEMPTS = 2

print("==================================================\n")
print("                CodeMedic AI\n       Autonomous Debugging Assistant\n")
print("==================================================\n")

# Execute the user's Python program
execution_report = execution_agent.execute_code(USER_FILE)

# Analyze the execution result to determine success or failure
analysis = analysis_agent.analyze_code(execution_report, USER_FILE)

# If the program ran successfully, display its output and stop
if analysis["status"] == "success":
    print("==================================================")
    print("            Program Executed Successfully")
    print("==================================================")
    print("\nProgram Output :")
    print(analysis["output"])
    print("\nNo debugging or repair was required.\n")
    print("==================================================")
    sys.exit(0)

# Save error information for debugging/history
database.save_error(analysis)

# Generate an explanation of why the error occurred using the LLM
try:
    prompt = root_cause_agent.create_prompt(analysis)
    analysis["root_cause_analysis"] = llm_client.ask_llm(prompt)
    print("✓ Explanation generated.")
except Exception as e:
    print("LLM Error:", e)

# Try to automatically repair the user's code
success = repair_loop_agent.repair_program( analysis, REPAIRED_FILE, MAX_ATTEMPTS )

if success:
    sys.exit(0)
print("==================================================")
print("                 Repair Failed")
print("==================================================")
sys.exit(1)