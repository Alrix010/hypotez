### **Системные инструкции для обработки кода проекта `hypotez`**

=========================================================================================

Описание функциональности и правил для генерации, анализа и улучшения кода. Направлено на обеспечение последовательного и читаемого стиля кодирования, соответствующего требованиям.

---

### **Основные принципы**

#### **1. Общие указания**:
- Соблюдай четкий и понятный стиль кодирования.
- Все изменения должны быть обоснованы и соответствовать установленным требованиям.

#### **2. Комментарии**:
- Используй `#` для внутренних комментариев.
- Документация всех функций, методов и классов должна следовать такому формату: 
    ```python
        def function(param: str, param1: Optional[str | dict | str] = None) -> dict | None:
            """ 
            Args:
                param (str): Описание параметра `param`.
                param1 (Optional[str | dict | str], optional): Описание параметра `param1`. По умолчанию `None`.
    
            Returns:
                dict | None: Описание возващаемого значения. Возвращает словарь или `None`.
    
            Raises:
                SomeError: Описание ситуации, в которой возникает исключение `SomeError`.

            Ехаmple:
                >>> function('param', 'param1')
                {'param': 'param1'}
            """
    ```
- Комментарии и документация должны быть четкими, лаконичными и точными.

#### **3. Форматирование кода**:
- Используй одинарные кавычки. `a:str = 'value'`, `print('Hello World!')`;
- Добавляй пробелы вокруг операторов. Например, `x = 5`;
- Все параметры должны быть аннотированы типами. `def function(param: str, param1: Optional[str | dict | str] = None) -> dict | None:`;
- Не используй `Union`. Вместо этого используй `|`.

#### **4. Логирование**:
- Для логгирования Всегда Используй модуль `logger` из `src.logger.logger`.
- Ошибки должны логироваться с использованием `logger.error`.
Пример:
    ```python
        try:
            ...
        except Exception as ex:
            logger.error('Error while processing data', ех, exc_info=True)
    ```
#### **5 Не используй `Union[]` в коде. Вместо него используй `|`
Например:
```python
x: str | int ...
```




---

### **Основные требования**:

#### **1. Формат ответов в Markdown**:
- Все ответы должны быть выполнены в формате **Markdown**.

#### **2. Формат комментариев**:
- Используй указанный стиль для комментариев и документации в коде.
- Пример:

```python
from typing import Generator, Optional, List
from pathlib import Path


def read_text_file(
    file_path: str | Path,
    as_list: bool = False,
    extensions: Optional[List[str]] = None,
    chunk_size: int = 8192,
) -> Generator[str, None, None] | str | None:
    """
    Считывает содержимое файла (или файлов из каталога) с использованием генератора для экономии памяти.

    Args:
        file_path (str | Path): Путь к файлу или каталогу.
        as_list (bool): Если `True`, возвращает генератор строк.
        extensions (Optional[List[str]]): Список расширений файлов для чтения из каталога.
        chunk_size (int): Размер чанков для чтения файла в байтах.

    Returns:
        Generator[str, None, None] | str | None: Генератор строк, объединенная строка или `None` в случае ошибки.

    Raises:
        Exception: Если возникает ошибка при чтении файла.

    Example:
        >>> from pathlib import Path
        >>> file_path = Path('example.txt')
        >>> content = read_text_file(file_path)
        >>> if content:
        ...    print(f'File content: {content[:100]}...')
        File content: Example text...
    """
    ...
```
- Всегда делай подробные объяснения в комментариях. Избегай расплывчатых терминов, 
- таких как *«получить»* или *«делать»*
-  . Вместо этого используйте точные термины, такие как *«извлечь»*, *«проверить»*, *«выполнить»*.
- Вместо: *«получаем»*, *«возвращаем»*, *«преобразовываем»* используй имя объекта *«функция получае»*, *«переменная возвращает»*, *«код преобразовывает»* 
- Комментарии должны непосредственно предшествовать описываемому блоку кода и объяснять его назначение.

#### **3. Пробелы вокруг операторов присваивания**:
- Всегда добавляйте пробелы вокруг оператора `=`, чтобы повысить читаемость.
- Примеры:
  - **Неправильно**: `x=5`
  - **Правильно**: `x = 5`

#### **4. Использование `j_loads` или `j_loads_ns`**:
- Для чтения JSON или конфигурационных файлов замените стандартное использование `open` и `json.load` на `j_loads` или `j_loads_ns`.
- Пример:

```python
# Неправильно:
with open('config.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Правильно:
data = j_loads('config.json')
```

