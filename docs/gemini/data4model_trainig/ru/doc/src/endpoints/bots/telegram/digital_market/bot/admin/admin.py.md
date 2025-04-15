# Модуль для управления административной частью Telegram-бота
## Обзор

Данный модуль содержит функциональность для управления административной частью Telegram-бота, включая обработку команд администратора, управление статистикой, добавление и удаление товаров. Он использует библиотеку `aiogram` для работы с Telegram API и `SQLAlchemy` для взаимодействия с базой данных. Модуль содержит роутеры, классы состояний и функции для обработки различных действий администратора, таких как просмотр статистики, добавление новых товаров, удаление существующих товаров и отмена текущих операций.

## Подробнее

Модуль предназначен для упрощения управления контентом и статистикой бота администраторами. Он предоставляет набор функций для выполнения различных административных задач, таких как добавление, удаление и изменение продуктов, просмотр статистики пользователей и заказов, а также управление категориями продуктов.

## Классы

### `AddProduct`

**Описание**:
Класс состояний (FSM - Finite State Machine) для процесса добавления нового продукта.

**Наследует**:
`StatesGroup` из библиотеки `aiogram.fsm.state`, предназначен для хранения состояний в процессе обработки данных.

**Атрибуты**:
- `name` (State): Состояние для ввода имени продукта.
- `description` (State): Состояние для ввода описания продукта.
- `price` (State): Состояние для ввода цены продукта.
- `file_id` (State): Состояние для загрузки файла продукта.
- `category_id` (State): Состояние для выбора категории продукта.
- `hidden_content` (State): Состояние для ввода скрытого контента продукта.
- `confirm_add` (State): Состояние для подтверждения добавления продукта.

**Принцип работы**:
Класс определяет состояния, которые используются в процессе добавления нового продукта через Telegram-бота. Каждое состояние представляет собой отдельный шаг в этом процессе, например, ввод имени, описания, цены и т.д. Это позволяет боту вести интерактивный диалог с администратором, запрашивая необходимую информацию и сохраняя ее в контексте FSM.

## Функции

### `start_admin`

```python
async def start_admin(call: CallbackQuery):
    """
    Args:
        call (CallbackQuery): Объект, представляющий входящий callback-запрос.

    Returns:
        None

    Raises:
        Exception: Если возникает ошибка при открытии админ-панели.

    """
```

**Назначение**:
Обрабатывает callback-запрос для входа в админ-панель.

**Параметры**:
- `call` (CallbackQuery): Объект, содержащий данные callback-запроса от пользователя.

**Возвращает**:
`None`

**Как работает функция**:

1.  Отвечает на callback-запрос сообщением "Доступ в админ-панель разрешен!".
2.  Пытается отредактировать предыдущее сообщение, чтобы отобразить интерфейс админ-панели с помощью клавиатуры `admin_kb()`.
3.  Если редактирование сообщения не удаётся, пытается удалить предыдущее сообщение и отправить новое сообщение с интерфейсом админ-панели.
4.  Если и отправка нового сообщения не удаётся, отправляет сообщение об ошибке.

**Примеры**:

```python
# Пример вызова функции (в контексте aiogram handler)
@admin_router.callback_query(F.data == "admin_panel", F.from_user.id.in_(settings.ADMIN_IDS))
async def start_admin_handler(call: CallbackQuery):
    await start_admin(call)
```

### `admin_statistic`

```python
async def admin_statistic(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Args:
        call (CallbackQuery): Объект, представляющий входящий callback-запрос.
        session_without_commit (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных без коммита.

    Returns:
        None

    Raises:
        Нет

    """
```

**Назначение**:
Обрабатывает callback-запрос для получения статистики.

**Параметры**:
- `call` (CallbackQuery): Объект, содержащий данные callback-запроса от пользователя.
- `session_without_commit` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных без коммита.

**Возвращает**:
`None`

**Как работает функция**:

