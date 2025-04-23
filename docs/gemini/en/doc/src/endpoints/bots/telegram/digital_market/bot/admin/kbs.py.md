# Модуль kbs.py

## Обзор

Модуль `kbs.py` предназначен для создания различных инлайн-клавиатур для Telegram-бота, используемых в административной панели. Он содержит функции для генерации клавиатур для управления каталогом, отправки файлов, администрирования, подтверждения действий и т.д. Клавиатуры создаются с использованием `InlineKeyboardBuilder` из библиотеки `aiogram`.

## Подробнее

Модуль предоставляет набор функций для создания инлайн-клавиатур, которые используются для взаимодействия администратора с ботом. Каждая функция создает определенную клавиатуру с заданным набором кнопок и callback-data, которые обрабатываются ботом для выполнения соответствующих действий.

## Функции

### `catalog_admin_kb`

```python
def catalog_admin_kb(catalog_data: List[Category]) -> InlineKeyboardMarkup:
    """Создает инлайн-клавиатуру для управления категориями каталога в административной панели.

    Args:
        catalog_data (List[Category]): Список объектов `Category`, для которых нужно создать кнопки.

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры.
    """
```

**Назначение**:
Функция создает инлайн-клавиатуру для администратора, отображающую список категорий каталога. Каждая категория представлена кнопкой, при нажатии на которую происходит добавление категории.

**Параметры**:
- `catalog_data` (List[Category]): Список объектов `Category`, содержащих информацию о категориях.

**Возвращаемое значение**:
- `InlineKeyboardMarkup`: Объект инлайн-клавиатуры, готовый для отправки пользователю.

**Как работает**:
1. Создается экземпляр `InlineKeyboardBuilder`.
2. Для каждой категории из списка `catalog_data` добавляется кнопка с названием категории и callback_data, содержащим id категории.
3. Добавляется кнопка "Отмена" с callback_data "admin_panel".
4. Клавиатура формируется с расположением кнопок в 2 столбца.
5. Возвращается объект `InlineKeyboardMarkup`.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup
from bot.dao.models import Category
from typing import List

# Пример данных о категориях
catalog_data: List[Category] = [
    Category(id=1, category_name="Электроника"),
    Category(id=2, category_name="Одежда"),
    Category(id=3, category_name="Обувь")
]

# Создание клавиатуры
keyboard: InlineKeyboardMarkup = catalog_admin_kb(catalog_data)

# Вывод клавиатуры (в реальном коде отправляется ботом)
print(keyboard)
```

### `admin_send_file_kb`

```python
def admin_send_file_kb() -> InlineKeyboardMarkup:
    """Создает инлайн-клавиатуру для выбора отправки файла в административной панели.

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры.
    """
```

**Назначение**:
Функция создает инлайн-клавиатуру с кнопками для выбора отправки файла или отказа от нее.

**Возвращаемое значение**:
- `InlineKeyboardMarkup`: Объект инлайн-клавиатуры.

**Как работает**:
1. Создается экземпляр `InlineKeyboardBuilder`.
2. Добавляется кнопка "Без файла" с callback_data "without_file".
3. Добавляется кнопка "Отмена" с callback_data "admin_panel".
4. Клавиатура формируется с расположением кнопок в 2 столбца.
5. Возвращается объект `InlineKeyboardMarkup`.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Создание клавиатуры
keyboard: InlineKeyboardMarkup = admin_send_file_kb()

# Вывод клавиатуры (в реальном коде отправляется ботом)
print(keyboard)
```

### `admin_kb`

```python
def admin_kb() -> InlineKeyboardMarkup:
    """Создает основную инлайн-клавиатуру административной панели.

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры.
    """
```

**Назначение**:
Функция создает основную инлайн-клавиатуру для административной панели с кнопками для статистики, управления товарами и возврата на главную страницу.

**Возвращаемое значение**:
- `InlineKeyboardMarkup`: Объект инлайн-клавиатуры.

**Как работает**:
1. Создается экземпляр `InlineKeyboardBuilder`.
2. Добавляется кнопка "📊 Статистика" с callback_data "statistic".
3. Добавляется кнопка "🛍️ Управлять товарами" с callback_data "process_products".
4. Добавляется кнопка "🏠 На главную" с callback_data "home".
5. Клавиатура формируется с расположением кнопок в 2 столбца.
6. Возвращается объект `InlineKeyboardMarkup`.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Создание клавиатуры
keyboard: InlineKeyboardMarkup = admin_kb()

# Вывод клавиатуры (в реальном коде отправляется ботом)
print(keyboard)
```

### `admin_kb_back`

```python
def admin_kb_back() -> InlineKeyboardMarkup:
    """Создает инлайн-клавиатуру с кнопками для возврата в административную панель и на главную страницу.

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры.
    """
