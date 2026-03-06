import subprocess
import sys
import os

# Автоматически определяем корень проекта и путь к тестам
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TESTS_DIR = os.path.join(BASE_DIR, "tests")

def run_commands():
    # Теперь мы всегда используем абсолютный путь TESTS_DIR
    pytest_cmd = ["pytest", TESTS_DIR, "--alluredir=allure-results", "--clean-alluredir"]

    # Handle marker filtering
    if "-m" in sys.argv:
        try:
            marker_index = sys.argv.index("-m")
            # Собираем всё после -m и очищаем от возможных артефактов IDE (&quot;)
            marker_expr = " ".join(sys.argv[marker_index + 1:])
            marker_expr = marker_expr.split("--")[0].strip().replace('"', '').replace('&quot;', '')

            pytest_cmd.append("-m")
            pytest_cmd.append(marker_expr)
            print(f"🎯 Filtering tests by expression: {marker_expr}")
        except IndexError:
            print("⚠️ Error: No marker specified after -m")
            sys.exit(1)

    # Check for --headed flag for UI tests
    if "--headed" in sys.argv:
        pytest_cmd.extend(["--headed", "--slowmo", "1000"])

    print(f"🔥 Executing: {' '.join(pytest_cmd)}")

    # Запуск тестов
    result = subprocess.run(pytest_cmd)

    # Generate and serve Allure report automatically
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