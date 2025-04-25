## Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот блок кода реализует обработчик команд и кнопок для пользователя в Telegram-боте. Он отвечает за регистрацию нового пользователя, показ приветственного сообщения, вывод информации о магазине,  отображение профиля пользователя с покупками и  детализацией приобретенных товаров.

Шаги выполнения
-------------------------
1. **Регистрация нового пользователя:**
    - При получении команды `/start` бот проверяет, зарегистрирован ли пользователь в базе данных.
    - Если пользователь найден, бот приветствует его и предлагает выбрать действие.
    - Если пользователя нет, бот регистрирует его с помощью `UserDAO.add()`,  получая имя, фамилию и username из `Message` и сохраняя их в базу данных.
    - После регистрации  бот приветствует пользователя  и предлагает выбрать действие.
2. **Обработка кнопки "Главная страница":**
    - При нажатии кнопки "home" бот отправляет сообщение "Главная страница".
    - Затем  бот отображает приветственное сообщение с выбором действия.
3. **Обработка кнопки "О магазине":**
    - При нажатии кнопки "about" бот отправляет сообщение "О магазине".
    - Затем бот выводит информацию о магазине, включая авторство, цели проекта, краткое описание, а также тестовые данные для оплаты. 
4. **Обработка кнопки "Профиль":**
    - При нажатии кнопки "my_profile" бот отправляет сообщение "Профиль".
    - Затем бот получает статистику покупок пользователя из базы данных с помощью `UserDAO.get_purchase_statistics()`.
    - Если у пользователя нет покупок, бот выводит сообщение об этом и предлагает открыть каталог.
    - Если у пользователя есть покупки, бот выводит информацию о количестве покупок и общей сумме. 
    - Далее бот предлагает пользователю просмотреть детали покупок.
5. **Обработка кнопки "Мои покупки":**
    - При нажатии кнопки "purchases" бот отправляет сообщение "Мои покупки".
    - Затем бот получает список покупок пользователя из базы данных с помощью `UserDAO.get_purchased_products()`.
    - Если у пользователя нет покупок, бот выводит сообщение об этом и предлагает открыть каталог.
    - Если у пользователя есть покупки, бот перебирает каждую покупку и отправляет информацию о товаре, включая название, описание, цену, скрытое описание и наличие файла.
    - Если у товара есть файл, бот отправляет файл с текстом о товаре.
    - Если у товара нет файла, бот отправляет только текст о товаре.
    - После обработки всех покупок, бот отправляет сообщение с благодарностью.
    
Пример использования
-------------------------

