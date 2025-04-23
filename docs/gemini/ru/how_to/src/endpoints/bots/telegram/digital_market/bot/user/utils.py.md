Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Функция `successful_payment_logic` обрабатывает логику успешной оплаты товара пользователем. Она сохраняет информацию о покупке в базе данных, отправляет уведомления администраторам о совершенной покупке и предоставляет пользователю информацию о приобретенном товаре.

Шаги выполнения
-------------------------
1. **Извлечение данных:** Извлекаются данные о продукте, цене, типе платежа, идентификаторах платежа и пользователя из объекта `payment_data`.
2. **Сохранение информации о покупке:** Функция сохраняет данные о платеже в базе данных, используя метод `PurchaseDao.add`.
3. **Получение данных о товаре:**  Запрашивает информацию о приобретенном товаре из базы данных, используя `ProductDao.find_one_or_none_by_id`.
4. **Отправка уведомлений администраторам:**  Отправляет уведомления каждому администратору о новой покупке, содержащие информацию о пользователе, названии товара, его ID и цене. В случае ошибки логирует ее.
5. **Формирование текста сообщения пользователю:** Формирует текст сообщения для пользователя с благодарностью за покупку и информацией о приобретенном товаре, включая название, описание, цену и информацию о наличии файла.
6. **Отправка информации пользователю:** В зависимости от наличия файла с товаром, отправляет либо файл с описанием, либо только текстовое сообщение пользователю.
7. **Возврат звезд за покупку (если оплата звездами):**  Если тип платежа - "stars", инициирует возврат звезд пользователю, используя метод `bot.refund_star_payment`.

Пример использования
-------------------------

```python
from aiogram import Bot
from sqlalchemy.ext.asyncio import AsyncSession
from bot.user.schemas import PaymentData
from bot.dao.dao import PurchaseDao, ProductDao
from bot.user.kbs import main_user_kb

async def successful_payment_logic(session: AsyncSession, payment_data: PaymentData, currency: str, user_tg_id: int, bot: Bot):
    """
    Обрабатывает логику успешной оплаты товара пользователем.

    Args:
        session (AsyncSession): Сессия базы данных SQLAlchemy.
        payment_data (PaymentData): Данные о платеже.
        currency (str): Валюта платежа.
        user_tg_id (int): Telegram ID пользователя.
        bot (Bot): Экземпляр бота aiogram.
    """
    product_id = int(payment_data.get("product_id"))
    price = payment_data.get("price")
    payment_type = payment_data.get("payment_type")
    payment_id = payment_data.get("payment_id")
    user_id = payment_data.get("user_id")

    # Сохранение информации о покупке
    await PurchaseDao.add(session=session, values=PaymentData(**payment_data))

    # Получение данных о товаре
    product_data = await ProductDao.find_one_or_none_by_id(session=session, data_id=product_id)

    # Отправка уведомлений администраторам (пример упрощен для краткости)
    # ...

    # Формирование текста сообщения пользователю
    file_text = "📦 <b>Товар включает файл:</b>" if product_data.file_id else "📄 <b>Товар не включает файлы:</b>"
    product_text = (
        f"🎉 <b>Спасибо за покупку!</b>\\n\\n"
        f"🛒 <b>Информация о вашем товаре:</b>\\n"
        f"━━━━━━━━━━━━━━━━━━\\n"
        f"🔹 <b>Название:</b> <b>{product_data.name}</b>\\n"
        f"🔹 <b>Описание:</b>\\n<i>{product_data.description}</i>\\n"
        f"🔹 <b>Цена:</b> <b>{price} {currency}</b>\\n"
        f"🔹 <b>Закрытое описание:</b>\\n<i>{product_data.hidden_content}</i>\\n"
        f"━━━━━━━━━━━━━━━━━━\\n"
        f"{file_text}\\n\\n"
        f"ℹ️ <b>Информацию о всех ваших покупках вы можете найти в личном профиле.</b>"
    )

    # Отправка информации пользователю
    if product_data.file_id:
        await bot.send_document(document=product_data.file_id,
                                chat_id=user_tg_id,
                                caption=product_text, reply_markup=main_user_kb(user_tg_id))
    else:
        await bot.send_message(chat_id=user_tg_id, text=product_text, reply_markup=main_user_kb(user_tg_id))

    # автоматический возврат звезд за покупку
    if payment_type == 'stars':
        await bot.refund_star_payment(user_id=user_tg_id, telegram_payment_charge_id=payment_id)

# Пример вызова функции (необходима инициализация session, payment_data, currency, user_tg_id, bot)
# await successful_payment_logic(session=session, payment_data=payment_data, currency="USD", user_tg_id=123456789, bot=bot)
```