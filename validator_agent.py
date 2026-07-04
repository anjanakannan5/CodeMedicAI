def validate_repair(original_analysis, repair_execution):
    print("[Validation Agent]")
    result = repair_execution["result"]
    
    # Program must execute successfully
    if result.returncode != 0:
        return {
            "valid": False,
            "reason": "Program execution failed."
        }
    
    # Program should produce output
    output = result.stdout.strip()
    if output == "":
        return {
            "valid": False,
            "reason": "Program produced no output."
        }

    if "Traceback" in output:
        return {
            "valid": False,
            "reason": "Program still contains a traceback."
        }
    
    return {
        "valid": True,
        "reason": "Repair validated successfully."
    }