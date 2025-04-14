# Модуль для формирования клавиатур администратора Telegram-бота

## Обзор

Модуль содержит функции для создания различных встроенных клавиатур (InlineKeyboardMarkup) для административной панели Telegram-бота. Клавиатуры используются для навигации, управления товарами, статистикой и выполнения других административных действий.

## Подробней

Этот модуль предоставляет набор функций для создания интерактивных клавиатур, которые позволяют администраторам управлять ботом. Каждая функция генерирует клавиатуру с определенным набором кнопок, которые выполняют различные действия при нажатии. Используются библиотеки `aiogram` для создания и управления клавиатурами.

## Функции

### `catalog_admin_kb`

**Назначение**: Создает встроенную клавиатуру для администратора с категориями каталога.

**Параметры**:

- `catalog_data` (List[Category]): Список объектов `Category`, для которых нужно создать кнопки.

**Возвращает**:

- `InlineKeyboardMarkup`: Объект встроенной клавиатуры с кнопками для каждой категории и кнопкой "Отмена".

**Как работает функция**:

- Создает экземпляр `InlineKeyboardBuilder`.
- Проходит по списку категорий `catalog_data`.
- Для каждой категории добавляет кнопку с названием категории и callback_data, содержащим ID категории.
- Добавляет кнопку "Отмена" с callback_data "admin_panel".
- Устанавливает расположение кнопок в два столбца.
- Возвращает клавиатуру в виде объекта `InlineKeyboardMarkup`.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup
from bot.dao.models import Category
from typing import List

# Пример данных категорий
categories: List[Category] = [
    Category(id=1, category_name="Электроника"),
    Category(id=2, category_name="Одежда"),
    Category(id=3, category_name="Обувь"),
]

# Создание клавиатуры
keyboard: InlineKeyboardMarkup = catalog_admin_kb(categories)
```

### `admin_send_file_kb`

**Назначение**: Создает встроенную клавиатуру для администратора с кнопками "Без файла" и "Отмена".

**Возвращает**:

- `InlineKeyboardMarkup`: Объект встроенной клавиатуры с кнопками "Без файла" и "Отмена".

**Как работает функция**:

- Создает экземпляр `InlineKeyboardBuilder`.
- Добавляет кнопку "Без файла" с callback_data "without_file".
- Добавляет кнопку "Отмена" с callback_data "admin_panel".
- Устанавливает расположение кнопок в два столбца.
- Возвращает клавиатуру в виде объекта `InlineKeyboardMarkup`.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Создание клавиатуры
keyboard: InlineKeyboardMarkup = admin_send_file_kb()
```

### `admin_kb`

**Назначение**: Создает основную встроенную клавиатуру для администратора с кнопками "📊 Статистика", "🛍️ Управлять товарами" и "🏠 На главную".

**Возвращает**:

- `InlineKeyboardMarkup`: Объект встроенной клавиатуры с кнопками для статистики, управления товарами и возврата на главную.

**Как работает функция**:

- Создает экземпляр `InlineKeyboardBuilder`.
- Добавляет кнопку "📊 Статистика" с callback_data "statistic".
- Добавляет кнопку "🛍️ Управлять товарами" с callback_data "process_products".
- Добавляет кнопку "🏠 На главную" с callback_data "home".
- Устанавливает расположение кнопок в два столбца.
- Возвращает клавиатуру в виде объекта `InlineKeyboardMarkup`.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Создание клавиатуры
keyboard: InlineKeyboardMarkup = admin_kb()
```

### `admin_kb_back`

**Назначение**: Создает встроенную клавиатуру для возврата в админ-панель и на главную страницу.

**Возвращает**:

- `InlineKeyboardMarkup`: Объект встроенной клавиатуры с кнопками "⚙️ Админ панель" и "🏠 На главную".

**Как работает функция**:

- Создает экземпляр `InlineKeyboardBuilder`.
- Добавляет кнопку "⚙️ Админ панель" с callback_data "admin_panel".
- Добавляет кнопку "🏠 На главную" с callback_data "home".
- Устанавливает расположение кнопок в один столбец.
- Возвращает клавиатуру в виде объекта `InlineKeyboardMarkup`.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Создание клавиатуры
keyboard: InlineKeyboardMarkup = admin_kb_back()
```

