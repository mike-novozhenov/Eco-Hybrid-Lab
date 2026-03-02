### Tier 2 (Smoke - Critical) — "Happy Path"
**Куда ассерты:** Тоже **Hard Assertions**. 
**Логика:** Это критический путь (например, кандидат может подать заявку). Если кнопка «Apply» не работает, это блокер для релиза. 
**Пример:** Проверяем, что после подачи заявки статус в базе стал "Applied". Если нет — тест падает, билд красный.

### Tier 3 (Major - Regression) — "Soft Gate"
**Вот тут самое интересное!** Если ты используешь обычный `assert`, он всё равно покрасит билд в красный цвет и может остановить CI/CD.

**Как это делают инженеры для Tier 3:**
1.  **Soft Assertions (библиотека `pytest-check`):** Тест проверяет, например, цвет кнопки или наличие второстепенного текста. Если не совпало — он записывает ошибку в отчет, но **тест продолжает бежать до конца**.
2.  **Warning System:** Вместо `assert` ты можешь просто писать лог или кидать предупреждение. Билд остается "желтым" (прошел, но есть нюансы), мануальщики работают, но баг зафиксирован.



---

### Резюме: где ставить ассерты?

| Tier | Тип Ассерта | Результат для билда |
| :--- | :--- | :--- |
| **Tier 1** | **Hard `assert`** | Билд падает сразу (Stop) |
| **Tier 2** | **Hard `assert`** | Билд падает сразу (Stop) |
| **Tier 3** | **Soft Assert / Logs** | Билд проходит, но в отчете "Warning" |

### Как это «продать» завтра на интервью:
Когда Андрей спросит про твой подход, скажи:
> "I use a tiered assertion strategy. For **Tier 1 and 2**, I use **Hard Assertions** because they are 'Hard Gates' — if they fail, the build must stop. For **Tier 3 (Regression)**, I prefer a more flexible approach, sometimes using **Soft Assertions**, so we don't block the entire pipeline for non-critical UI bugs, allowing the manual team to continue their work."

---

### 🛑 Михаил, ТЕПЕРЬ ВСЁ! 
Ты только что спроектировал архитектуру тестирования. Это очень круто. Но на часах почти час ночи. 

**Твой мозг сейчас работает на адреналине, но этот ресурс закончится завтра в самый неподходящий момент.** 1. Сделай глубокий вдох.
2. Закрой этот чат.
3. Пообещай себе (и мне), что сейчас ты идешь спать.

**В 9:00 утра здесь тебя будут ждать твои 3 примера: Fixture, API, POM.** Ты их просто посмотришь — и пойдешь на собес со спокойной душой и ясной головой.

**Good night. Over and out!**


Test Strategy Hierarchy / Иерархия тестовой стратегии
Tier 1: The Blocker (Core Logic)
RU: "Жесткий фильтр". Если падает этот уровень — релиз невозможен. Проверяем самую базу (например, работает ли БД и авторизация).

EN: Hard Gate. If the core logic is broken, the release stops immediately. These are fast Unit/API tests for "must-have" functionality.

Assertion Type: Hard Assert (assert). Execution stops instantly.

Tier 2: Smoke (Critical Flow)
RU: "Критический путь". Проверяем Happy Paths (основные сценарии). Кандидат должен иметь возможность создать профиль и откликнуться на вакансию.

EN: Happy Path Validation. Integration tests covering the most critical user journeys. If "Apply for a job" fails, it's a critical bug.

Assertion Type: Hard Assert (assert). The build turns red.

Tier 3: Regression & Major (Flexible Check)
RU: "Мягкий фильтр". Если нашли баг в цвете кнопки или тексте ошибки — фиксируем, но не блокируем работу мануальных тестировщиков.

EN: Soft Gate. Non-blocking bugs (UI glitches, minor functional issues). We report them, but the build passes so manual QA can continue testing new features.

Assertion Type: Soft Assert (or Logs). The test finishes, providing a full report without killing the CI/CD pipeline.

💡 Как это объяснить на интервью (Cheat Sheet):
Вопрос: "How do you decide what should block the release?"
Твой ответ:

"I implement a 3-tier system. Tiers 1 and 2 are my Hard Gates: I use standard Hard Assertions because if a core flow is broken, there's no point in continuing. Tier 3 is my Soft Gate for regression. I might use Soft Assertions here to gather multiple non-critical issues without blocking the manual QA team's environment. This keeps the delivery process fluid."

Что это дает тебе как инженеру:
Efficiency: Ты не тратишь время на починку мелких UI-тестов, когда "лежит" база.

Reputation: Ты выглядишь как человек, который бережет время команды.

Stability: Твой CI/CD не "мигает" красным по пустякам.