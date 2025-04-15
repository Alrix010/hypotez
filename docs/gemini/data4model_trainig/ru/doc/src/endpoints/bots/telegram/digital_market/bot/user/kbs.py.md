# Модуль для создания клавиатур для Telegram бота
=================================================

Модуль содержит функции для создания различных типов клавиатур (InlineKeyboardMarkup, ReplyKeyboardMarkup) для Telegram бота, использующего библиотеку aiogram.
Клавиатуры используются для навигации по боту, отображения каталога товаров, совершения покупок и т.д.

## Обзор

Модуль предоставляет набор функций для создания интерактивных клавиатур в Telegram-боте. Клавиатуры формируются с использованием библиотеки `aiogram` и содержат кнопки для навигации, отображения каталога, совершения покупок и других действий. Функции используют данные о категориях товаров, ценах и идентификаторах продуктов для генерации динамических клавиатур.

## Подробней

Этот модуль является важной частью Telegram-бота, поскольку он определяет интерфейс взаимодействия пользователя с ботом. Клавиатуры, создаваемые функциями этого модуля, позволяют пользователям перемещаться по боту, просматривать товары, совершать покупки и получать информацию.
Модуль использует `aiogram` для создания клавиатур и `bot.config.settings` для получения информации об администраторах бота.

## Функции

### `main_user_kb`

```python
def main_user_kb(user_id: int) -> InlineKeyboardMarkup:
    """
    Создает главную клавиатуру пользователя с кнопками навигации.

    Args:
        user_id (int): ID пользователя для проверки, является ли он администратором.

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup с кнопками "Мои покупки", "Каталог", "О магазине", "Поддержать автора" и (если пользователь - администратор) "Админ панель".

    Примеры:
        >>> from aiogram.types import InlineKeyboardMarkup
        >>> kb: InlineKeyboardMarkup = main_user_kb(12345)
        >>> assert isinstance(kb, InlineKeyboardMarkup)
    """
```

**Назначение**: Создает главную клавиатуру пользователя с кнопками навигации.

**Параметры**:
- `user_id` (int): ID пользователя для проверки, является ли он администратором.

**Возвращает**:
- `InlineKeyboardMarkup`: Объект InlineKeyboardMarkup с кнопками "Мои покупки", "Каталог", "О магазине", "Поддержать автора" и (если пользователь - администратор) "Админ панель".

**Как работает функция**:
- Создается объект `InlineKeyboardBuilder`.
- Добавляются кнопки: "👤 Мои покупки", "🛍 Каталог", "ℹ️ О магазине", "🌟 Поддержать автора".
- Если `user_id` есть в списке `settings.ADMIN_IDS`, добавляется кнопка "⚙️ Админ панель".
- Кнопки выравниваются в один столбец.
- Клавиатура преобразуется в объект `InlineKeyboardMarkup` и возвращается.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup
kb: InlineKeyboardMarkup = main_user_kb(12345)
assert isinstance(kb, InlineKeyboardMarkup)
```

### `catalog_kb`

```python
def catalog_kb(catalog_data: List[Category]) -> InlineKeyboardMarkup:
    """
    Создает клавиатуру каталога с кнопками для каждой категории.

    Args:
        catalog_data (List[Category]): Список объектов Category, представляющих категории товаров.

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup с кнопками для каждой категории и кнопкой "🏠 На главную".

    Примеры:
        >>> from aiogram.types import InlineKeyboardMarkup
        >>> from bot.dao.models import Category
        >>> categories = [Category(id=1, category_name='Category 1'), Category(id=2, category_name='Category 2')]
        >>> kb: InlineKeyboardMarkup = catalog_kb(categories)
        >>> assert isinstance(kb, InlineKeyboardMarkup)
    """
