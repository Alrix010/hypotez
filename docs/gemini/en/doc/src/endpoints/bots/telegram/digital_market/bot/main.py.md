# Module main.py

## Overview

Модуль `main.py` является точкой входа для Telegram-бота цифрового рынка. Он отвечает за настройку и запуск веб-приложения aiohttp, регистрацию обработчиков, мидлварей и роутеров, а также установку команд по умолчанию для бота.

## More details

Модуль использует библиотеки `aiogram`, `aiohttp`, `loguru` для создания и управления Telegram-ботом. Он также содержит функции для обработки webhook-ов, результатов Robokassa, а также для запуска и остановки бота.

## Functions

### `set_default_commands`

```python
async def set_default_commands():
    """
    Устанавливает команды по умолчанию для бота.
    """
    commands = [BotCommand(command='start', description='Запустить бота')]
    await bot.set_my_commands(commands, BotCommandScopeDefault())
```

**Purpose**: Устанавливает команды по умолчанию для Telegram-бота.

**How the function works**:
- Создает список команд, в котором содержится команда `/start` с описанием "Запустить бота".
- Использует метод `set_my_commands` объекта `bot` для установки этих команд для всех пользователей бота.

**Parameters**:
- Отсутствуют.

**Returns**:
- Отсутствует.

**Raises**:
- Отсутствуют.

**Examples**:

```python
await set_default_commands()
```

### `on_startup`

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
        except Exception as ex:
            logger.error(f"Не удалось отправить сообщение админу {admin_id}: {ex}")
    logger.info("Бот успешно запущен.")
```

**Purpose**: Выполняет действия при запуске приложения.

**How the function works**:
- Устанавливает команды по умолчанию, вызывая функцию `set_default_commands`.
- Устанавливает webhook для бота, используя URL, полученный из настроек (`settings.get_webhook_url`).
- Отправляет сообщение всем администраторам бота об успешном запуске. В случае ошибки при отправке сообщения администратору, регистрирует ошибку в лог.
- Регистрирует информацию об успешном запуске бота в лог.

**Parameters**:
- `app`: Экземпляр приложения aiohttp.

**Returns**:
- Отсутствует.

**Raises**:
- Отсутствуют.

**Examples**:

```python
await on_startup(app)
```

### `on_shutdown`

```python
async def on_shutdown(app):
    """
    Выполняется при остановке приложения.
    """
    for admin_id in admins:
        try:
            await bot.send_message(admin_id, 'Бот остановлен. Почему? 😔')
        except Exception as ex:
            logger.error(f"Не удалось отправить сообщение админу {admin_id}: {ex}")
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.session.close()
    logger.error("Бот остановлен!")
```

**Purpose**: Выполняет действия при остановке приложения.

**How the function works**:
- Отправляет сообщение всем администраторам бота об остановке бота. В случае ошибки при отправке сообщения администратору, регистрирует ошибку в лог.
- Удаляет webhook бота, чтобы бот перестал получать обновления.
- Закрывает сессию бота.
- Регистрирует информацию об остановке бота в лог.

**Parameters**:
- `app`: Экземпляр приложения aiohttp.

**Returns**:
- Отсутствует.

**Raises**:
- Отсутствуют.

**Examples**:

```python
await on_shutdown(app)
```

### `register_middlewares`

```python
def register_middlewares():
    """
    Регистрирует мидлвари для диспетчера.
    """
    dp.update.middleware.register(DatabaseMiddlewareWithoutCommit())
    dp.update.middleware.register(DatabaseMiddlewareWithCommit())
```

**Purpose**: Регистрирует мидлвари для диспетчера `dp`.

**How the function works**:
- Регистрирует два мидлваря: `DatabaseMiddlewareWithoutCommit` и `DatabaseMiddlewareWithCommit`. Эти мидлвари, вероятно, используются для управления сессиями базы данных без коммита и с коммитом соответственно.

**Parameters**:
- Отсутствуют.

**Returns**:
- Отсутствует.

**Raises**:
- Отсутствуют.

**Examples**:

```python
register_middlewares()
```

### `register_routers`

```python
def register_routers():
    """
    Регистрирует маршруты для диспетчера.
    """
    dp.include_router(catalog_router)
    dp.include_router(user_router)
    dp.include_router(admin_router)
```

**Purpose**: Регистрирует маршруты (роутеры) для диспетчера `dp`.

**How the function works**:
- Включает три роутера: `catalog_router`, `user_router` и `admin_router`. Это позволяет диспетчеру обрабатывать различные типы запросов, связанные с каталогом, пользователями и административными функциями.

**Parameters**:
- Отсутствуют.

**Returns**:
- Отсутствует.

**Raises**:
- Отсутствуют.

**Examples**:

```python
register_routers()
```

### `create_app`

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

**Purpose**: Создает и настраивает приложение aiohttp.

**How the function works**:
- Создает экземпляр приложения aiohttp.
- Регистрирует обработчики маршрутов для различных конечных точек, таких как webhook для бота, результаты Robokassa, неудачи Robokassa и главная страница.
- Настраивает приложение с диспетчером и ботом, используя функцию `setup_application`.
- Регистрирует функции `on_startup` и `on_shutdown` для выполнения при запуске и остановке приложения соответственно.
- Возвращает настроенное приложение aiohttp.

**Parameters**:
- Отсутствуют.

**Returns**:
- `app`: Экземпляр приложения aiohttp.

**Raises**:
- Отсутствуют.

**Examples**:

```python
app = create_app()
```

### `main`

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

**Purpose**: Главная функция для запуска приложения.

**How the function works**:
- Регистрирует мидлвари и роутеры, вызывая функции `register_middlewares` и `register_routers`.
- Создает приложение, вызывая функцию `create_app`.
- Запускает приложение aiohttp, используя функцию `web.run_app`, с хостом и портом, полученными из настроек.

**Parameters**:
- Отсутствуют.

**Returns**:
- Отсутствует.

**Raises**:
- Отсутствуют.

**Examples**:

```python
main()