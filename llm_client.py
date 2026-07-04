import ollama
import json
import re

def ask_llm(prompt):
    response = ollama.chat(
        model="qwen2.5-coder:1.5b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return clean_llm_response(response)

def clean_llm_response(response):

    text = response["message"]["content"].strip()

    # Case 1: JSON response
    try:
        data = json.loads(text)
        if "code" in data:
            return data["code"]
    except:
        pass

    # Case 2: Markdown code block
    match = re.search(r"```(?:python)?\n(.*?)```", text, re.DOTALL)
    if match:
        return match.group(1).strip()

    # Case 3: Remove common introductory phrases
    lines = text.splitlines()

    cleaned = []
    started = False

    for line in lines:

        line = line.rstrip()

        if (
            line.startswith("Here's")
            or line.startswith("The corrected")
            or line.startswith("Corrected")
            or line.startswith("Explanation")
            or line.startswith("This revised")
            or line.strip() == "python"
        ):
            continue

        if line.strip():
            started = True

        if started:
            cleaned.append(line)

    return "\n".join(cleaned).strip()