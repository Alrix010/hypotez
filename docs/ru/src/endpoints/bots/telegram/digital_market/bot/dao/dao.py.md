# Модуль для доступа к данным (DAO) в боте Telegram для цифрового рынка
========================================================================

Модуль содержит классы DAO (Data Access Object) для работы с базой данных, используемой в Telegram-боте для цифрового рынка.
Эти классы обеспечивают взаимодействие с таблицами `User`, `Purchase`, `Category` и `Product` посредством асинхронных сессий SQLAlchemy.

## Обзор

Этот модуль предоставляет набор классов DAO для выполнения операций CRUD (Create, Read, Update, Delete) с различными сущностями, такими как пользователи, покупки, категории и продукты. Он также включает методы для получения статистической информации, связанной с этими сущностями.

## Подробнее

Модуль использует SQLAlchemy для взаимодействия с базой данных асинхронно. Каждый класс DAO связан с определенной моделью базы данных и предоставляет методы для выполнения запросов к соответствующей таблице.

## Содержание

- [Классы](#классы)
    - [`UserDAO`](#userdao)
        - [`get_purchase_statistics`](#get_purchase_statistics)
        - [`get_purchased_products`](#get_purchased_products)
        - [`get_statistics`](#get_statistics)
    - [`PurchaseDao`](#purchasedao)
        - [`get_payment_stats`](#get_payment_stats)
        - [`get_full_summ`](#get_full_summ)
        - [`get_next_id`](#get_next_id)
    - [`CategoryDao`](#categorydao)
    - [`ProductDao`](#productdao)

## Классы

### `UserDAO`

**Описание**: Класс для доступа к данным пользователей.

**Наследует**: `BaseDAO[User]`

**Методы**:
- `get_purchase_statistics`: Получает статистику покупок пользователя.
- `get_purchased_products`: Получает список приобретенных пользователем продуктов.
- `get_statistics`: Получает общую статистику по пользователям.

#### `get_purchase_statistics`

```python
@classmethod
async def get_purchase_statistics(cls, session: AsyncSession, telegram_id: int) -> Optional[Dict[str, int]]:
    """
    Получает статистику покупок пользователя, такую как общее количество покупок и общая сумма покупок.

    Args:
        session (AsyncSession): Асинхронная сессия базы данных.
        telegram_id (int): Идентификатор пользователя в Telegram.

    Returns:
        Optional[Dict[str, int]]: Словарь со статистикой покупок пользователя или None в случае ошибки.
                                    Словарь содержит ключи 'total_purchases' (общее количество покупок)
                                    и 'total_amount' (общая сумма покупок).

    Raises:
        SQLAlchemyError: При возникновении ошибки при работе с базой данных.

    Как работает функция:
    - Формирует запрос к базе данных для подсчета общего числа покупок и общей суммы покупок для указанного пользователя.
    - Выполняет запрос с использованием асинхронной сессии.
    - Обрабатывает результат запроса, возвращая словарь со статистикой.
    - В случае ошибки логирует информацию об ошибке и возвращает None.

    Примеры:
        >>> session = AsyncSession()
        >>> telegram_id = 123456789
        >>> stats = await UserDAO.get_purchase_statistics(session, telegram_id)
        >>> if stats:
        ...     print(f"Общее количество покупок: {stats['total_purchases']}")
        ...     print(f"Общая сумма покупок: {stats['total_amount']}")
    """
    ...
```

#### `get_purchased_products`

```python
    @classmethod
    async def get_purchased_products(cls, session: AsyncSession, telegram_id: int) -> Optional[List[Purchase]]:
        """
        Получает список продуктов, приобретенных пользователем.

        Args:
            session (AsyncSession): Асинхронная сессия базы данных.
            telegram_id (int): Идентификатор пользователя в Telegram.

        Returns:
            Optional[List[Purchase]]: Список покупок пользователя, где каждая покупка содержит информацию о продукте, или None в случае ошибки.

        Raises:
            SQLAlchemyError: При возникновении ошибки при работе с базой данных.

        Как работает функция:
        - Формирует запрос к базе данных для получения пользователя с его покупками и связанными продуктами.
        - Выполняет запрос с использованием асинхронной сессии.
        - Извлекает список покупок пользователя из результата запроса.
        - В случае ошибки логирует информацию об ошибке и возвращает None.

        Примеры:
            >>> session = AsyncSession()
            >>> telegram_id = 123456789
            >>> purchases = await UserDAO.get_purchased_products(session, telegram_id)
            >>> if purchases:
            ...     for purchase in purchases:
            ...         print(f"Продукт: {purchase.product.name}, Цена: {purchase.price}")
        """
        ...
```

#### `get_statistics`

```python
    @classmethod
    async def get_statistics(cls, session: AsyncSession):
        """
        Получает общую статистику по пользователям, такую как общее количество пользователей,
        количество новых пользователей за сегодня, за неделю и за месяц.

        Args:
            session (AsyncSession): Асинхронная сессия базы данных.

        Returns:
            dict: Словарь со статистикой по пользователям.
                  Содержит ключи 'total_users' (общее количество пользователей), 'new_today' (количество новых пользователей за сегодня),
                  'new_week' (количество новых пользователей за неделю) и 'new_month' (количество новых пользователей за месяц).

        Raises:
            SQLAlchemyError: При возникновении ошибки при работе с базой данных.

        Как работает функция:
        - Формирует запрос к базе данных для подсчета общего количества пользователей и количества новых пользователей за разные периоды времени.
        - Выполняет запрос с использованием асинхронной сессии.
        - Извлекает статистические данные из результата запроса.
        - Логирует информацию об успешном получении статистики.
        - В случае ошибки логирует информацию об ошибке и пробрасывает исключение.

        Примеры:
            >>> session = AsyncSession()
            >>> stats = await UserDAO.get_statistics(session)
            >>> print(f"Общее количество пользователей: {stats['total_users']}")
            >>> print(f"Новых пользователей за сегодня: {stats['new_today']}")
            >>> print(f"Новых пользователей за неделю: {stats['new_week']}")
            >>> print(f"Новых пользователей за месяц: {stats['new_month']}")
        """
        ...
```

### `PurchaseDao`

**Описание**: Класс для доступа к данным о покупках.

**Наследует**: `BaseDAO[Purchase]`

**Методы**:
- `get_payment_stats`: Получает статистику по типам оплат.
- `get_full_summ`: Получает общую сумму всех покупок.
- `get_next_id`: Возвращает следующий свободный ID для новой записи.

#### `get_payment_stats`

```python
    @classmethod
    async def get_payment_stats(cls, session: AsyncSession) -> str:
        """
        Получает статистику по типам оплат, такую как общая сумма оплат для каждого типа (Юкасса, Робокасса, STARS).

        Args:
            session (AsyncSession): Асинхронная сессия базы данных.

        Returns:
            str: Отформатированная строка со статистикой по типам оплат.

        Как работает функция:
        - Формирует запрос к базе данных для подсчета общей суммы оплат для каждого типа оплаты.
        - Выполняет запрос с использованием асинхронной сессии.
        - Обрабатывает результат запроса, формируя словарь со статистикой.
        - Форматирует словарь в строку для удобного отображения статистики.

        Примеры:
            >>> session = AsyncSession()
            >>> stats = await PurchaseDao.get_payment_stats(session)
            >>> print(stats)
            '💳 Юкасса: 1234.56 ₽\\n🤖 Робокасса: 789.01 ₽\\n⭐ STARS: 42\\n\\nСтатистика актуальна на данный момент.'
        """
        ...
```

#### `get_full_summ`

```python
    @classmethod
    async def get_full_summ(cls, session: AsyncSession) -> int:
        """
        Получает общую сумму всех покупок.

        Args:
            session (AsyncSession): Асинхронная сессия базы данных.

        Returns:
            int: Общая сумма всех покупок.

        Как работает функция:
        - Формирует запрос к базе данных для подсчета общей суммы всех покупок.
        - Выполняет запрос с использованием асинхронной сессии.
        - Извлекает общую сумму из результата запроса.

        Примеры:
            >>> session = AsyncSession()
            >>> total_sum = await PurchaseDao.get_full_summ(session)
            >>> print(f"Общая сумма всех покупок: {total_sum}")
        """
        ...
```

#### `get_next_id`

```python
    @classmethod
    async def get_next_id(cls, session: AsyncSession) -> int:
        """
        Возвращает следующий свободный ID для новой записи.

        Args:
            session (AsyncSession): Асинхронная сессия базы данных

        Returns:
            int: Следующий свободный ID

        Как работает функция:
           -  Функция запрашивает максимальный ID из таблицы `Purchase` и прибавляет к нему 1.
           -  Если таблица пуста, возвращает 1.

        Примеры:
            >>> session = AsyncSession()
            >>> next_id = await PurchaseDao.get_next_id(session)
            >>> print(f"Следующий ID: {next_id}")
        """
        ...
```

### `CategoryDao`

**Описание**: Класс для доступа к данным о категориях.

**Наследует**: `BaseDAO[Category]`

### `ProductDao`

**Описание**: Класс для доступа к данным о продуктах.

**Наследует**: `BaseDAO[Product]`