### Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код определяет набор функций для создания встроенных клавиатур (InlineKeyboardMarkup) для Telegram-ботов с использованием библиотеки `aiogram`. Каждая функция создает клавиатуру для определенных действий администратора, таких как управление каталогом, отправка файлов, просмотр статистики, управление товарами и подтверждение действий.

Шаги выполнения
-------------------------
1. **Импорт необходимых модулей**:
   - Импортируются классы `List` из модуля `typing`, `InlineKeyboardMarkup` из `aiogram.types`, `InlineKeyboardBuilder` из `aiogram.utils.keyboard` и `Category` из `bot.dao.models`.

2. **Функция `catalog_admin_kb`**:
   - Функция `catalog_admin_kb` принимает список объектов `Category` в качестве аргумента.
   - Создает объект `InlineKeyboardBuilder`.
   - Итерируется по списку категорий и добавляет кнопку для каждой категории с текстом `category.category_name` и callback_data в формате `add_category_{category.id}`.
   - Добавляет кнопку "Отмена" с `callback_data="admin_panel"`.
   - Вызывает метод `adjust(2)` для автоматического размещения кнопок в два столбца.
   - Возвращает объект `InlineKeyboardMarkup`, созданный на основе `InlineKeyboardBuilder`.

3. **Функция `admin_send_file_kb`**:
   - Функция `admin_send_file_kb` не принимает аргументов.
   - Создает объект `InlineKeyboardBuilder`.
   - Добавляет кнопку "Без файла" с `callback_data="without_file"`.
   - Добавляет кнопку "Отмена" с `callback_data="admin_panel"`.
   - Вызывает метод `adjust(2)` для автоматического размещения кнопок в два столбца.
   - Возвращает объект `InlineKeyboardMarkup`.

4. **Функция `admin_kb`**:
   - Функция `admin_kb` не принимает аргументов.
   - Создает объект `InlineKeyboardBuilder`.
   - Добавляет кнопки "📊 Статистика", "🛍️ Управлять товарами" и "🏠 На главную" с соответствующими `callback_data`.
   - Вызывает метод `adjust(2)` для автоматического размещения кнопок в два столбца.
   - Возвращает объект `InlineKeyboardMarkup`.

5. **Функция `admin_kb_back`**:
   - Функция `admin_kb_back` не принимает аргументов.
   - Создает объект `InlineKeyboardBuilder`.
   - Добавляет кнопки "⚙️ Админ панель" и "🏠 На главную" с соответствующими `callback_data`.
   - Вызывает метод `adjust(1)` для размещения кнопок в один столбец.
   - Возвращает объект `InlineKeyboardMarkup`.

6. **Функция `dell_product_kb`**:
   - Функция `dell_product_kb` принимает `product_id` (int) в качестве аргумента.
   - Создает объект `InlineKeyboardBuilder`.
   - Добавляет кнопки "🗑️ Удалить", "⚙️ Админ панель" и "🏠 На главную" с соответствующими `callback_data`, включая `product_id` для кнопки удаления.
   - Вызывает метод `adjust(2, 2, 1)` для размещения кнопок в три ряда: 2, 2 и 1 кнопка.
   - Возвращает объект `InlineKeyboardMarkup`.

7. **Функция `product_management_kb`**:
   - Функция `product_management_kb` не принимает аргументов.
   - Создает объект `InlineKeyboardBuilder`.
   - Добавляет кнопки "➕ Добавить товар", "🗑️ Удалить товар", "⚙️ Админ панель" и "🏠 На главную" с соответствующими `callback_data`.
   - Вызывает метод `adjust(2, 2, 1)` для размещения кнопок в три ряда: 2, 2 и 1 кнопка.
   - Возвращает объект `InlineKeyboardMarkup`.

8. **Функция `cancel_kb_inline`**:
   - Функция `cancel_kb_inline` не принимает аргументов.
   - Создает объект `InlineKeyboardBuilder`.
   - Добавляет кнопку "Отмена" с `callback_data="cancel"`.
   - Возвращает объект `InlineKeyboardMarkup`.

9. **Функция `admin_confirm_kb`**:
   - Функция `admin_confirm_kb` не принимает аргументов.
   - Создает объект `InlineKeyboardBuilder`.
   - Добавляет кнопки "Все верно" и "Отмена" с соответствующими `callback_data`.
   - Вызывает метод `adjust(1)` для размещения кнопок в один столбец.
   - Возвращает объект `InlineKeyboardMarkup`.

Пример использования
-------------------------

```python
    from aiogram import Bot
    from aiogram.types import Message
    from bot.dao.models import Category

    # Пример использования функции catalog_admin_kb
    async def send_catalog_keyboard(message: Message, bot: Bot, catalog_data: List[Category]):
        keyboard = catalog_admin_kb(catalog_data)
        await bot.send_message(message.chat.id, "Выберите категорию:", reply_markup=keyboard)

    # Пример использования функции admin_kb
    async def send_admin_keyboard(message: Message, bot: Bot):
        keyboard = admin_kb()
        await bot.send_message(message.chat.id, "Панель администратора:", reply_markup=keyboard)