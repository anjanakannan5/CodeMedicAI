import os
import shutil
import subprocess

TEST_FOLDER = "tests"
SANDBOX_FILE = "sandbox/user_code.py"

passed = 0
failed = 0

for test in sorted(os.listdir(TEST_FOLDER)):

    if not test.endswith(".py"):
        continue

    print("\n" + "="*60)
    print("Running:", test)

    shutil.copy(
        os.path.join(TEST_FOLDER, test),
        SANDBOX_FILE
    )

    result = subprocess.run(["python", "main.py"])

    if result.returncode == 0:
        passed += 1
    else:
        failed += 1

print("\n" + "="*60)
print("Testing Complete")
print(f"Passed : {passed}")
print(f"Failed : {failed}")