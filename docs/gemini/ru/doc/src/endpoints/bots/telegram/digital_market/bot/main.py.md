# Модуль main.py 

## Обзор

Модуль `main.py` - точка входа в приложение Telegram бота. 

- В нем реализована логика запуска и остановки бота.
- Задаются команды по умолчанию.
- Регистрируются мидлвари и маршруты.
- Создается и настраивается приложение `aiohttp`. 

## Подробнее

Модуль `main.py`  использует стандартную архитектуру Telegram бота:

- **`aiogram`:** фреймворк для работы с ботами.
- **`aiohttp`:**  библиотека для асинхронной работы с HTTP запросами.
- **`loguru`:**  библиотека для ведения логов.

## Классы

### `DatabaseMiddlewareWithoutCommit`

**Описание**:  Мидлваря, которая подключается к базе данных без совершения коммитов (сохранения).

**Атрибуты**:

- `db` (`Database`):  Объект базы данных.

### `DatabaseMiddlewareWithCommit`

**Описание**:  Мидлваря, которая подключается к базе данных с совершением коммитов (сохранения).

**Атрибуты**:

- `db` (`Database`):  Объект базы данных.

## Функции

### `set_default_commands()`

**Назначение**:  Устанавливает команды по умолчанию для бота.

**Параметры**: 
 - `commands` (List[BotCommand]): Список команд.

**Возвращает**: 
 - `None`

**Пример**:
```python
commands = [BotCommand(command='start', description='Запустить бота')]
await bot.set_my_commands(commands, BotCommandScopeDefault())
```

### `on_startup(app)`

**Назначение**:  Функция, которая вызывается при запуске приложения `aiohttp`.

**Параметры**: 
- `app` (web.Application): Объект приложения `aiohttp`.

**Возвращает**: 
- `None`

**Как работает функция**:
-  Устанавливает команды по умолчанию для бота (`set_default_commands()`).
-  Устанавливает webhook для бота.
-  Отправляет сообщение в чат админам о запуске бота.
-  Выводит сообщение в лог о запуске бота.

**Примеры**:
```python
async def on_startup(app):
    await set_default_commands()
    await bot.set_webhook(settings.get_webhook_url)
    for admin_id in admins:
        try:
            await bot.send_message(admin_id, 'Бот запущен 🥳.')
        except Exception as e:
            logger.error(f"Не удалось отправить сообщение админу {admin_id}: {e}")
    logger.info("Бот успешно запущен.")
```

### `on_shutdown(app)`

**Назначение**:  Функция, которая вызывается при остановке приложения `aiohttp`.

**Параметры**: 
- `app` (web.Application): Объект приложения `aiohttp`.

**Возвращает**: 
- `None`

**Как работает функция**:
-  Отправляет сообщение в чат админам о остановке бота.
-  Удаляет webhook для бота.
-  Закрывает сессию бота.
-  Выводит сообщение в лог о остановке бота.

**Примеры**:
```python
async def on_shutdown(app):
    for admin_id in admins:
        try:
            await bot.send_message(admin_id, 'Бот остановлен. Почему? 😔')
        except Exception as e:
            logger.error(f"Не удалось отправить сообщение админу {admin_id}: {e}")
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.session.close()
    logger.error("Бот остановлен!")
```

### `register_middlewares()`

**Назначение**:  Регистрирует мидлвари для диспетчера бота.

**Параметры**: 
- `None`

**Возвращает**: 
- `None`

**Как работает функция**:
-  Регистрирует мидлвару `DatabaseMiddlewareWithoutCommit` для всех обновлений.
-  Регистрирует мидлвару `DatabaseMiddlewareWithCommit` для всех обновлений.

**Примеры**:
```python
def register_middlewares():
    dp.update.middleware.register(DatabaseMiddlewareWithoutCommit())
    dp.update.middleware.register(DatabaseMiddlewareWithCommit())
```

### `register_routers()`

**Назначение**:  Регистрирует маршруты (роутеры) для диспетчера бота.

**Параметры**: 
- `None`

**Возвращает**: 
- `None`

**Как работает функция**:
-  Включает маршрут `catalog_router`.
-  Включает маршрут `user_router`.
-  Включает маршрут `admin_router`.

**Примеры**:
```python
def register_routers():
    dp.include_router(catalog_router)
    dp.include_router(user_router)
    dp.include_router(admin_router)
```

### `create_app()`

**Назначение**:  Создает и настраивает приложение `aiohttp`.

**Параметры**: 
- `None`

**Возвращает**: 
- `web.Application`: Объект приложения `aiohttp`.

**Как работает функция**:
-  Создает приложение `aiohttp`.
-  Регистрирует обработчики маршрутов (роутеры).
-  Настраивает приложение с помощью диспетчера `dp` и бота `bot`.
-  Регистрирует функции запуска (`on_startup`) и остановки (`on_shutdown`).

**Примеры**:
```python
def create_app():
    app = web.Application()
    app.router.add_post(f"/{settings.BOT_TOKEN}", handle_webhook)
    app.router.add_post("/robokassa/result/", robokassa_result)
    app.router.add_get("/robokassa/fail/", robokassa_fail)
    app.router.add_get("/", home_page)
    setup_application(app, dp, bot=bot)
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    return app
```

### `main()`

**Назначение**:  Главная функция для запуска приложения.

**Параметры**: 
- `None`

**Возвращает**: 
- `None`

**Как работает функция**:
-  Регистрирует мидлвари (`register_middlewares()`).
-  Регистрирует маршруты (`register_routers()`).
-  Создает приложение `aiohttp` (`create_app()`).
-  Запускает приложение.

**Примеры**:
```python
def main():
    register_middlewares()
    register_routers()
    app = create_app()
    web.run_app(app, host=settings.SITE_HOST, port=settings.SITE_PORT)