1.  Отвечает на callback-запрос сообщениями "Запрос на получение статистики..." и "📊 Собираем статистику...".
2.  Получает статистику пользователей с помощью `UserDAO.get_statistics()`.
3.  Получает статистику по платежам с помощью `PurchaseDao.get_payment_stats()`.
4.  Формирует сообщение со статистикой, включая общее количество пользователей, новых пользователей за сегодня, за неделю и за месяц, а также статистику по заказам.
5.  Редактирует предыдущее сообщение, чтобы отобразить статистику и интерфейс админ-панели с помощью клавиатуры `admin_kb()`.

**Примеры**:

```python
# Пример вызова функции (в контексте aiogram handler)
@admin_router.callback_query(F.data == 'statistic', F.from_user.id.in_(settings.ADMIN_IDS))
async def admin_statistic_handler(call: CallbackQuery, session_without_commit: AsyncSession):
    await admin_statistic(call, session_without_commit)
```

### `admin_process_cancel`

```python
async def admin_process_cancel(call: CallbackQuery, state: FSMContext):
    """
    Args:
        call (CallbackQuery): Объект, представляющий входящий callback-запрос.
        state (FSMContext): Контекст FSM для управления состоянием пользователя.

    Returns:
        None

    Raises:
        Нет

    """
```

**Назначение**:
Обрабатывает callback-запрос для отмены сценария добавления товара.

**Параметры**:
- `call` (CallbackQuery): Объект, содержащий данные callback-запроса от пользователя.
- `state` (FSMContext): Контекст FSM для управления состоянием пользователя.

**Возвращает**:
`None`

**Как работает функция**:

1.  Очищает состояние пользователя с помощью `state.clear()`.
2.  Отвечает на callback-запрос сообщением "Отмена сценария добавления товара".
3.  Удаляет предыдущее сообщение.
4.  Отправляет новое сообщение с текстом "Отмена добавления товара." и интерфейсом админ-панели с помощью клавиатуры `admin_kb_back()`.

**Примеры**:

```python
# Пример вызова функции (в контексте aiogram handler)
@admin_router.callback_query(F.data == "cancel", F.from_user.id.in_(settings.ADMIN_IDS))
async def admin_process_cancel_handler(call: CallbackQuery, state: FSMContext):
    await admin_process_cancel(call, state)
```

### `admin_process_start_dell`

```python
async def admin_process_start_dell(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Args:
        call (CallbackQuery): Объект, представляющий входящий callback-запрос.
        session_without_commit (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных без коммита.

    Returns:
        None

    Raises:
        Нет

    """
```

**Назначение**:
Обрабатывает callback-запрос для начала процесса удаления товара.

**Параметры**:
- `call` (CallbackQuery): Объект, содержащий данные callback-запроса от пользователя.
- `session_without_commit` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных без коммита.

**Возвращает**:
`None`

**Как работает функция**:

1.  Отвечает на callback-запрос сообщением "Режим удаления товаров".
2.  Получает список всех товаров из базы данных с помощью `ProductDao.find_all()`.
3.  Редактирует предыдущее сообщение, чтобы отобразить информацию о количестве товаров в базе данных.
4.  Для каждого товара формирует текст с описанием товара (название, описание, цена, скрытое описание) и отправляет сообщение с этим текстом и кнопкой для удаления товара (`dell_product_kb(product_data.id)`).
5.  Если у товара есть файл, отправляет файл с описанием товара, иначе отправляет только текст с описанием товара.

**Примеры**:

```python
# Пример вызова функции (в контексте aiogram handler)
@admin_router.callback_query(F.data == 'delete_product', F.from_user.id.in_(settings.ADMIN_IDS))
async def admin_process_start_dell_handler(call: CallbackQuery, session_without_commit: AsyncSession):
    await admin_process_start_dell(call, session_without_commit)
```

### `admin_process_start_dell`

```python
async def admin_process_start_dell(call: CallbackQuery, session_with_commit: AsyncSession):
    """
    Args:
        call (CallbackQuery): Объект, представляющий входящий callback-запрос.
        session_with_commit (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных с коммитом.

    Returns:
        None

    Raises:
        Нет

    """
```

