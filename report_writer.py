def save_repair_report(analysis, attempts_used, repaired_file, program_output):
    with open("repair_report.txt", "w") as file:
        file.write("==================================================\n")
        file.write("           CodeMedic AI Repair Report\n")
        file.write("==================================================\n")
        
        file.write("Original Exception\n")
        file.write("----------------------\n")
        file.write(f"Type    : {analysis['exception_type']}\n")
        file.write(f"Message : {analysis['error_message']}\n")
        file.write(f"File    : {analysis['file_name']}\n")
        file.write(f"Line    : {analysis['line_number']}\n\n")
        
        file.write("Root Cause Analysis\n")
        file.write("----------------------\n")
        file.write(analysis["root_cause_analysis"])
        file.write("\n\n")
        
        file.write("Repair Status\n")
        file.write("----------------------\n")
        file.write("SUCCESS\n\n")
        
        file.write("Attempts Used\n")
        file.write("----------------------\n")
        file.write(f"{attempts_used}\n\n")

        file.write("Repaired File\n")
        file.write("----------------------\n")
        file.write(f"{repaired_file}\n\n")

        file.write("Program Output\n")
        file.write("----------------------\n")
        file.write(program_output)