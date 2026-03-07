import os
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TESTS_DIR = os.path.join(BASE_DIR, "tests")


def run_commands():
    pytest_cmd = ["pytest", "-n", "auto", TESTS_DIR, "--alluredir=allure-results", "--clean-alluredir"]

    if "-m" in sys.argv:
        try:
            marker_index = sys.argv.index("-m")
            marker_expr = " ".join(sys.argv[marker_index + 1 :])
            marker_expr = marker_expr.split("--")[0].strip().replace('"', "").replace("&quot;", "")

            pytest_cmd.append("-m")
            pytest_cmd.append(marker_expr)
            print(f"🎯 Filtering tests by expression: {marker_expr}")
        except IndexError:
            print("⚠️ Error: No marker specified after -m")
            sys.exit(1)

    if "--headed" in sys.argv:
        if "-n" in pytest_cmd:
            pytest_cmd.remove("-n")
            pytest_cmd.remove("auto")
        pytest_cmd.extend(["--headed", "--slowmo", "1000"])

    print(f"🔥 Executing: {' '.join(pytest_cmd)}")

    result = subprocess.run(pytest_cmd)

    if result.returncode in [0, 1]:
        print("\n📊 Opening Allure report (Press Ctrl+C to stop)...")
        try:
            subprocess.run("allure serve allure-results", shell=True)
        except KeyboardInterrupt:
            print("\n✅ Report server stopped by user")
            sys.exit(0)
    else:
        print(f"❌ Tests failed to execute (Return code: {result.returncode})")


if __name__ == "__main__":
    run_commands()