#### **5. Сохранение комментариев**:
- Все существующие комментарии, начинающиеся с `#`, должны быть сохранены без изменений в разделе «Улучшенный код».
- Если комментарий кажется устаревшим или неясным, не изменяйте его. Вместо этого отметьте его в разделе «Изменения».

#### **6. Обработка `...` в коде**:
- Оставляйте `...` как указатели в коде без изменений.
- Не документируйте строки с `...`.
```

#### **7. Аннотации**
Для всех переменных должны быть определены аннотации типа. 
Для всех функций все входные и выходные параметры аннотириваны
Для все параметров должны быть аннотации типа.


### **8. webdriver**
В коде используется webdriver. Он импртируется из модуля `webdriver` проекта `hypotez`
```python
from src.webdirver import Driver, Chrome, Firefox, Playwright, ...
driver = Driver(Firefox)

Пoсле чего может использоваться как

close_banner = {
  "attribute": null,
  "by": "XPATH",
  "selector": "//button[@id = 'closeXButton']",
  "if_list": "first",
  "use_mouse": false,
  "mandatory": false,
  "timeout": 0,
  "timeout_for_event": "presence_of_element_located",
  "event": "click()",
  "locator_description": "Закрываю pop-up окно, если оно не появилось - не страшно (`mandatory`:`false`)"
}

result = driver.execute_locator(close_banner)
```

## Анализ кода `hypotez/src/endpoints/bots/telegram/digital_market/bot/main.py`

### 1. Блок-схема

```mermaid
graph TD
    A[Начало: `main()`] --> B{Регистрация мидлварей: `register_middlewares()`};
    B -- Да --> C{Регистрация роутеров: `register_routers()`};
    C -- Да --> D{Создание приложения: `create_app()`};
    D -- Создано --> E{Запуск приложения: `web.run_app()`};
    E --> F[Конец];

    subgraph `register_middlewares()`
    M1[dp.update.middleware.register(DatabaseMiddlewareWithoutCommit())] --> M2[dp.update.middleware.register(DatabaseMiddlewareWithCommit())];
    end

    subgraph `register_routers()`
    R1[dp.include_router(catalog_router)] --> R2[dp.include_router(user_router)] --> R3[dp.include_router(admin_router)];
    end

    subgraph `create_app()`
    CA1[app = web.Application()] --> CA2{Регистрация обработчиков: app.router.add_post()} --> CA3[setup_application(app, dp, bot=bot)] --> CA4{Регистрация событий: app.on_startup.append(), app.on_shutdown.append()};
    end

    subgraph `on_startup(app)`
    S1[await set_default_commands()] --> S2[await bot.set_webhook()] --> S3{Отправка сообщения администраторам};
    S3 -- Успешно --> S4[logger.info("Бот успешно запущен.")]
    S3 -- Ошибка --> S4
    end

    subgraph `on_shutdown(app)`
    SH1{Отправка сообщения администраторам} --> SH2[await bot.delete_webhook()] --> SH3[await bot.session.close()] --> SH4[logger.error("Бот остановлен!")];
    SH1 -- Ошибка --> SH2
    end

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style F fill:#f9f,stroke:#333,stroke-width:2px
```

**Примеры для логических блоков:**

*   **Регистрация мидлварей**: Регистрируются `DatabaseMiddlewareWithoutCommit` и `DatabaseMiddlewareWithCommit` для обработки запросов к базе данных.
    *   `DatabaseMiddlewareWithoutCommit`:  Не выполняет коммит транзакции.
    *   `DatabaseMiddlewareWithCommit`: Выполняет коммит транзакции.
*   **Регистрация роутеров**: Регистрируются роутеры `catalog_router`, `user_router` и `admin_router` для обработки различных типов запросов.
    *   `catalog_router`: Обрабатывает запросы, связанные с каталогом товаров.
    *   `user_router`: Обрабатывает запросы, связанные с пользователями.
    *   `admin_router`: Обрабатывает запросы, связанные с административными функциями.
*   **Создание приложения**: Создается экземпляр `aiohttp.web.Application`, регистрируются обработчики маршрутов (`handle_webhook`, `robokassa_result`, `robokassa_fail`, `home_page`) и настраивается приложение с диспетчером (`dp`) и ботом (`bot`).
    *   `handle_webhook`: Обрабатывает входящие webhook запросы от Telegram.
    *   `robokassa_result`: Обрабатывает результат оплаты через Robokassa.
    *   `robokassa_fail`: Обрабатывает неудачную оплату через Robokassa.
    *   `home_page`: Обрабатывает запросы к главной странице.
*   **Запуск приложения**: Приложение запускается с использованием `web.run_app()` на указанном хосте и порту.
*   **`on_startup(app)`**: Функция, выполняющаяся при запуске приложения: устанавливает команды по умолчанию, устанавливает webhook, отправляет сообщение администраторам об успешном запуске бота.
*   **`on_shutdown(app)`**: Функция, выполняющаяся при остановке приложения: отправляет сообщение администраторам об остановке бота, удаляет webhook, закрывает сессию бота.

### 2. Диаграмма

```mermaid
graph TD
    subgraph "main.py"
    A[main()] --> B(register_middlewares());
    B --> C(register_routers());
    C --> D(create_app());
    D --> E(web.run_app());
    end

    subgraph "Мидлвари"
    B --> F[DatabaseMiddlewareWithoutCommit];
    B --> G[DatabaseMiddlewareWithCommit];
    end

    subgraph "Роутеры"
    C --> H[catalog_router];
    C --> I[user_router];
    C --> J[admin_router];
    end

    subgraph "create_app()"
    D --> K[handle_webhook];
    D --> L[robokassa_result];
    D --> M[robokassa_fail];
    D --> N[home_page];
    D --> O(setup_application);
    O --> P[dp];
    O --> Q[bot];
    D --> R(on_startup);
    D --> S(on_shutdown);
    end

    subgraph "on_startup"
    R --> T(set_default_commands);
    R --> U(bot.set_webhook);
    R --> V{Отправка сообщения администраторам};
    end

    subgraph "on_shutdown"
    S --> W{Отправка сообщения администраторам};
    S --> X(bot.delete_webhook);
    S --> Y(bot.session.close);
    end

    subgraph "config.py"
    style AA fill:#ccf,stroke:#333,stroke-width:2px
    AA[settings]
    AA --> E
    AA --> U
    AA --> K
    end

    subgraph "aiogram"
    style BB fill:#ccf,stroke:#333,stroke-width:2px
    BB[aiogram]
    BB --> O
    BB --> T
    BB --> U
    BB --> X
    BB --> Y
    end

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style E fill:#f9f,stroke:#333,stroke-width:2px

