def get_line_number(result):
    line_number = None
    for line in result.stderr.splitlines():
        if line.strip().startswith("File"):
            line_number = line.split("line")[1].split(",")[0].strip()
            break
    return line_number


def get_source_code(file_path, line_number):
    source = None
    with open(file_path, "r") as file:
        full_source = file.read()
    lines = full_source.splitlines()
    if line_number is not None:
        line_number = int(line_number)
        if 0 < line_number <= len(lines):
            source = lines[line_number - 1]
    return full_source, source


def analyze_code(execution_report, file_path):
    print("[Analysis Agent]")
    print("→ Analyzing execution result...")
    result = execution_report["result"]
    if result.returncode != 0:
        err = result.stderr.splitlines()[-1] if result.stderr else "No error"
        error_type = err.split(":", 1)[0] if err else "No error"
        error_message = err.split(":", 1)[1].strip() if err else "No error"
        line_number = get_line_number(result)
        full_source, source = get_source_code(file_path, line_number)
        print(f"✗ Error Detected.\n")
        print("Error Details\n-------------")
        print(f"- Exception : {error_type}")
        print(f"- Line      : {line_number}")
        print(f"- File      : {file_path.split("/")[-1]}\n")
        return {
            "status": "failed",
            "exception_type": error_type,
            "error_message": error_message,
            "line_number": line_number,
            "file_name": file_path.split("/")[-1],
            "source_code": source,
            "full_source_code": full_source,
            "traceback": result.stderr,
            "timestamp": execution_report["timestamp"],
        }

    else:
        print("✓ No errors found.\n")
        return {"status": "success", "output": result.stdout}