```python
# Импорт необходимых модулей
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession
from bot.dao.dao import UserDAO
from bot.user.kbs import main_user_kb, purchases_kb
from bot.user.schemas import TelegramIDModel, UserModel

# Создание роутера для пользователя
user_router = Router()

# Обработчик команды /start
@user_router.message(CommandStart())
async def cmd_start(message: Message, session_with_commit: AsyncSession):
    # Получение ID пользователя
    user_id = message.from_user.id
    # Проверка наличия пользователя в базе данных
    user_info = await UserDAO.find_one_or_none(
        session=session_with_commit,
        filters=TelegramIDModel(telegram_id=user_id)
    )
    # Если пользователь найден, приветствуем его
    if user_info:
        return await message.answer(
            f"👋 Привет, {message.from_user.full_name}! Выберите необходимое действие",
            reply_markup=main_user_kb(user_id)
        )
    # Если пользователя нет, регистрируем его
    values = UserModel(
        telegram_id=user_id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )
    await UserDAO.add(session=session_with_commit, values=values)
    # После регистрации приветствуем пользователя
    await message.answer(f"🎉 <b>Благодарим за регистрацию!</b>. Теперь выберите необходимое действие.",
                         reply_markup=main_user_kb(user_id))

# Обработчик кнопки "Главная страница"
@user_router.callback_query(F.data == "home")
async def page_home(call: CallbackQuery):
    await call.answer("Главная страница")
    return await call.message.answer(
        f"👋 Привет, {call.from_user.full_name}! Выберите необходимое действие",
        reply_markup=main_user_kb(call.from_user.id)
    )

# Обработчик кнопки "О магазине"
@user_router.callback_query(F.data == "about")
async def page_about(call: CallbackQuery):
    await call.answer("О магазине")
    await call.message.answer(
        text=(
            "🎓 Добро пожаловать в наш учебный магазин!\\n\\n"
            "🚀 Этот бот создан как демонстрационный проект для статьи на Хабре.\\n\\n"
            "👨\u200d💻 Автор: Яковенко Алексей\\n\\n"
            "🛍️ Здесь вы можете изучить принципы работы телеграм-магазина, "
            "ознакомиться с функциональностью и механизмами взаимодействия с пользователем.\\n\\n"
            "📚 Этот проект - это отличный способ погрузиться в мир разработки ботов "
            "и электронной коммерции в Telegram.\\n\\n"
            "💡 Исследуйте, учитесь и вдохновляйтесь!\\n\\n"
            "Данные для тестовой оплаты:\\n\\n"
            "Карта: 1111 1111 1111 1026\\n"
            "Годен до: 12/26\\n"
            "CVC-код: 000\\n"
        ),
        reply_markup=call.message.reply_markup
    )

# Обработчик кнопки "Профиль"
@user_router.callback_query(F.data == "my_profile")
async def page_about(call: CallbackQuery, session_without_commit: AsyncSession):
    await call.answer("Профиль")

    # Получаем статистику покупок пользователя
    purchases = await UserDAO.get_purchase_statistics(session=session_without_commit, telegram_id=call.from_user.id)
    total_amount = purchases.get("total_amount", 0)
    total_purchases = purchases.get("total_purchases", 0)

    # Формируем сообщение в зависимости от наличия покупок
    if total_purchases == 0:
        await call.message.answer(
            text="🔍 <b>У вас пока нет покупок.</b>\\n\\n"
                 "Откройте каталог и выберите что-нибудь интересное!",
            reply_markup=main_user_kb(call.from_user.id)
        )
    else:
        text = (
            f"🛍 <b>Ваш профиль:</b>\\n\\n"
            f"Количество покупок: <b>{total_purchases}</b>\\n"
            f"Общая сумма: <b>{total_amount}₽</b>\\n\\n"
            "Хотите просмотреть детали ваших покупок?"
        )
        await call.message.answer(
            text=text,
            reply_markup=purchases_kb()
        )

# Обработчик кнопки "Мои покупки"
@user_router.callback_query(F.data == "purchases")
async def page_user_purchases(call: CallbackQuery, session_without_commit: AsyncSession):
    await call.answer("Мои покупки")
    try:
        await call.message.delete()
    except Exception as e:
        pass
    # Получаем список покупок пользователя
    purchases = await UserDAO.get_purchased_products(session=session_without_commit, telegram_id=call.from_user.id)

    if not purchases:
        await call.message.answer(
            text=f"🔍 <b>У вас пока нет покупок.</b>\\n\\n"
                 f"Откройте каталог и выберите что-нибудь интересное!",
            reply_markup=main_user_kb(call.from_user.id)
        )
        return

    # Для каждой покупки отправляем информацию
    for purchase in purchases:
        product = purchase.product
        file_text = "📦 <b>Товар включает файл:</b>" if product.file_id else "📄 <b>Товар не включает файлы:</b>"

        product_text = (
            f"🛒 <b>Информация о вашем товаре:</b>\\n"
            f"━━━━━━━━━━━━━━━━━━\\n"
            f"🔹 <b>Название:</b> <i>{product.name}</i>\\n"
            f"🔹 <b>Описание:</b>\\n<i>{product.description}</i>\\n"
            f"🔹 <b>Цена:</b> <b>{product.price} ₽</b>\\n"
            f"🔹 <b>Закрытое описание:</b>\\n<i>{product.hidden_content}</i>\\n"
            f"━━━━━━━━━━━━━━━━━━\\n"
            f"{file_text}\\n"
        )

        if product.file_id:
            # Отправляем файл с текстом
            await call.message.answer_document(
                document=product.file_id,
                caption=product_text,
            )
        else:
            # Отправляем только текст
            await call.message.answer(
                text=product_text,
            )

    await call.message.answer(
        text="🙏 Спасибо за доверие!",
        reply_markup=main_user_kb(call.from_user.id)
    )
```