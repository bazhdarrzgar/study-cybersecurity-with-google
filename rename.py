import os
from pathlib import Path

# Path to the folder containing the directories
base_path = Path("/home/swyanswartz/Documents/course/Note/ Play It Safe Manage Security Risks/01_security-domains/04_review-security-domains")

# Raw user input
raw_old = """
file1.md
"""

raw_new = """
01_wrap-up.md
"""

# Process the raw strings into clean lists
old_names = [line.strip() for line in raw_old.strip().splitlines() if line.strip()]
new_names = [line.strip() for line in raw_new.strip().splitlines() if line.strip()]

# Safety check
if len(old_names) != len(new_names):
    print("⚠️ Error: The number of old and new names does not match.")
else:
    for old, new in zip(old_names, new_names):
        old_path = os.path.join(base_path, old)
        new_path = os.path.join(base_path, new)

        if os.path.exists(old_path):
            os.rename(old_path, new_path)
            print(f'✅ Renamed: "{old}" → "{new}"')
        else:
            print(f'❌ Folder not found: "{old}"')
