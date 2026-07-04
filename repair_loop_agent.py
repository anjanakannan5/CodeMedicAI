import repair_agent
import llm_client
import file_writer
import execution_agent
import analysis_agent
import validator_agent
import report_writer


def repair_program(current_analysis, repaired_file, max_attempts):

    # Keep the original root cause explanation throughout all repair attempts.
    #root_cause = current_analysis["root_cause_analysis"]
    root_cause = current_analysis.get("root_cause_analysis", "Root cause analysis could not be generated.")
    
    # Try repairing the program until it succeeds
    # or the maximum number of attempts is reached.
    for attempt in range(max_attempts):

        print(f"\n[Repair Agent]")
        print("----------------------------------------")
        print(f"    Repair Attempt {attempt + 1}/{max_attempts}")
        print("----------------------------------------")

        # Create repair prompt
        repair_prompt = repair_agent.create_repair_prompt(current_analysis)

        # Ask the LLM for repaired code
        repaired_code = llm_client.ask_llm(repair_prompt)
        print("✓ Repair generated.\n")

        # Save repaired code
        print("[File Writer]")
        file_writer.save_repaired_code(repaired_code, repaired_file)

        # Execute repaired program
        repair_execution = execution_agent.execute_code(repaired_file)

        # Repair succeeded
        if repair_execution["result"].returncode == 0:
            
            validation = validator_agent.validate_repair( current_analysis, repair_execution)
            
            if validation["valid"]:
                print("✓ Validation passed\n")
                
                print("==================================================")
                print("              Repair Successful")
                print("==================================================")
                print(f"\nAttempts Used : {attempt + 1}/{max_attempts}")
                print(f"Repaired File : {repaired_file}\n")
                print("Program Output :")
                print(repair_execution["result"].stdout.strip())
                print("\n==================================================")

                #Report on the error
                report_writer.save_repair_report(
                    current_analysis,
                    attempt + 1,
                    repaired_file,
                    repair_execution["result"].stdout.strip()
                )

                print("\n[Report Writer]")
                print("✓ repair_report.txt created.")
                return True
            
            print("✗ Validation failed")
            print(validation["reason"])

        print("✗ Repair failed.\n")

        # Analyze the new error
        current_analysis = analysis_agent.analyze_code(
            repair_execution,
            repaired_file
        )

        # Preserve the original root cause explanation
        current_analysis["root_cause_analysis"] = root_cause

    return False