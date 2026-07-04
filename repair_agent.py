def create_repair_prompt(analysis):
    print("→ Generating repair...")
    return f"""
You are an expert Python code repair engine.

Your task is to repair the following Python program.

Original Python program:

{analysis["full_source_code"]}

The program produced:

Exception Type:
{analysis["exception_type"]}

Error Message:
{analysis["error_message"]}

Traceback:
{analysis["traceback"]}

Instructions:

1. Return the COMPLETE corrected Python program.
2. Preserve the original program as much as possible.
3. Fix ONLY the bug that caused the exception.
4. Produce VALID Python syntax only.
5. Never generate JavaScript, JSON, or any other language.
6. Never use markdown.
7. Never use ```python.
8. Never explain your answer.
9. Never include comments.
10. Do not invent variables, modules, or values unless absolutely necessary.
11. If information is missing, make the smallest reasonable correction.
12. The repaired program must execute without raising the same exception.

Repair Guidelines:

For NameError:
- If an undefined variable is clearly a typo, replace it with the intended variable.
- If the intended variable cannot be inferred, define the missing variable only when it is obvious.
- Never leave an undefined variable unchanged.

For IndexError:
- Use a valid index.
- Do not remove the list or the print statement.
- Preserve the program's original behavior.

For KeyError:
- Access an existing key when obvious.
- Otherwise use dict.get() with an appropriate default.

For TypeError:
- Preserve the original operation.
- Convert operands only when appropriate.
- If converting a string to an integer, use a valid numeric string.

For ValueError:
- Replace invalid values with valid ones while preserving the original intent.

For ZeroDivisionError:
- Replace only the zero denominator.
- Do not change the rest of the expression.

For ModuleNotFoundError:
- Do not invent module names.
- Keep the original import if the correct module cannot be determined.

For ImportError:
- Import an existing function or object from the same module.

For AttributeError:
- Use an object that supports the requested attribute or method.
- Do not remove the method call.

For SyntaxError:
- Fix only the syntax error.
- Preserve the program logic.

Output ONLY the corrected Python source code.
"""