```

**Анализ зависимостей:**

*   `aiogram.webhook.aiohttp_server`: Используется для настройки webhook для бота, что позволяет боту получать обновления в реальном времени через HTTP.
*   `aiohttp`: Используется как веб-фреймворк для создания веб-приложения, обрабатывающего webhook запросы и другие HTTP запросы (например, для Robokassa).
*   `aiogram.types`: Используется для определения типов данных, таких как `BotCommand` и `BotCommandScopeDefault`, необходимых для работы с Telegram Bot API.
*   `loguru`: Используется для логирования событий и ошибок в приложении.
*   `bot.app.app`: Содержит функции-обработчики для webhook запросов, результатов Robokassa, неудачных оплат и главной страницы.
*   `bot.config`: Содержит настройки бота, такие как токен бота, список администраторов и URL webhook.
*   `bot.dao.database_middleware`: Содержит мидлвари для управления сессиями базы данных.
*   `bot.admin.admin`: Содержит роутер для административных функций бота.
*   `bot.user.user_router`: Содержит роутер для пользовательских функций бота.
*   `bot.user.catalog_router`: Содержит роутер для функций каталога бота.

### 3. Объяснение

#### Импорты:

*   `from aiogram.webhook.aiohttp_server import setup_application`: Функция для интеграции aiogram с aiohttp для обработки webhook запросов.
*   `from aiohttp import web`: Модуль aiohttp для создания веб-приложения.
*   `from aiogram.types import BotCommand, BotCommandScopeDefault`: Типы данных aiogram для работы с командами бота.
*   `from loguru import logger`: Библиотека для логирования событий.
*   `from bot.app.app import handle_webhook, robokassa_result, robokassa_fail, home_page`: Функции-обработчики для различных HTTP endpoint'ов.
*   `from bot.config import bot, admins, dp, settings`: Объекты бота, список администраторов, диспетчер и настройки.
*   `from bot.dao.database_middleware import DatabaseMiddlewareWithoutCommit, DatabaseMiddlewareWithCommit`: Мидлвари для управления сессиями базы данных.
*   `from bot.admin.admin import admin_router`: Роутер для административных функций.
*   `from bot.user.user_router import user_router`: Роутер для пользовательских функций.
*   `from bot.user.catalog_router import catalog_router`: Роутер для функций каталога.

#### Классы:

В данном коде нет определения новых классов, но используются классы из импортированных модулей, такие как `web.Application` из `aiohttp` и `BotCommand` из `aiogram`.

#### Функции:

*   `set_default_commands()`: Устанавливает команды по умолчанию для бота (например, `/start`).
    ```python
    async def set_default_commands():
        """
        Устанавливает команды по умолчанию для бота.
        """
        commands = [BotCommand(command='start', description='Запустить бота')]
        await bot.set_my_commands(commands, BotCommandScopeDefault())
    ```
*   `on_startup(app)`: Выполняется при запуске приложения. Устанавливает webhook, отправляет сообщение администраторам.
    ```python
    async def on_startup(app):
        """
        Выполняется при запуске приложения.
        """
        await set_default_commands()
        await bot.set_webhook(settings.get_webhook_url)
        for admin_id in admins:
            try:
                await bot.send_message(admin_id, 'Бот запущен 🥳.')
            except Exception as e:
                logger.error(f"Не удалось отправить сообщение админу {admin_id}: {e}")
        logger.info("Бот успешно запущен.")
    ```
*   `on_shutdown(app)`: Выполняется при остановке приложения. Отправляет сообщение администраторам, удаляет webhook, закрывает сессию бота.
    ```python
    async def on_shutdown(app):
        """
        Выполняется при остановке приложения.
        """
        for admin_id in admins:
            try:
                await bot.send_message(admin_id, 'Бот остановлен. Почему? 😔')
            except Exception as e:
                logger.error(f"Не удалось отправить сообщение админу {admin_id}: {e}")
        await bot.delete_webhook(drop_pending_updates=True)
        await bot.session.close()
        logger.error("Бот остановлен!")
    ```
*   `register_middlewares()`: Регистрирует мидлвари для диспетчера.
    ```python
    def register_middlewares():
        """
        Регистрирует мидлвари для диспетчера.
        """
        dp.update.middleware.register(DatabaseMiddlewareWithoutCommit())
        dp.update.middleware.register(DatabaseMiddlewareWithCommit())
    ```
*   `register_routers()`: Регистрирует роутеры для диспетчера.
    ```python
    def register_routers():
        """
        Регистрирует маршруты для диспетчера.
        """
        dp.include_router(catalog_router)
        dp.include_router(user_router)
        dp.include_router(admin_router)
    ```
*   `create_app()`: Создает и настраивает приложение aiohttp.
    ```python
    def create_app():
        """
        Создает и настраивает приложение aiohttp.
        """
        # Создаем приложение
        app = web.Application()

        # Регистрация обработчиков маршрутов
        app.router.add_post(f"/{settings.BOT_TOKEN}", handle_webhook)
        app.router.add_post("/robokassa/result/", robokassa_result)
        app.router.add_get("/robokassa/fail/", robokassa_fail)
        app.router.add_get("/", home_page)

        # Настройка приложения с диспетчером и ботом
        setup_application(app, dp, bot=bot)

        # Регистрация функций запуска и остановки
        app.on_startup.append(on_startup)
        app.on_shutdown.append(on_shutdown)

        return app
    ```
*   `main()`: Главная функция для запуска приложения.
    ```python
    def main():
        """
        Главная функция для запуска приложения.
        """
        # Регистрация мидлварей и роутеров
        register_middlewares()
        register_routers()

        # Создаем приложение и запускаем его
        app = create_app()
        web.run_app(app, host=settings.SITE_HOST, port=settings.SITE_PORT)
    ```

#### Переменные:

*   `commands`: Список команд для бота.
*   `admins`: Список ID администраторов бота.
*   `dp`: Диспетчер aiogram.
*   `bot`: Объект бота aiogram.
*   `settings`: Объект настроек.
*   `app`: Объект приложения aiohttp.

#### Потенциальные ошибки и области для улучшения:

*   Обработка ошибок при отправке сообщений администраторам в функциях `on_startup` и `on_shutdown` может быть улучшена. Сейчас логируется только факт ошибки, но не предпринимается никаких действий для повторной отправки сообщения или уведомления об ошибке другим способом.
*   В функции `on_shutdown` можно добавить более подробное логирование причины остановки бота.
*   Использовать `j_loads` для чтения конфигурационных файлов не было нужно, т.к. здесь нет чтения конфигов.
*   В данном коде отсутствует проверка наличия необходимых переменных окружения (например, токена бота).

#### Взаимосвязи с другими частями проекта:

*   Файл `main.py` является точкой входа для Telegram-бота и зависит от модулей `bot.config`, `bot.dao`, `bot.admin`, `bot.user`, которые определяют конфигурацию, модели данных, административные и пользовательские функции бота соответственно.
*   Обработчики (`handle_webhook`, `robokassa_result`, `robokassa_fail`, `home_page`) из `bot.app.app` определяют логику обработки входящих запросов.
*   Мидлвари (`DatabaseMiddlewareWithoutCommit`, `DatabaseMiddlewareWithCommit`) обеспечивают управление транзакциями базы данных.