# Модуль kbs

## Обзор

Модуль `kbs.py` предназначен для создания и управления клавиатурами (инлайн и обычными) для Telegram-бота. Он содержит функции для генерации различных типов клавиатур, используемых для навигации, отображения каталога, управления покупками и осуществления платежей.

## Более детально

Модуль предоставляет набор функций, которые упрощают создание интерактивных клавиатур для Telegram-бота. Клавиатуры создаются с использованием библиотеки `aiogram` и включают в себя кнопки для навигации по каталогу, управления профилем пользователя, совершения покупок и взаимодействия с административной панелью. Кроме того, модуль содержит функции для генерации ссылок на оплату через различные платежные системы, такие как ЮКасса и Robocassa.

## Классы

В данном модуле классы отсутствуют.

## Функции

### `main_user_kb`

```python
def main_user_kb(user_id: int) -> InlineKeyboardMarkup:
    """ Функция создает главную клавиатуру пользователя.

    Args:
        user_id (int): ID пользователя.

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры.
    
    Как работает функция:
    - Создает инлайн-клавиатуру с кнопками "👤 Мои покупки", "🛍 Каталог", "ℹ️ О магазине" и "🌟 Поддержать автора 🌟".
    - Если `user_id` присутствует в списке `settings.ADMIN_IDS`, добавляет кнопку "⚙️ Админ панель".
    - Устанавливает расположение кнопок в один столбец.

    Пример:
        >>> main_user_kb(12345)
        <InlineKeyboardMarkup object>
    """
    ...
```

### `catalog_kb`

```python
def catalog_kb(catalog_data: List[Category]) -> InlineKeyboardMarkup:
    """ Функция создает клавиатуру каталога на основе списка категорий.

    Args:
        catalog_data (List[Category]): Список объектов категорий.

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры.
    
    Как работает функция:
    - Создает инлайн-клавиатуру, добавляя кнопки для каждой категории из списка `catalog_data`.
    - Добавляет кнопку "🏠 На главную".
    - Устанавливает расположение кнопок в два столбца.

    Пример:
        >>> catalog_kb([Category(id=1, category_name="Category 1"), Category(id=2, category_name="Category 2")])
        <InlineKeyboardMarkup object>
    """
    ...
```

### `purchases_kb`

```python
def purchases_kb() -> InlineKeyboardMarkup:
    """ Функция создает клавиатуру для управления покупками.

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры.
    
    Как работает функция:
    - Создает инлайн-клавиатуру с кнопками "🗑 Смотреть покупки" и "🏠 На главную".
    - Устанавливает расположение кнопок в один столбец.

    Пример:
        >>> purchases_kb()
        <InlineKeyboardMarkup object>
    """
    ...
```

### `product_kb`

```python
def product_kb(product_id, price, stars_price) -> InlineKeyboardMarkup:
    """ Функция создает клавиатуру продукта с вариантами оплаты.

    Args:
        product_id: ID продукта.
        price: Цена продукта в рублях.
        stars_price: Цена продукта в звездах.

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры.
    
    Как работает функция:
    - Создает инлайн-клавиатуру с кнопками для оплаты через ЮКасса, Robocassa и звездами.
    - Добавляет кнопки "🛍 Назад" и "🏠 На главную".
    - Устанавливает расположение кнопок в два столбца.

    Пример:
        >>> product_kb(123, 100, 50)
        <InlineKeyboardMarkup object>
    """
    ...
```

### `get_product_buy_youkassa`

```python
def get_product_buy_youkassa(price) -> InlineKeyboardMarkup:
    """ Функция создает клавиатуру для оплаты продукта через ЮКасса.

    Args:
        price: Цена продукта.

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры.
    
    Как работает функция:
    - Создает инлайн-клавиатуру с кнопкой для оплаты через ЮКасса и кнопкой "Отменить".

    Пример:
        >>> get_product_buy_youkassa(100)
        <InlineKeyboardMarkup object>
    """
    ...
```

### `get_product_buy_robocassa`

```python
def get_product_buy_robocassa(price: int, payment_link: str) -> InlineKeyboardMarkup:
    """ Функция создает клавиатуру для оплаты продукта через Robocassa.

    Args:
        price (int): Цена продукта.
        payment_link (str): Ссылка на оплату в Robocassa.

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры.
    
    Как работает функция:
    - Создает инлайн-клавиатуру с кнопкой для оплаты через Robocassa (открывается в WebApp) и кнопкой "Отменить".

    Пример:
        >>> get_product_buy_robocassa(100, "https://robokassa.ru/payment_link")
        <InlineKeyboardMarkup object>
    """
    ...
```

### `get_product_buy_stars`

```python
def get_product_buy_stars(price) -> InlineKeyboardMarkup:
    """ Функция создает клавиатуру для оплаты продукта звездами.

    Args:
        price: Цена продукта в звездах.

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры.
    
    Как работает функция:
    - Создает инлайн-клавиатуру с кнопкой для оплаты звездами и кнопкой "Отменить".

    Пример:
        >>> get_product_buy_stars(50)
        <InlineKeyboardMarkup object>
    """
    ...
```