**Назначение**:
Обрабатывает callback-запрос для удаления товара.

**Параметры**:
- `call` (CallbackQuery): Объект, содержащий данные callback-запроса от пользователя.
- `session_with_commit` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных с коммитом.

**Как работает функция**:

1.  Извлекает ID товара из данных callback-запроса (`call.data`).
2.  Удаляет товар из базы данных с помощью `ProductDao.delete()`.
3.  Отвечает на callback-запрос сообщением об успешном удалении товара.
4.  Удаляет сообщение с информацией о товаре.

**Примеры**:

```python
# Пример вызова функции (в контексте aiogram handler)
@admin_router.callback_query(F.data.startswith('dell_'), F.from_user.id.in_(settings.ADMIN_IDS))
async def admin_process_start_dell_handler(call: CallbackQuery, session_with_commit: AsyncSession):
    await admin_process_start_dell(call, session_with_commit)
```

### `admin_process_products`

```python
async def admin_process_products(call: CallbackQuery, session_without_commit: AsyncSession):
    """
    Args:
        call (CallbackQuery): Объект, представляющий входящий callback-запрос.
        session_without_commit (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных без коммита.

    Returns:
        None

    Raises:
        Нет

    """
```

**Назначение**:
Обрабатывает callback-запрос для отображения интерфейса управления товарами.

**Параметры**:
- `call` (CallbackQuery): Объект, содержащий данные callback-запроса от пользователя.
- `session_without_commit` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных без коммита.

**Возвращает**:
`None`

**Как работает функция**:

1.  Отвечает на callback-запрос сообщением "Режим управления товарами".
2.  Получает общее количество товаров из базы данных с помощью `ProductDao.count()`.
3.  Редактирует предыдущее сообщение, чтобы отобразить информацию о количестве товаров и кнопки для управления товарами (`product_management_kb()`).

**Примеры**:

```python
# Пример вызова функции (в контексте aiogram handler)
@admin_router.callback_query(F.data == 'process_products', F.from_user.id.in_(settings.ADMIN_IDS))
async def admin_process_products_handler(call: CallbackQuery, session_without_commit: AsyncSession):
    await admin_process_products(call, session_without_commit)
```

### `admin_process_add_product`

```python
async def admin_process_add_product(call: CallbackQuery, state: FSMContext):
    """
    Args:
        call (CallbackQuery): Объект, представляющий входящий callback-запрос.
        state (FSMContext): Контекст FSM для управления состоянием пользователя.

    Returns:
        None

    Raises:
        Нет

    """
```

**Назначение**:
Обрабатывает callback-запрос для запуска сценария добавления нового товара.

**Параметры**:
- `call` (CallbackQuery): Объект, содержащий данные callback-запроса от пользователя.
- `state` (FSMContext): Контекст FSM для управления состоянием пользователя.

**Возвращает**:
`None`

**Как работает функция**:

1.  Отвечает на callback-запрос сообщением "Запущен сценарий добавления товара.".
2.  Удаляет предыдущее сообщение.
3.  Отправляет сообщение с запросом имени товара и кнопкой для отмены (`cancel_kb_inline()`).
4.  Обновляет контекст FSM, сохраняя ID последнего отправленного сообщения.
5.  Устанавливает состояние `AddProduct.name`.

**Примеры**:

```python
# Пример вызова функции (в контексте aiogram handler)
@admin_router.callback_query(F.data == 'add_product', F.from_user.id.in_(settings.ADMIN_IDS))
async def admin_process_add_product_handler(call: CallbackQuery, state: FSMContext):
    await admin_process_add_product(call, state)
```

### `admin_process_name`

```python
async def admin_process_name(message: Message, state: FSMContext):
    """
    Args:
        message (Message): Объект, представляющий входящее текстовое сообщение.
        state (FSMContext): Контекст FSM для управления состоянием пользователя.

    Returns:
        None

    Raises:
        Нет

    """
```

**Назначение**:
Обрабатывает ввод имени товара в процессе добавления товара.

