# Eco-Hybrid-Lab: Hybrid Test Automation Framework

## Project Overview
This project demonstrates a hybrid approach to test automation, integrating UI, API, and Database layers into a single, scalable framework.

### 📊 Performance & Observability
![Allure Report Dashboard](docs/graphs.jpg)
*Summary: 100% Pass Rate | 10 Tests | ~27s Total Duration*

The framework is optimized for a balanced execution profile:
* **API/DB Layer (< 1s):** Highly efficient back-end validation. `test_api_to_db_logging` demonstrates seamless integration between requests and SQL layers
* **UI Resilience (2s - 4s):** Rapid UI feedback achieved through strategic resource blocking and async event handling
* **Full E2E Flows (8s - 9s):** Comprehensive business logic validation using the Page Object Model (POM) without compromising stability

<details>
<summary>🔍 <b>Deep Traceability Example (Click to expand)</b></summary>
<br>

For the **API to DB Sync** scenario, the report captures every internal step with raw data evidence:

1. **POST Request:** Resource creation verified in **431ms**
2. **DB Logging:** Action recorded via SQLAlchemy in **16ms**
3. **Data Audit:** Direct SQL `SELECT` verifies persistence with raw data attachment: `(1, 'Create post...', 'Success')`
4. **Auto-Cleanup:** Environment is reset via `Tear down` fixtures automatically

<p align="center">
  <img src="docs/traceability.jpg" alt="Deep Traceability" width="80%">
</p>

</details>

> **Key Takeaway:** By utilizing a hybrid approach, 80% of the test suite provides feedback in under 4 seconds, significantly reducing CI/CD pipeline costs
---

### 🟢 Positive Scenarios (Happy Path)
| Scenario | Layer | Technical Highlights & Patterns | Validation & Data Handling | Risk Mitigated |
| :--- | :--- | :--- | :--- | :--- |
| **E2E Shopping Flow** | Hybrid | **POM**, Session persistence, API-driven preconditions | UI State + URL verification; Real-time session auth | Broken conversion funnel |
| **API Data Contract** | API | Type checking (ID as int), header validation | JSON Schema; Status 201; Header integrity | Integration mismatches |
| **API to DB Sync** | API + DB | **Singleton DB Client**, Automated SQL Teardown | Cross-layer integrity (SQL SELECT match) | Silent data loss in backend |
| **Add to Cart** | UI | Dynamic dialog handling, `wait_for_selector` logic | Cart persistence; Alert automation | UI/Logic synchronization |

### 🔴 Negative Scenarios (Resilience & Edge Cases)
| Scenario | Layer | Technical Highlights & Patterns | Validation & Data Handling | Risk Mitigated |
| :--- | :--- | :--- | :--- | :--- |
| **Empty Checkout** | UI | **Turbo Mode**: Asset blocking, 3.7s speed, `dispatch_event` | Alert Interception; No-wait actionability | UI validation bypass |
| **Broken Links Audit** | UI / API | **Multi-threading**: 11 parallel workers, HEAD requests | HTTP Status 200/300; Concurrent discovery | Negative SEO & Dead UX |
| **Auth Resilience** | UI | **Event-driven**: `expect_event("dialog")` (No `sleep`) | Regex alert text match; Dynamic waiting | Flaky tests / Async race conditions |
| **Malformed API Data**| API | Schema resilience, Type-mismatch payloads | JSON Contract; Documentation of server flaws | Backend crashes on bad input |
| **API Failure Logs** | API + DB | Integrated Error Logging (404 -> DB) | Status code mapping to SQL audit logs | Untraceable system errors |


### 🛠 Engineering DNA (Best Practices)
* **Zero-Sleep Policy:** No static timeouts. All asynchronous states are handled via Playwright's native event listeners and smart assertions.
* **Extreme Performance:** Optimized execution through strategic resource blocking (CSS/Images) and multi-threaded processing.
* **Deep Observability:** Automated Allure reporting with integrated screenshots, browser trace logs, and SQL query snapshots for every failure.
* **Clean State Management:** Singleton-based database connectivity with automated transaction teardowns to ensure environment purity.

## 🚀 Tech Stack
* **Language:** Python 3.13
* **UI Engine:** Playwright (Chromium)
* **Test Runner:** Pytest
* **Database:** SQLAlchemy + SQLite3
* **Reporting:** Allure Reports
* **Env Management:** Python-dotenv


## 📂 Project Structure
```text
├── data/               # Test data and DB initialization
├── pages/              # Page Object Models (UI layer)
├── tests/              # Test suites (UI, API, Integration)
├── utils/              # API clients, DB wrappers, Loggers
├── .env.example        # Environment variables template
├── pytest.ini          # Test runner configuration
└── requirements.txt    # Project dependencies
```

## 🚀 Installation & Running

### 1. Clone the repository
```bash
git clone [https://github.com/your-username/Eco-Hybrid-Lab.git](https://github.com/your-username/Eco-Hybrid-Lab.git)
cd Eco-Hybrid-Lab
```

### 2. Setup Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
```

### 3. Execution & Reporting
```bash
# Run all tests and generate results
pytest --alluredir=allure-results

# Open interactive Allure report
allure serve allure-results
```