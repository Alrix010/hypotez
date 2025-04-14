# Модуль для создания клавиатур администратора Telegram-бота

## Обзор

Модуль `kbs.py` предназначен для создания различных инлайн-клавиатур (InlineKeyboardMarkup) для административной панели Telegram-бота.
Он предоставляет функции для генерации клавиатур для управления каталогом, отправки файлов, администрирования, управления продуктами и подтверждения действий.

## Подробней

Этот модуль облегчает создание интерактивных элементов управления в Telegram-боте, позволяя администраторам удобно выполнять различные задачи, такие как добавление и удаление товаров, просмотр статистики и навигация по административной панели. Каждая функция в модуле возвращает объект `InlineKeyboardMarkup`, который может быть отправлен пользователю вместе с сообщением.

## Функции

### `catalog_admin_kb`

**Назначение**: Создает инлайн-клавиатуру для выбора категории товара администратором.

**Параметры**:

-   `catalog_data` (List[Category]): Список объектов `Category`, для которых нужно создать кнопки.

**Возвращает**:

-   `InlineKeyboardMarkup`: Инлайн-клавиатура с кнопками для каждой категории и кнопкой "Отмена".

**Как работает функция**:

1.  Инициализирует объект `InlineKeyboardBuilder`.
2.  Для каждой категории в `catalog_data` создает кнопку с названием категории и callback_data, содержащим ID категории.
3.  Добавляет кнопку "Отмена" с callback_data "admin_panel".
4.  Устанавливает размещение кнопок в два столбца.
5.  Преобразует `InlineKeyboardBuilder` в `InlineKeyboardMarkup` и возвращает его.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup
from bot.dao.models import Category

# Пример данных о категориях
categories = [
    Category(id=1, category_name="Электроника"),
    Category(id=2, category_name="Одежда"),
    Category(id=3, category_name="Обувь")
]

# Создание клавиатуры администратора каталога
keyboard: InlineKeyboardMarkup = catalog_admin_kb(categories)
print(keyboard)
```

### `admin_send_file_kb`

**Назначение**: Создает инлайн-клавиатуру для выбора отправки файла или отказа от нее администратором.

**Возвращает**:

-   `InlineKeyboardMarkup`: Инлайн-клавиатура с кнопками "Без файла" и "Отмена".

**Как работает функция**:

1.  Инициализирует объект `InlineKeyboardBuilder`.
2.  Создает кнопку "Без файла" с callback_data "without_file".
3.  Создает кнопку "Отмена" с callback_data "admin_panel".
4.  Устанавливает размещение кнопок в два столбца.
5.  Преобразует `InlineKeyboardBuilder` в `InlineKeyboardMarkup` и возвращает его.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Создание клавиатуры для отправки файла администратором
keyboard: InlineKeyboardMarkup = admin_send_file_kb()
print(keyboard)
```

### `admin_kb`

**Назначение**: Создает основную инлайн-клавиатуру администратора.

**Возвращает**:

-   `InlineKeyboardMarkup`: Инлайн-клавиатура с кнопками "📊 Статистика", "🛍️ Управлять товарами" и "🏠 На главную".

**Как работает функция**:

1.  Инициализирует объект `InlineKeyboardBuilder`.
2.  Создает кнопку "📊 Статистика" с callback_data "statistic".
3.  Создает кнопку "🛍️ Управлять товарами" с callback_data "process_products".
4.  Создает кнопку "🏠 На главную" с callback_data "home".
5.  Устанавливает размещение кнопок в два столбца.
6.  Преобразует `InlineKeyboardBuilder` в `InlineKeyboardMarkup` и возвращает его.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Создание основной клавиатуры администратора
keyboard: InlineKeyboardMarkup = admin_kb()
print(keyboard)
```

### `admin_kb_back`

**Назначение**: Создает инлайн-клавиатуру с кнопками "⚙️ Админ панель" и "🏠 На главную".

**Возвращает**:

-   `InlineKeyboardMarkup`: Инлайн-клавиатура с кнопками "⚙️ Админ панель" и "🏠 На главную".

**Как работает функция**:

1.  Инициализирует объект `InlineKeyboardBuilder`.
2.  Создает кнопку "⚙️ Админ панель" с callback_data "admin_panel".
3.  Создает кнопку "🏠 На главную" с callback_data "home".
4.  Устанавливает размещение кнопок в один столбец.
5.  Преобразует `InlineKeyboardBuilder` в `InlineKeyboardMarkup` и возвращает его.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Создание клавиатуры администратора с кнопками возврата
keyboard: InlineKeyboardMarkup = admin_kb_back()
print(keyboard)
```

