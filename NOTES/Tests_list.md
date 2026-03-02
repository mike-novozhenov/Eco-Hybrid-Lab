### 📋 План автоматизации тестирования (Hybrid Framework)

| № | Тип теста | Сценарий проверки | Ключевой навык (Skill) |
|:--|:---|:---|:---|
| **1** | **Pure UI (POM)** | Добавление товара в корзину через интерфейс | Page Object Model & Clean Code |
| **2** | **API + UI** | Регистрация пользователя через API → Авторизация в браузере | Интеграция слоев & Backend-knowledge |
| **3** | **UI + DB** | Оформление заказа → Проверка транзакции в базе данных | Database Testing & SQL |
| **4** | **Data Driven** | Массовая регистрация пользователей из внешнего JSON/CSV | Scalability & Pytest Parametrization |
| **5** | **E2E Flow** | Сквозной сценарий: Login → Cart → Checkout → Logout | End-to-End Business Logic |
| **6** | **Negative/Security** | Валидация форм: SQL-инъекции и пустые обязательные поля | Edge Cases & QA Mindset |


### 🌐 Стратегия выбора площадок для тестирования

| № | Тест | Целевой ресурс | Техническое обоснование | Stack |
|:--|:---|:---|:---|:---|
| **1** | **Pure UI (POM)** | [Demoblaze](https://www.demoblaze.com/) | Динамический контент, работа с модальными окнами (Alerts) и корзиной | Playwright, POM |
| **2** | **API + UI** | [ReqRes](https://reqres.in/) + Demoblaze | Связка внешнего REST API сервиса с фронтендом реального магазина | Requests, Pytest |
| **3** | **UI + DB** | Local Project | Полный контроль над транзакциями: от клика в браузере до строки в PostgreSQL | SQLAlchemy, SQL |
| **4** | **Data Driven** | [SauceDemo](https://www.saucedemo.com/) | Классический полигон для массовой проверки прав доступа (RBAC) | Pytest Parametrize |
| **5** | **E2E Flow** | [OpenCart Demo](https://demo.opencart.com/) | Проверка сложной бизнес-логики: фильтрация, оформление, итоговая сумма | Playwright, E2E |
| **6** | **Negative** | [The Internet](https://the-internet.herokuapp.com/) | Специализированные кейсы: обработка ошибок, битые ссылки, JS-инъекции | QA Mindset, Logs |