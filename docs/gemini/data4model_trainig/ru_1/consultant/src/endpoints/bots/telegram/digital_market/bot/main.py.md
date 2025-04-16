### **Анализ кода модуля `main.py`**

## \file /hypotez/src/endpoints/bots/telegram/digital_market/bot/main.py

Модуль является основной точкой входа для Telegram-бота "Digital Market". Он отвечает за настройку и запуск веб-приложения, обработку входящих запросов через webhook, регистрацию middleware и роутеров, а также обработку событий запуска и остановки бота.

**Качество кода:**

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код хорошо структурирован и разбит на отдельные функции, что облегчает понимание и поддержку.
    - Используются асинхронные функции для работы с ботом и веб-приложением, что обеспечивает высокую производительность.
    - Присутствует обработка исключений при отправке сообщений администраторам.
    - Код использует `logger` для логирования событий, что полезно для отладки и мониторинга.
- **Минусы**:
    - Отсутствуют аннотации типов для параметров функций и переменных.
    - Нет docstring для модуля.
    - Не все функции имеют подробное описание в docstring.
    - В блоках `try...except` используется `e` вместо `ex` для исключения.
    - Не все строки соответствуют PEP8 (например, отсутствие пробелов вокруг операторов).

**Рекомендации по улучшению:**

1.  **Добавить docstring для модуля**:
    - Описать назначение модуля, основные классы и функции, а также примеры использования.
2.  **Добавить аннотации типов**:
    - Указать типы для всех переменных и параметров функций.
3.  **Обновить docstring**:
    - Добавить более подробные описания для всех функций, включая аргументы, возвращаемые значения и возможные исключения.
    - Перевести существующие docstring на русский язык.
4.  **Исправить использование исключений**:
    - Заменить `e` на `ex` в блоках `try...except`.
5.  **Соблюдать PEP8**:
    - Добавить пробелы вокруг операторов присваивания и других операторов.
6.  **Добавить обработку ошибок при установке webhook**:
    - Обернуть вызов `bot.set_webhook` в блок `try...except` для обработки возможных ошибок.
7.  **Удалить неиспользуемые импорты**:
    - Проверить и удалить неиспользуемые импорты, если таковые имеются.

**Оптимизированный код:**

```python
"""
Модуль для запуска Telegram-бота "Digital Market"
=================================================

Модуль содержит основные функции для настройки и запуска веб-приложения,
обработки входящих запросов через webhook, регистрации middleware и роутеров,
а также обработки событий запуска и остановки бота.
"""

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
async def set_default_commands() -> None:
    """
    Устанавливает команды по умолчанию для бота.
    """
    commands: list[BotCommand] = [BotCommand(command='start', description='Запустить бота')]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


# Функции для запуска и остановки бота
async def on_startup(app: web.Application) -> None:
    """
    Выполняется при запуске приложения.

    Args:
        app (web.Application): Экземпляр веб-приложения aiohttp.

    Raises:
        Exception: Если не удается отправить сообщение администратору.
    """
    await set_default_commands()
    try:
        await bot.set_webhook(settings.get_webhook_url)
    except Exception as ex:
        logger.error('Ошибка при установке вебхука', ex, exc_info=True)

    for admin_id in admins:
        try:
            await bot.send_message(admin_id, 'Бот запущен 🥳.')
        except Exception as ex:
            logger.error(f'Не удалось отправить сообщение админу {admin_id}: {ex}', exc_info=True)
    logger.info('Бот успешно запущен.')


async def on_shutdown(app: web.Application) -> None:
    """
    Выполняется при остановке приложения.

    Args:
        app (web.Application): Экземпляр веб-приложения aiohttp.

    Raises:
        Exception: Если не удается отправить сообщение администратору.
    """
    for admin_id in admins:
        try:
            await bot.send_message(admin_id, 'Бот остановлен. Почему? 😔')
        except Exception as ex:
            logger.error(f'Не удалось отправить сообщение админу {admin_id}: {ex}', exc_info=True)
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.session.close()
    logger.error('Бот остановлен!')


# Регистрация мидлварей и роутеров
def register_middlewares() -> None:
    """
    Регистрирует мидлвари для диспетчера.
    """
    dp.update.middleware.register(DatabaseMiddlewareWithoutCommit())
    dp.update.middleware.register(DatabaseMiddlewareWithCommit())


def register_routers() -> None:
    """
    Регистрирует маршруты для диспетчера.
    """
    dp.include_router(catalog_router)
    dp.include_router(user_router)
    dp.include_router(admin_router)


# Функция для создания приложения aiohttp
def create_app() -> web.Application:
    """
    Создает и настраивает приложение aiohttp.
    """
    # Создаем приложение
    app: web.Application = web.Application()

    # Регистрация обработчиков маршрутов
    app.router.add_post(f'/{settings.BOT_TOKEN}', handle_webhook)
    app.router.add_post('/robokassa/result/', robokassa_result)
    app.router.add_get('/robokassa/fail/', robokassa_fail)
    app.router.add_get('/', home_page)

    # Настройка приложения с диспетчером и ботом
    setup_application(app, dp, bot=bot)

    # Регистрация функций запуска и остановки
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    return app


# Главная функция
def main() -> None:
    """
    Главная функция для запуска приложения.
    """
    # Регистрация мидлварей и роутеров
    register_middlewares()
    register_routers()

    # Создаем приложение и запускаем его
    app: web.Application = create_app()
    web.run_app(app, host=settings.SITE_HOST, port=settings.SITE_PORT)


if __name__ == '__main__':
    main()