eco-hybrid-lab/
├── .github/
│   └── workflows/
│       └── main.yml           # Инструкция для ручного запуска (On Demand)
├── data/
│   ├── schemas/               # JSON-схемы для валидации API (Pydantic модели)
│   │   └── user_schema.py
│   └── test_data.json         # Статичные данные для тестов
├── db/
│   ├── scripts/               # SQL скрипты инициализации (init.sql)
│   └── db_client.py           # Хелпер для работы с БД (SQLAlchemy)
├── pages/
│   ├── base_page.py           # Базовые методы и общие ожидания
│   ├── components/            # Те самые переиспользуемые компоненты
│   │   ├── header.py
│   │   ├── footer.py
│   │   └── product_card.py    # Пример компонента внутри списка
│   └── cart_page.py           # Логика конкретных страниц
├── tests/
│   ├── api/                   # Чистые тесты на бэкенд
│   ├── ui/                    # Чистые тесты на фронтенд
│   └── hybrid/                # Самые мощные тесты (UI + API + DB)
├── utils/
│   └── api_client.py          # Обертка над Playwright API Request для тестов
├── .env.example               # Пример файла с переменными окружения
├── .gitignore                 # Игнорируем venv, логи, отчеты и .env
├── conftest.py                # Главное сердце: фикстуры для DB, API и Browser
├── docker-compose.yml         # Магия для локального поднятия всей среды
├── Dockerfile                 # Образ для запуска тестов в изоляции
├── pytest.ini                 # Конфиг pytest (маркировки, опции запуска)
├── requirements.txt           # Список библиотек (playwright, pytest, sqlalchemy, pydantic)
└── README.md                  # Лицо твоего проекта