```

**Назначение**: Создает клавиатуру каталога с кнопками для каждой категории.

**Параметры**:
- `catalog_data` (List[Category]): Список объектов `Category`, представляющих категории товаров.

**Возвращает**:
- `InlineKeyboardMarkup`: Объект `InlineKeyboardMarkup` с кнопками для каждой категории и кнопкой "🏠 На главную".

**Как работает функция**:
- Создается объект `InlineKeyboardBuilder`.
- Для каждой категории в `catalog_data` добавляется кнопка с названием категории и `callback_data` в формате `category_{category.id}`.
- Добавляется кнопка "🏠 На главную" с `callback_data` "home".
- Кнопки выравниваются в два столбца.
- Клавиатура преобразуется в объект `InlineKeyboardMarkup` и возвращается.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup
from bot.dao.models import Category
categories = [Category(id=1, category_name='Category 1'), Category(id=2, category_name='Category 2')]
kb: InlineKeyboardMarkup = catalog_kb(categories)
assert isinstance(kb, InlineKeyboardMarkup)
```

### `purchases_kb`

```python
def purchases_kb() -> InlineKeyboardMarkup:
    """
    Создает клавиатуру для просмотра покупок с кнопками "Смотреть покупки" и "На главную".

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup с кнопками "🗑 Смотреть покупки" и "🏠 На главную".

    Примеры:
        >>> from aiogram.types import InlineKeyboardMarkup
        >>> kb: InlineKeyboardMarkup = purchases_kb()
        >>> assert isinstance(kb, InlineKeyboardMarkup)
    """
```

**Назначение**: Создает клавиатуру для просмотра покупок с кнопками "Смотреть покупки" и "На главную".

**Параметры**:
- Нет.

**Возвращает**:
- `InlineKeyboardMarkup`: Объект `InlineKeyboardMarkup` с кнопками "🗑 Смотреть покупки" и "🏠 На главную".

**Как работает функция**:
- Создается объект `InlineKeyboardBuilder`.
- Добавляются кнопки: "🗑 Смотреть покупки" и "🏠 На главную".
- Кнопки выравниваются в один столбец.
- Клавиатура преобразуется в объект `InlineKeyboardMarkup` и возвращается.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup
kb: InlineKeyboardMarkup = purchases_kb()
assert isinstance(kb, InlineKeyboardMarkup)
```

### `product_kb`

```python
def product_kb(product_id, price, stars_price) -> InlineKeyboardMarkup:
    """
    Создает клавиатуру продукта с кнопками для оплаты различными способами и кнопками "Назад" и "На главную".

    Args:
        product_id: ID продукта.
        price: Цена продукта в рублях.
        stars_price: Цена продукта в звездах.

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup с кнопками для оплаты через ЮКасса, Robocassa, звездами, а также кнопками "🛍 Назад" и "🏠 На главную".

    Примеры:
        >>> from aiogram.types import InlineKeyboardMarkup
        >>> kb: InlineKeyboardMarkup = product_kb(1, 100, 50)
        >>> assert isinstance(kb, InlineKeyboardMarkup)
    """
```

**Назначение**: Создает клавиатуру продукта с кнопками для оплаты различными способами и кнопками "Назад" и "На главную".

**Параметры**:
- `product_id`: ID продукта.
- `price`: Цена продукта в рублях.
- `stars_price`: Цена продукта в звездах.

**Возвращает**:
- `InlineKeyboardMarkup`: Объект `InlineKeyboardMarkup` с кнопками для оплаты через ЮКасса, Robocassa, звездами, а также кнопками "🛍 Назад" и "🏠 На главную".

**Как работает функция**:
- Создается объект `InlineKeyboardBuilder`.
- Добавляются кнопки для оплаты через ЮКасса, Robocassa и звездами с соответствующими callback_data.
- Добавляются кнопки "🛍 Назад" и "🏠 На главную".
- Кнопки выравниваются в два столбца.
- Клавиатура преобразуется в объект `InlineKeyboardMarkup` и возвращается.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup
kb: InlineKeyboardMarkup = product_kb(1, 100, 50)
assert isinstance(kb, InlineKeyboardMarkup)
```

### `get_product_buy_youkassa`