### `dell_product_kb`

**Назначение**: Создает инлайн-клавиатуру для подтверждения удаления товара.

**Параметры**:

-   `product_id` (int): ID товара, который нужно удалить.

**Возвращает**:

-   `InlineKeyboardMarkup`: Инлайн-клавиатура с кнопками "🗑️ Удалить", "⚙️ Админ панель" и "🏠 На главную".

**Как работает функция**:

1.  Инициализирует объект `InlineKeyboardBuilder`.
2.  Создает кнопку "🗑️ Удалить" с callback_data, содержащим ID товара.
3.  Создает кнопку "⚙️ Админ панель" с callback_data "admin_panel".
4.  Создает кнопку "🏠 На главную" с callback_data "home".
5.  Устанавливает размещение кнопок в три ряда: 2, 2 и 1 кнопка.
6.  Преобразует `InlineKeyboardBuilder` в `InlineKeyboardMarkup` и возвращает его.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Создание клавиатуры для удаления товара
keyboard: InlineKeyboardMarkup = dell_product_kb(product_id=123)
print(keyboard)
```

### `product_management_kb`

**Назначение**: Создает инлайн-клавиатуру для управления товарами.

**Возвращает**:

-   `InlineKeyboardMarkup`: Инлайн-клавиатура с кнопками "➕ Добавить товар", "🗑️ Удалить товар", "⚙️ Админ панель" и "🏠 На главную".

**Как работает функция**:

1.  Инициализирует объект `InlineKeyboardBuilder`.
2.  Создает кнопку "➕ Добавить товар" с callback_data "add_product".
3.  Создает кнопку "🗑️ Удалить товар" с callback_data "delete_product".
4.  Создает кнопку "⚙️ Админ панель" с callback_data "admin_panel".
5.  Создает кнопку "🏠 На главную" с callback_data "home".
6.  Устанавливает размещение кнопок в три ряда: 2, 2 и 1 кнопка.
7.  Преобразует `InlineKeyboardBuilder` в `InlineKeyboardMarkup` и возвращает его.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Создание клавиатуры для управления товарами
keyboard: InlineKeyboardMarkup = product_management_kb()
print(keyboard)
```

### `cancel_kb_inline`

**Назначение**: Создает инлайн-клавиатуру с кнопкой "Отмена".

**Возвращает**:

-   `InlineKeyboardMarkup`: Инлайн-клавиатура с кнопкой "Отмена".

**Как работает функция**:

1.  Инициализирует объект `InlineKeyboardBuilder`.
2.  Создает кнопку "Отмена" с callback_data "cancel".
3.  Преобразует `InlineKeyboardBuilder` в `InlineKeyboardMarkup` и возвращает его.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Создание клавиатуры для отмены действия
keyboard: InlineKeyboardMarkup = cancel_kb_inline()
print(keyboard)
```

### `admin_confirm_kb`

**Назначение**: Создает инлайн-клавиатуру для подтверждения действия администратором.

**Возвращает**:

-   `InlineKeyboardMarkup`: Инлайн-клавиатура с кнопками "Все верно" и "Отмена".

**Как работает функция**:

1.  Инициализирует объект `InlineKeyboardBuilder`.
2.  Создает кнопку "Все верно" с callback_data "confirm_add".
3.  Создает кнопку "Отмена" с callback_data "admin_panel".
4.  Устанавливает размещение кнопок в один столбец.
5.  Преобразует `InlineKeyboardBuilder` в `InlineKeyboardMarkup` и возвращает его.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Создание клавиатуры для подтверждения действия администратором
keyboard: InlineKeyboardMarkup = admin_confirm_kb()
print(keyboard)