**Параметры**:
- `message` (Message): Объект, содержащий данные текстового сообщения от пользователя.
- `state` (FSMContext): Контекст FSM для управления состоянием пользователя.

**Возвращает**:
`None`

**Как работает функция**:

1.  Сохраняет имя товара в контексте FSM.
2.  Удаляет предыдущее сообщение пользователя.
3.  Отправляет сообщение с запросом короткого описания товара и кнопкой для отмены (`cancel_kb_inline()`).
4.  Обновляет контекст FSM, сохраняя ID последнего отправленного сообщения.
5.  Устанавливает состояние `AddProduct.description`.

**Примеры**:

```python
# Пример вызова функции (в контексте aiogram handler)
@admin_router.message(F.text, F.from_user.id.in_(settings.ADMIN_IDS), AddProduct.name)
async def admin_process_name_handler(message: Message, state: FSMContext):
    await admin_process_name(message, state)
```

### `admin_process_description`

```python
async def admin_process_description(message: Message, state: FSMContext, session_without_commit: AsyncSession):
    """
    Args:
        message (Message): Объект, представляющий входящее текстовое сообщение.
        state (FSMContext): Контекст FSM для управления состоянием пользователя.
        session_without_commit (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных без коммита.

    Returns:
        None

    Raises:
        Нет

    """
```

**Назначение**:
Обрабатывает ввод описания товара в процессе добавления товара.

**Параметры**:
- `message` (Message): Объект, представляющий входящее текстовое сообщение.
- `state` (FSMContext): Контекст FSM для управления состоянием пользователя.
- `session_without_commit` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных без коммита.

**Возвращает**:
`None`

**Как работает функция**:

1.  Сохраняет описание товара в контексте FSM.
2.  Удаляет предыдущее сообщение пользователя.
3.  Получает список категорий из базы данных с помощью `CategoryDao.find_all()`.
4.  Отправляет сообщение с запросом выбора категории товара и клавиатурой с категориями (`catalog_admin_kb(catalog_data)`).
5.  Обновляет контекст FSM, сохраняя ID последнего отправленного сообщения.
6.  Устанавливает состояние `AddProduct.category_id`.

**Примеры**:

```python
# Пример вызова функции (в контексте aiogram handler)
@admin_router.message(F.text, F.from_user.id.in_(settings.ADMIN_IDS), AddProduct.description)
async def admin_process_description_handler(message: Message, state: FSMContext, session_without_commit: AsyncSession):
    await admin_process_description(message, state, session_without_commit)
```

### `admin_process_category`

```python
async def admin_process_category(call: CallbackQuery, state: FSMContext):
    """
    Args:
        call (CallbackQuery): Объект, представляющий входящий callback-запрос.
        state (FSMContext): Контекст FSM для управления состоянием пользователя.

    Returns:
        None

    Raises:
        Нет

    """
```

**Назначение**:
Обрабатывает выбор категории товара в процессе добавления товара.

**Параметры**:
- `call` (CallbackQuery): Объект, содержащий данные callback-запроса от пользователя.
- `state` (FSMContext): Контекст FSM для управления состоянием пользователя.

**Возвращает**:
`None`

**Как работает функция**:

1.  Извлекает ID категории из данных callback-запроса (`call.data`).
2.  Сохраняет ID категории в контексте FSM.
3.  Отвечает на callback-запрос сообщением "Категория товара успешно выбрана.".
4.  Редактирует предыдущее сообщение, чтобы запросить цену товара и кнопкой для отмены (`cancel_kb_inline()`).
5.  Обновляет контекст FSM, сохраняя ID последнего отправленного сообщения.
6.  Устанавливает состояние `AddProduct.price`.

**Примеры**:

```python
# Пример вызова функции (в контексте aiogram handler)
@admin_router.callback_query(F.data.startswith("add_category_"),
                             F.from_user.id.in_(settings.ADMIN_IDS),
                             AddProduct.category_id)
async def admin_process_category_handler(call: CallbackQuery, state: FSMContext):
    await admin_process_category(call, state)
```

