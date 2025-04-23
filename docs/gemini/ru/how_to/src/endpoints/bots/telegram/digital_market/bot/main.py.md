### Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код представляет собой основной файл для запуска Telegram-бота, предназначенного для работы в цифровом рынке. Он инициализирует и настраивает бота, регистрирует обработчики, мидлвари и роутеры, а также запускает веб-сервер на базе `aiohttp` для обработки входящих запросов, включая webhook от Telegram и ответы от Robokassa.

Шаги выполнения
-------------------------
1. **Импорт необходимых модулей**:
   - Импортируются модули из `aiogram` для работы с Telegram API и webhook.
   - Импортируются `web` из `aiohttp` для создания веб-приложения.
   - Импортируются модули для логирования (`logger`), обработки webhook и результатов Robokassa.
   - Импортируются конфигурационные данные (`bot`, `admins`, `dp`, `settings`).
   - Импортируются мидлвари для работы с базой данных (`DatabaseMiddlewareWithoutCommit`, `DatabaseMiddlewareWithCommit`).
   - Импортируются роутеры для обработки различных типов запросов (`admin_router`, `user_router`, `catalog_router`).

2. **Определение асинхронной функции `set_default_commands()`**:
   - Функция устанавливает команды по умолчанию для бота (например, `/start`).
   - Использует `bot.set_my_commands()` для установки команд.

3. **Определение асинхронной функции `on_startup(app)`**:
   - Функция выполняется при запуске приложения.
   - Вызывает `set_default_commands()` для установки команд бота.
   - Устанавливает webhook для бота, используя URL из настроек (`settings.get_webhook_url`).
   - Отправляет сообщение всем администраторам (`admins`) об успешном запуске бота.
   - Логирует информацию о запуске бота.

4. **Определение асинхронной функции `on_shutdown(app)`**:
   - Функция выполняется при остановке приложения.
   - Отправляет сообщение всем администраторам (`admins`) об остановке бота.
   - Удаляет webhook бота.
   - Закрывает сессию бота.
   - Логирует информацию об остановке бота.

5. **Определение функции `register_middlewares()`**:
   - Регистрирует мидлвари для диспетчера (`dp`).
   - Мидлвари используются для обработки каждого обновления.
   - Регистрируются `DatabaseMiddlewareWithoutCommit` и `DatabaseMiddlewareWithCommit` для управления сессиями базы данных.

6. **Определение функции `register_routers()`**:
   - Регистрирует роутеры для диспетчера (`dp`).
   - Роутеры используются для обработки различных типов команд и запросов.
   - Регистрируются `catalog_router`, `user_router` и `admin_router`.

7. **Определение функции `create_app()`**:
   - Создает приложение `aiohttp`.
   - Регистрирует обработчики маршрутов, такие как `/`, `/robokassa/result/`, `/robokassa/fail/` и маршрут для обработки webhook от Telegram.
   - Настраивает приложение с диспетчером и ботом с помощью `setup_application`.
   - Регистрирует функции запуска (`on_startup`) и остановки (`on_shutdown`) приложения.

8. **Определение функции `main()`**:
   - Главная функция для запуска приложения.
   - Регистрирует мидлвари и роутеры.
   - Создает приложение с помощью `create_app()`.
   - Запускает веб-приложение, используя `web.run_app()`.

9. **Запуск приложения**:
   - Если файл запускается напрямую (`if __name__ == "__main__":`), вызывается функция `main()`.

Пример использования
-------------------------

```python
from aiogram.webhook.aiohttp_server import setup_application
from aiohttp import web
from aiogram.types import BotCommand, BotCommandScopeDefault
from loguru import logger
from bot.app.app import handle_webhook, robokassa_result, robokassa_fail, home_page
from bot.config import bot, admins, dp, settings
from bot.dao.database_middleware import DatabaseMiddlewareWithoutCommit, DatabaseMiddlewareWithCommit
from bot.admin.admin import admin_router
from bot.user.user_router import user_router
from bot.user.catalog_router import catalog_router


# Функция для установки команд по умолчанию для бота
async def set_default_commands():
    """
    Устанавливает команды по умолчанию для бота.
    """
    commands = [BotCommand(command='start', description='Запустить бота')]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


# Функции для запуска и остановки бота
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


# Регистрация мидлварей и роутеров
def register_middlewares():
    """
    Регистрирует мидлвари для диспетчера.
    """
    dp.update.middleware.register(DatabaseMiddlewareWithoutCommit())
    dp.update.middleware.register(DatabaseMiddlewareWithCommit())


def register_routers():
    """
    Регистрирует маршруты для диспетчера.
    """
    dp.include_router(catalog_router)
    dp.include_router(user_router)
    dp.include_router(admin_router)


# Функция для создания приложения aiohttp
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


# Главная функция
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


if __name__ == "__main__":
    main()