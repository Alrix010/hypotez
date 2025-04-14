### **Анализ кода модуля `utils.py`**

**Качество кода:**

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код выполняет логику обработки успешной оплаты, включая добавление информации о покупке в БД, отправку уведомлений администраторам и предоставление информации пользователю.
    - Используется `AsyncSession` для асинхронной работы с базой данных.
    - Есть обработка ошибок при отправке уведомлений администраторам.
- **Минусы**:
    - Отсутствуют аннотации типов для параметров функций, что ухудшает читаемость и усложняет отладку.
    - В блоке `except` используется переменная `e` вместо `ex`.
    - Используется `logger.error` без передачи `exc_info=True`, что может затруднить отладку.
    - В коде используется f-строки, что хорошо, но можно улучшить форматирование текста.
    - Не все переменные аннотированы типами.

**Рекомендации по улучшению:**

- Добавить аннотации типов для параметров и возвращаемых значений функции `successful_payment_logic`.
- Использовать `ex` вместо `e` в блоке `except`.
- Добавить `exc_info=True` в `logger.error` для получения полной информации об ошибке.
- Улучшить форматирование текста, чтобы сделать его более читаемым.
- Добавить комментарии к коду, чтобы объяснить логику работы каждой части.
- Добавить docstring к функции `successful_payment_logic` для описания ее назначения, аргументов и возвращаемого значения.

**Оптимизированный код:**

```python
from aiogram import Bot
from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession
from bot.config import settings
from bot.dao.dao import PurchaseDao, ProductDao
from bot.user.kbs import main_user_kb
from bot.user.schemas import PaymentData
from typing import Dict, Any, Optional


async def successful_payment_logic(
    session: AsyncSession,
    payment_data: Dict[str, Any],
    currency: str,
    user_tg_id: int,
    bot: Bot
) -> None:
    """
    Обрабатывает логику успешной оплаты, включая добавление информации о покупке в БД,
    отправку уведомлений администраторам и предоставление информации пользователю.

    Args:
        session (AsyncSession): Сессия базы данных SQLAlchemy.
        payment_data (Dict[str, Any]): Данные о платеже.
        currency (str): Валюта платежа.
        user_tg_id (int): Telegram ID пользователя.
        bot (Bot): Объект бота aiogram.

    Returns:
        None
    """
    product_id: int = int(payment_data.get("product_id")) # ID продукта
    price: str = payment_data.get("price") # Цена товара
    payment_type: str = payment_data.get("payment_type") # Тип платежа
    payment_id: str = payment_data.get("payment_id") # ID платежа
    user_id: str = payment_data.get("user_id") # ID пользователя

    # Добавление информации о покупке в базу данных
    await PurchaseDao.add(session=session, values=PaymentData(**payment_data))

    # Получение данных о продукте
    product_data = await ProductDao.find_one_or_none_by_id(session=session, data_id=product_id)

    # Отправка уведомлений администраторам
    for admin_id in settings.ADMIN_IDS:
        try:
            await bot.send_message(
                chat_id=admin_id,
                text=(
                    f"💲 Пользователь c ID {user_id} купил товар <b>{product_data.name}</b> (ID: {product_id}) "
                    f"за <b>{price} {currency}</b>."
                )
            )
        except Exception as ex:
            logger.error(f"Ошибка при отправке уведомления администраторам: {ex}", exc_info=True)

    # Определение текста для информации о файле
    file_text: str = "📦 <b>Товар включает файл:</b>" if product_data.file_id else "📄 <b>Товар не включает файлы:</b>"
    
    # Формирование текста сообщения пользователю
    product_text: str = (
        f"🎉 <b>Спасибо за покупку!</b>\n\n"
        f"🛒 <b>Информация о вашем товаре:</b>\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"🔹 <b>Название:</b> <b>{product_data.name}</b>\n"
        f"🔹 <b>Описание:</b>\n<i>{product_data.description}</i>\n"
        f"🔹 <b>Цена:</b> <b>{price} {currency}</b>\n"
        f"🔹 <b>Закрытое описание:</b>\n<i>{product_data.hidden_content}</i>\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"{file_text}\n\n"
        f"ℹ️ <b>Информацию о всех ваших покупках вы можете найти в личном профиле.</b>"
    )

    # Отправка документа или сообщения пользователю
    if product_data.file_id:
        await bot.send_document(
            document=product_data.file_id,
            chat_id=user_tg_id,
            caption=product_text,
            reply_markup=main_user_kb(user_tg_id)
        )
    else:
        await bot.send_message(
            chat_id=user_tg_id,
            text=product_text,
            reply_markup=main_user_kb(user_tg_id)
        )

    # Автоматический возврат звезд за покупку
    if payment_type == 'stars':
        await bot.refund_star_payment(user_id=user_tg_id, telegram_payment_charge_id=payment_id)