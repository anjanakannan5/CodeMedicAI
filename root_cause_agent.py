def create_prompt(analysis):
    print("[Root Cause Agent]")
    print("→ Requesting explanation...")
    prompt = f"""
You are an expert Python debugging assistant.

Analyze the following Python error.

Exception Type:
{analysis["exception_type"]}

Error Message:
{analysis["error_message"]}

File Name:
{analysis["file_name"]}

Line Number:
{analysis["line_number"]}

Source Code:
{analysis["source_code"]}

Return ONLY the following sections:

Root Cause:
(Describe the actual reason for the error.)

Explanation:
(Explain why Python raised this exception.)

Suggested Fix:
(Explain how the code should be changed. Do not rewrite the full program.)
"""
    return prompt