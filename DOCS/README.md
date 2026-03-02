# Eco-Hybrid-Lab: Hybrid Test Automation Framework

This project demonstrates a hybrid approach to test automation, integrating UI, API, and Database layers into a single, scalable framework.

## 🚀 Tech Stack
* **Language:** Python 3.13
* **UI Engine:** Playwright (Chromium)
* **Test Runner:** Pytest
* **Database:** SQLAlchemy + PostgreSQL
* **Reporting:** Allure Reports
* **Env Management:** Python-dotenv

## 🛠 Automation Strategy (Test Scenarios)

| № | Test Type | Verification Scenario | Key Skill / Achievement |
|:--|:---|:---|:---|
| **1** | **Pure UI (POM)** | Adding a product to the cart via the web interface | Page Object Model & Clean Code |
| **2** | **API + UI** | User registration via API → Session authorization in browser | Layer Integration & Backend Knowledge |
| **3** | **UI + DB** | Checkout completion → Transaction validation in the database | Database Testing & SQL |
| **4** | **Data Driven** | Bulk user registration from external JSON/CSV files | Scalability & Pytest Parametrization |
| **5** | **E2E Flow** | Full flow: Login → Cart → Checkout → Logout | End-to-End Business Logic |
| **6** | **Negative/Security** | Form validation: SQL injections and empty required fields | Edge Cases & QA Mindset |


## 🌐 Test Targets

| № | Test Type | Target Resource | Technical Rationale |
|:--|:---|:---|:---|
| **1** | **Pure UI** | [Demoblaze](https://www.demoblaze.com/) | Handling dynamic content, async wait strategies, and browser Alerts |
| **2** | **API + UI** | [ReqRes](https://reqres.in/) + Demoblaze | Integration of external **REST API** with frontend logic to verify data consistency |
| **3** | **UI + DB** | Local PostgreSQL | End-to-end transaction tracking: from browser click to **SQL** record validation |
| **4** | **Data Driven** | [SauceDemo](https://www.saucedemo.com/) | Implementation of **DDT** (Data-Driven Testing) for mass user RBAC verification |
| **5** | **E2E Flow** | [OpenCart Demo](https://demo.opencart.com/) | Complex business logic: filtering, checkout process, and total sum calculation |
| **6** | **Negative** | [The Internet](https://the-internet.herokuapp.com/) | Error handling: broken links, status codes, and JS-injection security cases |


## 🚀 Quick Start Guide

### 1. Installation & Environment Setup
Clone the repository and prepare your local environment:

```bash
git clone <your_repository_url>
cd Eco-Hybrid-Lab
python -m venv .venv

# Activate virtual environment (Windows):
.venv\Scripts\activate

# Activate virtual environment (macOS/Linux):
source .venv/bin/activate

# Install dependencies and Playwright browsers:
pip install -r requirements.txt
playwright install chromium
```
   
### 2. Environment Setup
Create a `.env` file in the project root directory based on the template to configure your **DB** and API credentials.

**Windows (CMD):**
```bash
copy .env.example .env
```

**Linux / macOS:**
```bash
cp .env.example .env
```

### 3. Running Tests & Reports
The project uses a custom runner script `run.py` to simplify test execution and report generation.

| Command | Description |
|:---|:---|
| `python run.py` | Run all tests and open Allure report |
| `python run.py --headed` | Run tests in **Headed** mode (visible browser) |
| `python run.py -m ui` | Run only **UI** functional tests |
| `python run.py -m api` | Run only fast **API** integration tests |
| `python run.py -m smoke` | Run critical path tests only |

#### Example: Run UI tests in visible mode
```bash
python run.py -m ui --headed
```

## Test Tagging System
You can run specific groups of tests using the `-m` flag with `run.py`:

| Tag | Description | Command |
|-----|-------------|---------|
| **ui** | Browser-based tests | `python run.py -m ui` |
| **api** | Fast backend requests | `python run.py -m api` |
| **smoke** | Most critical tests | `python run.py -m smoke` |