### `admin_process_price`

```python
async def admin_process_price(message: Message, state: FSMContext):
    """
    Args:
        message (Message): Объект, представляющий входящее текстовое сообщение.
        state (FSMContext): Контекст FSM для управления состоянием пользователя.

    Returns:
        None

    Raises:
        ValueError: Если введенное значение не является числом.

    """
```

**Назначение**:
Обрабатывает ввод цены товара в процессе добавления товара.

**Параметры**:
- `message` (Message): Объект, представляющий входящее текстовое сообщение.
- `state` (FSMContext): Контекст FSM для управления состоянием пользователя.

**Возвращает**:
`None`

**Как работает функция**:

1.  Пытается преобразовать введенное значение в целое число.
2.  Если преобразование успешно, сохраняет цену товара в контексте FSM.
3.  Удаляет предыдущее сообщение пользователя.
4.  Отправляет сообщение с запросом файла товара или предложением пропустить этот шаг (`admin_send_file_kb()`).
5.  Обновляет контекст FSM, сохраняя ID последнего отправленного сообщения.
6.  Устанавливает состояние `AddProduct.file_id`.
7.  Если преобразование не удается, отправляет сообщение об ошибке.

**Примеры**:

```python
# Пример вызова функции (в контексте aiogram handler)
@admin_router.message(F.text, F.from_user.id.in_(settings.ADMIN_IDS), AddProduct.price)
async def admin_process_price_handler(message: Message, state: FSMContext):
    await admin_process_price(message, state)
```

### `admin_process_without_file`

```python
async def admin_process_without_file(call: CallbackQuery, state: FSMContext):
    """
    Args:
        call (CallbackQuery): Объект, представляющий входящий callback-запрос.
        state (FSMContext): Контекст FSM для управления состоянием пользователя.

    Returns:
        None

    Raises:
        Нет

    """
```

**Назначение**:
Обрабатывает выбор отсутствия файла товара в процессе добавления товара.

**Параметры**:
- `call` (CallbackQuery): Объект, представляющий входящий callback-запрос.
- `state` (FSMContext): Контекст FSM для управления состоянием пользователя.

**Возвращает**:
`None`

**Как работает функция**:

1.  Сохраняет `None` в контексте FSM в качестве ID файла.
2.  Отвечает на callback-запрос сообщением "Файл не выбран.".
3.  Редактирует предыдущее сообщение, чтобы запросить скрытый контент товара и кнопкой для отмены (`cancel_kb_inline()`).
4.  Обновляет контекст FSM, сохраняя ID последнего отправленного сообщения.
5.  Устанавливает состояние `AddProduct.hidden_content`.

**Примеры**:

```python
# Пример вызова функции (в контексте aiogram handler)
@admin_router.callback_query(F.data == "without_file", F.from_user.id.in_(settings.ADMIN_IDS), AddProduct.file_id)
async def admin_process_without_file_handler(call: CallbackQuery, state: FSMContext):
    await admin_process_without_file(call, state)
```

### `admin_process_without_file`

```python
async def admin_process_without_file(message: Message, state: FSMContext):
    """
    Args:
        message (Message): Объект, представляющий входящее сообщение с документом (файлом).
        state (FSMContext): Контекст FSM для управления состоянием пользователя.

    Returns:
        None

    Raises:
        Нет

    """
```

**Назначение**:
Обрабатывает загрузку файла товара в процессе добавления товара.

**Параметры**:
- `message` (Message): Объект, представляющий входящее сообщение с файлом от пользователя.
- `state` (FSMContext): Контекст FSM для управления состоянием пользователя.

**Возвращает**:
`None`

**Как работает функция**:

1.  Сохраняет ID файла в контексте FSM.
2.  Удаляет предыдущее сообщение пользователя.
3.  Отправляет сообщение с запросом скрытого контента товара и кнопкой для отмены (`cancel_kb_inline()`).
4.  Обновляет контекст FSM, сохраняя ID последнего отправленного сообщения.
5.  Устанавливает состояние `AddProduct.hidden_content`.