```

**Назначение**:
Функция создает инлайн-клавиатуру с кнопками для возврата в административную панель и на главную страницу.

**Возвращаемое значение**:
- `InlineKeyboardMarkup`: Объект инлайн-клавиатуры.

**Как работает**:
1. Создается экземпляр `InlineKeyboardBuilder`.
2. Добавляется кнопка "⚙️ Админ панель" с callback_data "admin_panel".
3. Добавляется кнопка "🏠 На главную" с callback_data "home".
4. Клавиатура формируется с расположением кнопок в 1 столбец.
5. Возвращается объект `InlineKeyboardMarkup`.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Создание клавиатуры
keyboard: InlineKeyboardMarkup = admin_kb_back()

# Вывод клавиатуры (в реальном коде отправляется ботом)
print(keyboard)
```

### `dell_product_kb`

```python
def dell_product_kb(product_id: int) -> InlineKeyboardMarkup:
    """Создает инлайн-клавиатуру для подтверждения удаления товара.

    Args:
        product_id (int): ID товара, который нужно удалить.

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры.
    """
```

**Назначение**:
Функция создает инлайн-клавиатуру для подтверждения удаления товара с кнопками "Удалить", "Админ панель" и "На главную".

**Параметры**:
- `product_id` (int): ID товара, который нужно удалить.

**Возвращаемое значение**:
- `InlineKeyboardMarkup`: Объект инлайн-клавиатуры.

**Как работает**:
1. Создается экземпляр `InlineKeyboardBuilder`.
2. Добавляется кнопка "🗑️ Удалить" с callback_data, содержащим id товара для удаления.
3. Добавляется кнопка "⚙️ Админ панель" с callback_data "admin_panel".
4. Добавляется кнопка "🏠 На главную" с callback_data "home".
5. Кнопки размещаются в три ряда: 2, 2 и 1 кнопка.
6. Возвращается объект `InlineKeyboardMarkup`.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# ID товара для удаления
product_id: int = 123

# Создание клавиатуры
keyboard: InlineKeyboardMarkup = dell_product_kb(product_id)

# Вывод клавиатуры (в реальном коде отправляется ботом)
print(keyboard)
```

### `product_management_kb`

```python
def product_management_kb() -> InlineKeyboardMarkup:
    """Создает инлайн-клавиатуру для управления товарами (добавление, удаление).

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры.
    """
```

**Назначение**:
Функция создает инлайн-клавиатуру для управления товарами с кнопками "Добавить товар", "Удалить товар", "Админ панель" и "На главную".

**Возвращаемое значение**:
- `InlineKeyboardMarkup`: Объект инлайн-клавиатуры.

**Как работает**:
1. Создается экземпляр `InlineKeyboardBuilder`.
2. Добавляется кнопка "➕ Добавить товар" с callback_data "add_product".
3. Добавляется кнопка "🗑️ Удалить товар" с callback_data "delete_product".
4. Добавляется кнопка "⚙️ Админ панель" с callback_data "admin_panel".
5. Добавляется кнопка "🏠 На главную" с callback_data "home".
6. Кнопки размещаются в три ряда: 2, 2 и 1 кнопка.
7. Возвращается объект `InlineKeyboardMarkup`.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Создание клавиатуры
keyboard: InlineKeyboardMarkup = product_management_kb()

# Вывод клавиатуры (в реальном коде отправляется ботом)
print(keyboard)
```

### `cancel_kb_inline`

```python
def cancel_kb_inline() -> InlineKeyboardMarkup:
    """Создает инлайн-клавиатуру с кнопкой "Отмена".

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры.
    """
```

**Назначение**:
Функция создает инлайн-клавиатуру с кнопкой "Отмена".

**Возвращаемое значение**:
- `InlineKeyboardMarkup`: Объект инлайн-клавиатуры.

**Как работает**:
1. Создается экземпляр `InlineKeyboardBuilder`.
2. Добавляется кнопка "Отмена" с callback_data "cancel".
3. Возвращается объект `InlineKeyboardMarkup`.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Создание клавиатуры
keyboard: InlineKeyboardMarkup = cancel_kb_inline()

# Вывод клавиатуры (в реальном коде отправляется ботом)
print(keyboard)
```

### `admin_confirm_kb`

```python
def admin_confirm_kb() -> InlineKeyboardMarkup:
    """Создает инлайн-клавиатуру для подтверждения действия администратором.

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры.
    """
```

**Назначение**:
Функция создает инлайн-клавиатуру для подтверждения действия администратором с кнопками "Все верно" и "Отмена".

**Возвращаемое значение**:
- `InlineKeyboardMarkup`: Объект инлайн-клавиатуры.

**Как работает**:
1. Создается экземпляр `InlineKeyboardBuilder`.
2. Добавляется кнопка "Все верно" с callback_data "confirm_add".
3. Добавляется кнопка "Отмена" с callback_data "admin_panel".
4. Клавиатура формируется с расположением кнопок в 1 столбец.
5. Возвращается объект `InlineKeyboardMarkup`.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup

# Создание клавиатуры
keyboard: InlineKeyboardMarkup = admin_confirm_kb()

# Вывод клавиатуры (в реальном коде отправляется ботом)
print(keyboard)
```