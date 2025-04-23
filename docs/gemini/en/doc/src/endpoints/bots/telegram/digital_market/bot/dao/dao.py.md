# Документация модуля dao.py

## Описание

Модуль `dao.py` содержит классы для взаимодействия с базой данных, используя SQLAlchemy. Он предоставляет DAO (Data Access Object) для моделей `User`, `Purchase`, `Category` и `Product`. Включает методы для получения статистической информации о пользователях и покупках, а также для работы с категориями и продуктами.

## Содержание

- [UserDAO](#UserDAO)
  - [get_purchase_statistics](#get_purchase_statistics)
  - [get_purchased_products](#get_purchased_products)
  - [get_statistics](#get_statistics)
- [PurchaseDao](#PurchaseDao)
  - [get_payment_stats](#get_payment_stats)
  - [get_full_summ](#get_full_summ)
  - [get_next_id](#get_next_id)
- [CategoryDao](#CategoryDao)
- [ProductDao](#ProductDao)

## Детали

### `UserDAO`

Класс для доступа к данным модели `User`.
**Наследуется от**: `BaseDAO[User]`

#### `get_purchase_statistics`

```python
@classmethod
async def get_purchase_statistics(cls, session: AsyncSession, telegram_id: int) -> Optional[Dict[str, int]]:
    """
    Функция получает статистику покупок пользователя.

    Args:
        session (AsyncSession): Асинхронная сессия базы данных.
        telegram_id (int): Telegram ID пользователя.

    Returns:
        Optional[Dict[str, int]]: Словарь со статистикой покупок пользователя или `None` в случае ошибки.
                                  Содержит ключи `'total_purchases'` (общее количество покупок) и `'total_amount'` (общая сумма покупок).

    Raises:
        SQLAlchemyError: При возникновении ошибки при работе с базой данных.

    Example:
        Пример вызова:
        >>> await UserDAO.get_purchase_statistics(session, 123456789)
        {'total_purchases': 10, 'total_amount': 1000}
    """
```

**Как работает**:

1.  Формируется запрос к базе данных для подсчета общего числа покупок и общей суммы покупок для указанного `telegram_id`.
2.  Выполняется запрос с использованием `session.execute`.
3.  Извлекаются результаты запроса.
4.  В случае отсутствия данных возвращается `None`.
5.  Возвращается словарь с ключами `'total_purchases'` и `'total_amount'`.
6.  При возникновении ошибки SQLAlchemyError, она регистрируется в логе, и возвращается `None`.

#### `get_purchased_products`

```python
@classmethod
async def get_purchased_products(cls, session: AsyncSession, telegram_id: int) -> Optional[List[Purchase]]:
    """
    Функция получает список приобретенных товаров пользователем.

    Args:
        session (AsyncSession): Асинхронная сессия базы данных.
        telegram_id (int): Telegram ID пользователя.

    Returns:
        Optional[List[Purchase]]: Список покупок пользователя или `None` в случае ошибки.

    Raises:
        SQLAlchemyError: При возникновении ошибки при работе с базой данных.

    Example:
        Пример вызова:
        >>> await UserDAO.get_purchased_products(session, 123456789)
        [<Purchase object at 0x...>, <Purchase object at 0x...>]
    """
```

**Как работает**:

1.  Формируется запрос к базе данных для получения пользователя с его покупками и связанными продуктами на основе `telegram_id`.
2.  Используется `selectinload` для оптимизации загрузки связанных данных.
3.  Выполняется запрос с использованием `session.execute`.
4.  Извлекается объект пользователя.
5.  В случае отсутствия пользователя возвращается `None`.
6.  Возвращается список покупок пользователя.
7.  При возникновении ошибки SQLAlchemyError, она регистрируется в логе, и возвращается `None`.

#### `get_statistics`

```python
@classmethod
async def get_statistics(cls, session: AsyncSession):
    """
    Функция получает статистику по пользователям (общее количество, новые за сегодня, неделю, месяц).

    Args:
        session (AsyncSession): Асинхронная сессия базы данных.

    Returns:
        Dict[str, int]: Словарь со статистикой пользователей.

    Raises:
        SQLAlchemyError: При возникновении ошибки при работе с базой данных.

    Example:
        Пример вызова:
        >>> await UserDAO.get_statistics(session)
        {'total_users': 100, 'new_today': 5, 'new_week': 20, 'new_month': 50}
    """
```

**Как работает**:

1.  Получает текущее время в UTC.
2.  Формирует запрос к базе данных для подсчета общего количества пользователей, новых пользователей за сегодня, за неделю и за месяц.
3.  Используется `case` для условного подсчета новых пользователей.
4.  Выполняется запрос с использованием `session.execute`.
5.  Извлекаются результаты запроса.
6.  Формируется и возвращается словарь со статистикой.
7.  В случае возникновения ошибки SQLAlchemyError, она регистрируется в логе и вызывается исключение.

### `PurchaseDao`

Класс для доступа к данным модели `Purchase`.

**Наследуется от**: `BaseDAO[Purchase]`

#### `get_payment_stats`

```python
@classmethod
async def get_payment_stats(cls, session: AsyncSession) -> str:
    """
    Функция получает статистику по типам оплат.

    Args:
        session (AsyncSession): Асинхронная сессия базы данных.

    Returns:
        str: Форматированная строка со статистикой по типам оплат.

    Raises:
        SQLAlchemyError: При возникновении ошибки при работе с базой данных.

    Example:
        Пример вызова:
        >>> await PurchaseDao.get_payment_stats(session)
        '💳 Юкасса: 5000.00 ₽\\n🤖 Робокасса: 3000.00 ₽\\n⭐ STARS: 100\\n\\nСтатистика актуальна на данный момент.'
    """
```

**Как работает**:

1.  Формируется запрос к базе данных для получения статистики по типам оплат (payment\_type) и сумме цен (price).
2.  Выполняется запрос с использованием `session.execute`.
3.  Извлекаются результаты запроса.
4.  Формируется словарь `totals` для хранения результатов по каждому типу оплаты.
5.  Заполняется словарь результатами запроса.
6.  Форматируется строка со статистикой.
7.  Возвращается форматированная строка.

#### `get_full_summ`

```python
@classmethod
async def get_full_summ(cls, session: AsyncSession) -> int:
    """
    Функция получает полную сумму всех покупок.

    Args:
        session (AsyncSession): Асинхронная сессия базы данных.

    Returns:
        int: Полная сумма всех покупок.

    Raises:
        SQLAlchemyError: При возникновении ошибки при работе с базой данных.

    Example:
        Пример вызова:
        >>> await PurchaseDao.get_full_summ(session)
        8000
    """
```

**Как работает**:

1.  Формируется запрос к базе данных для получения полной суммы всех покупок.
2.  Выполняется запрос с использованием `session.execute`.
3.  Извлекается результат запроса.
4.  Возвращается полная сумма всех покупок.

#### `get_next_id`

```python
@classmethod
async def get_next_id(cls, session: AsyncSession) -> int:
    """
    Функция возвращает следующий свободный ID для новой записи.

    Args:
        session (AsyncSession): Асинхронная сессия базы данных.

    Returns:
        int: Следующий свободный ID.

    Raises:
        SQLAlchemyError: При возникновении ошибки при работе с базой данных.

    Example:
        Пример вызова:
        >>> await PurchaseDao.get_next_id(session)
        6
    """
```

**Как работает**:

1.  Формируется запрос к базе данных для получения максимального значения ID и добавления 1 для получения следующего свободного ID. Если таблица пуста, возвращается 1.
2.  Выполняется запрос с использованием `session.execute`.
3.  Извлекается результат запроса.
4.  Возвращается следующий свободный ID.

### `CategoryDao`

Класс для доступа к данным модели `Category`.

**Наследуется от**: `BaseDAO[Category]`

### `ProductDao`

Класс для доступа к данным модели `Product`.

**Наследуется от**: `BaseDAO[Product]`