**Примеры**:

```python
# Пример вызова функции (в контексте aiogram handler)
@admin_router.message(F.document, F.from_user.id.in_(settings.ADMIN_IDS), AddProduct.file_id)
async def admin_process_without_file_handler(message: Message, state: FSMContext):
    await admin_process_without_file(message, state)
```

### `admin_process_hidden_content`

```python
async def admin_process_hidden_content(message: Message, state: FSMContext, session_without_commit: AsyncSession):
    """
    Args:
        message (Message): Объект, представляющий входящее текстовое сообщение.
        state (FSMContext): Контекст FSM для управления состоянием пользователя.
        session_without_commit (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных без коммита.

    Returns:
        None

    Raises:
        Нет

    """
```

**Назначение**:
Обрабатывает ввод скрытого контента товара в процессе добавления товара.

**Параметры**:
- `message` (Message): Объект, представляющий входящее текстовое сообщение.
- `state` (FSMContext): Контекст FSM для управления состоянием пользователя.
- `session_without_commit` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных без коммита.

**Возвращает**:
`None`

**Как работает функция**:

1.  Сохраняет скрытый контент товара в контексте FSM.
2.  Получает данные о товаре из контекста FSM.
3.  Получает информацию о категории товара из базы данных с помощью `CategoryDao.find_one_or_none_by_id()`.
4.  Формирует текст с информацией о товаре (название, описание, цена, скрытый контент, категория, наличие файла).
5.  Удаляет предыдущее сообщение пользователя.
6.  Если у товара есть файл, отправляет файл с информацией о товаре и кнопками для подтверждения или отмены (`admin_confirm_kb()`), иначе отправляет только текст с информацией о товаре.
7.  Обновляет контекст FSM, сохраняя ID последнего отправленного сообщения.
8.  Устанавливает состояние `AddProduct.confirm_add`.

**Примеры**:

```python
# Пример вызова функции (в контексте aiogram handler)
@admin_router.message(F.text, F.from_user.id.in_(settings.ADMIN_IDS), AddProduct.hidden_content)
async def admin_process_hidden_content_handler(message: Message, state: FSMContext, session_without_commit: AsyncSession):
    await admin_process_hidden_content(message, state, session_without_commit)
```

### `admin_process_confirm_add`

```python
async def admin_process_confirm_add(call: CallbackQuery, state: FSMContext, session_with_commit: AsyncSession):
    """
    Args:
        call (CallbackQuery): Объект, представляющий входящий callback-запрос.
        state (FSMContext): Контекст FSM для управления состоянием пользователя.
        session_with_commit (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных с коммитом.

    Returns:
        None

    Raises:
        Нет

    """
```

**Назначение**:
Обрабатывает подтверждение добавления товара в базу данных.

**Параметры**:
- `call` (CallbackQuery): Объект, представляющий входящий callback-запрос.
- `state` (FSMContext): Контекст FSM для управления состоянием пользователя.
- `session_with_commit` (AsyncSession): Асинхровая сессия SQLAlchemy для выполнения запросов к базе данных с коммитом.

**Возвращает**:
`None`

**Как работает функция**:

1.  Отвечает на callback-запрос сообщением "Приступаю к сохранению файла!".
2.  Получает данные о товаре из контекста FSM.
3.  Удаляет сообщение с подтверждением информации о товаре.
4.  Удаляет ID последнего сообщения из данных о товаре.
5.  Добавляет товар в базу данных с помощью `ProductDao.add()`.
6.  Отправляет сообщение об успешном добавлении товара в базу данных и интерфейс админ-панели с помощью клавиатуры `admin_kb()`.

**Примеры**:

```python
# Пример вызова функции (в контексте aiogram handler)
@admin_router.callback_query(F.data == "confirm_add", F.from_user.id.in_(settings.ADMIN_IDS))
async def admin_process_confirm_add_handler(call: CallbackQuery, state: FSMContext, session_with_commit: AsyncSession):
    await admin_process_confirm_add(call, state, session_with_commit)