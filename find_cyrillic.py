import os
import re


def find_russian_in_comments():
    # Regular expression to find Cyrillic characters
    russian_pattern = re.compile(r'[а-яА-ЯёЁ]')

    # Exclude service directories
    exclude_dirs = {'.git', '.venv', '__pycache__', '.pytest_cache', 'allure-results', 'allure-history'}

    found_any = False
    print("--- Searching for Russian characters in code ---")

    for root, dirs, files in os.walk("."):
        # Filter directories in-place
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        for file in files:
            if file.endswith(('.py', '.yml', '.yaml', '.html')):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        for line_num, line in enumerate(f, 1):
                            if russian_pattern.search(line):
                                print(f"📍 {file_path} [Line {line_num}]: {line.strip()}")
                                found_any = True
                except Exception as e:
                    print(f"Could not read {file_path}: {e}")

    if not found_any:
        print("✅ No Russian characters found! Your code is clean.")
    else:
        print("\n❌ Please replace the lines above with English equivalents.")


if __name__ == "__main__":
    find_russian_in_comments()