### `dell_product_kb`

**Назначение**: Создает встроенную клавиатуру для подтверждения удаления товара с кнопками "🗑️ Удалить", "⚙️ Админ панель" и "🏠 На главную".

**Параметры**:

- `product_id` (int): ID товара, который нужно удалить.

**Возвращает**:

- `InlineKeyboardMarkup`: Объект встроенной клавиатуры с кнопками для удаления товара, возврата в админ-панель и на главную.

**Как работает функция**:

- Создает экземпляр `InlineKeyboardBuilder`.
- Добавляет кнопку "🗑️ Удалить" с callback_data, содержащим ID товара.
- Добавляет кнопку "⚙️ Админ панель" с callback_data "admin_panel".
- Добавляет кнопку "🏠 На главную" с callback_data "home".
- Устанавливает расположение кнопок в три ряда: 2, 2 и 1 кнопка.
- Возвращает клавиатуру в виде объекта `InlineKeyboardMarkup`.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# ID товара для удаления
product_id: int = 123

# Создание клавиатуры
keyboard: InlineKeyboardMarkup = dell_product_kb(product_id)
```

### `product_management_kb`

**Назначение**: Создает встроенную клавиатуру для управления товарами с кнопками "➕ Добавить товар", "🗑️ Удалить товар", "⚙️ Админ панель" и "🏠 На главную".

**Возвращает**:

- `InlineKeyboardMarkup`: Объект встроенной клавиатуры с кнопками для добавления, удаления товаров, возврата в админ-панель и на главную.

**Как работает функция**:

- Создает экземпляр `InlineKeyboardBuilder`.
- Добавляет кнопку "➕ Добавить товар" с callback_data "add_product".
- Добавляет кнопку "🗑️ Удалить товар" с callback_data "delete_product".
- Добавляет кнопку "⚙️ Админ панель" с callback_data "admin_panel".
- Добавляет кнопку "🏠 На главную" с callback_data "home".
- Устанавливает расположение кнопок в три ряда: 2, 2 и 1 кнопка.
- Возвращает клавиатуру в виде объекта `InlineKeyboardMarkup`.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Создание клавиатуры
keyboard: InlineKeyboardMarkup = product_management_kb()
```

### `cancel_kb_inline`

**Назначение**: Создает встроенную клавиатуру с кнопкой "Отмена".

**Возвращает**:

- `InlineKeyboardMarkup`: Объект встроенной клавиатуры с кнопкой "Отмена".

**Как работает функция**:

- Создает экземпляр `InlineKeyboardBuilder`.
- Добавляет кнопку "Отмена" с callback_data "cancel".
- Возвращает клавиатуру в виде объекта `InlineKeyboardMarkup`.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Создание клавиатуры
keyboard: InlineKeyboardMarkup = cancel_kb_inline()
```

### `admin_confirm_kb`

**Назначение**: Создает встроенную клавиатуру для подтверждения действия администратором с кнопками "Все верно" и "Отмена".

**Возвращает**:

- `InlineKeyboardMarkup`: Объект встроенной клавиатуры с кнопками "Все верно" и "Отмена".

**Как работает функция**:

- Создает экземпляр `InlineKeyboardBuilder`.
- Добавляет кнопку "Все верно" с callback_data "confirm_add".
- Добавляет кнопку "Отмена" с callback_data "admin_panel".
- Устанавливает расположение кнопок в один столбец.
- Возвращает клавиатуру в виде объекта `InlineKeyboardMarkup`.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Создание клавиатуры
keyboard: InlineKeyboardMarkup = admin_confirm_kb()