```python
def get_product_buy_youkassa(price) -> InlineKeyboardMarkup:
    """
    Создает клавиатуру для оплаты продукта через ЮКасса.

    Args:
        price: Цена продукта.

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup с кнопкой для оплаты через ЮКасса и кнопкой "Отменить".

    Примеры:
        >>> from aiogram.types import InlineKeyboardMarkup
        >>> kb: InlineKeyboardMarkup = get_product_buy_youkassa(100)
        >>> assert isinstance(kb, InlineKeyboardMarkup)
    """
```

**Назначение**: Создает клавиатуру для оплаты продукта через ЮКасса.

**Параметры**:
- `price`: Цена продукта.

**Возвращает**:
- `InlineKeyboardMarkup`: Объект `InlineKeyboardMarkup` с кнопкой для оплаты через ЮКасса и кнопкой "Отменить".

**Как работает функция**:
- Создается объект `InlineKeyboardMarkup`.
- Добавляется кнопка для оплаты через ЮКасса с указанием цены.
- Добавляется кнопка "Отменить" с `callback_data` "home".
- Клавиатура возвращается.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup
kb: InlineKeyboardMarkup = get_product_buy_youkassa(100)
assert isinstance(kb, InlineKeyboardMarkup)
```

### `get_product_buy_robocassa`

```python
def get_product_buy_robocassa(price: int, payment_link: str) -> InlineKeyboardMarkup:
    """
    Создает клавиатуру для оплаты продукта через Robocassa с использованием web_app.

    Args:
        price (int): Цена продукта.
        payment_link (str): Ссылка на оплату через Robocassa.

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup с кнопкой для оплаты через Robocassa и кнопкой "Отменить".

    Примеры:
        >>> from aiogram.types import InlineKeyboardMarkup
        >>> kb: InlineKeyboardMarkup = get_product_buy_robocassa(100, "https://example.com/robocassa_payment")
        >>> assert isinstance(kb, InlineKeyboardMarkup)
    """
```

**Назначение**: Создает клавиатуру для оплаты продукта через Robocassa с использованием `web_app`.

**Параметры**:
- `price` (int): Цена продукта.
- `payment_link` (str): Ссылка на оплату через Robocassa.

**Возвращает**:
- `InlineKeyboardMarkup`: Объект `InlineKeyboardMarkup` с кнопкой для оплаты через Robocassa и кнопкой "Отменить".

**Как работает функция**:
- Создается объект `InlineKeyboardMarkup`.
- Добавляется кнопка для оплаты через Robocassa, использующая `web_app` для перенаправления пользователя на страницу оплаты.
- Добавляется кнопка "Отменить" с `callback_data` "home".
- Клавиатура возвращается.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup
kb: InlineKeyboardMarkup = get_product_buy_robocassa(100, "https://example.com/robocassa_payment")
assert isinstance(kb, InlineKeyboardMarkup)
```

### `get_product_buy_stars`

```python
def get_product_buy_stars(price) -> InlineKeyboardMarkup:
    """
    Создает клавиатуру для оплаты продукта звездами.

    Args:
        price: Цена продукта в звездах.

    Returns:
        InlineKeyboardMarkup: Объект InlineKeyboardMarkup с кнопкой для оплаты звездами и кнопкой "Отменить".

    Примеры:
        >>> from aiogram.types import InlineKeyboardMarkup
        >>> kb: InlineKeyboardMarkup = get_product_buy_stars(50)
        >>> assert isinstance(kb, InlineKeyboardMarkup)
    """
```

**Назначение**: Создает клавиатуру для оплаты продукта звездами.

**Параметры**:
- `price`: Цена продукта в звездах.

**Возвращает**:
- `InlineKeyboardMarkup`: Объект `InlineKeyboardMarkup` с кнопкой для оплаты звездами и кнопкой "Отменить".

**Как работает функция**:
- Создается объект `InlineKeyboardMarkup`.
- Добавляется кнопка для оплаты звездами с указанием цены.
- Добавляется кнопка "Отменить" с `callback_data` "home".
- Клавиатура возвращается.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup
kb: InlineKeyboardMarkup = get_product_buy_stars(50)
assert isinstance(kb, InlineKeyboardMarkup)