def save_repaired_code(code, file_path):
    print('→ Saving repaired code...')
    with open(file_path, "w") as file:
        file.write(code)
    print("✓ repaired_user_code.py created.\n")