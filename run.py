import subprocess
import sys

def run_commands():
    # 1. Base command for pytest
    # We remove the hardcoded path to allow filtering by markers across the project
    pytest_cmd = "pytest --alluredir=allure-results --clean-alluredir"

    # Check for marker filtering (e.g., python run.py -m ui)
    if "-m" in sys.argv:
        try:
            marker_index = sys.argv.index("-m")
            marker_tag = sys.argv[marker_index + 1]
            pytest_cmd += f" -m {marker_tag}"
            print(f"🎯 Filtering tests by marker: {marker_tag}")
        except IndexError:
            print("⚠️ Error: No marker specified after -m")
            sys.exit(1)
    else:
        # If no marker, run the specific UI test by default (or the whole folder)
        pytest_cmd += " tests/ui/test_add_to_cart.py"

    # Check for --headed flag in command line arguments to show browser UI
    if "--headed" in sys.argv:
        pytest_cmd += " --headed --slowmo 1000"

    print(f"🚀 Executing: {pytest_cmd}")
    subprocess.run(pytest_cmd, shell=True)

    # 2. Generate and serve Allure report automatically
    print("\n📊 Opening Allure report (Press Ctrl+C to stop)...")
    try:
        # We use shell=True to ensure Allure is found in the system PATH
        subprocess.run("allure serve allure-results", shell=True)
    except KeyboardInterrupt:
        # Clean exit without showing traceback
        print("\n✅ Report server stopped by user")
        sys.exit(0)

if __name__ == "__main__":
    run_commands()