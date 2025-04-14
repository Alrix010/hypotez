# Модуль для взаимодействия с Grok AI
==========================================

Модуль содержит класс `Grok`, который используется для взаимодействия с Grok AI.
Он предоставляет возможности для аутентификации, создания бесед и получения ответов от модели.

## Обзор

Модуль `Grok` предоставляет интерфейс для взаимодействия с Grok AI, включая аутентификацию, создание бесед и получение ответов от модели. Он поддерживает работу с различными моделями, такими как "grok-3", "grok-3-thinking" и "grok-2".

## Подробнее

Модуль предназначен для интеграции с Grok AI через API. Он предоставляет удобные методы для аутентификации, подготовки запросов и обработки ответов. Он также поддерживает работу с cookies и прокси для обеспечения безопасного и надежного соединения.

## Классы

### `Conversation`

**Описание**: Класс представляет собой беседу с Grok AI.

**Атрибуты**:

- `conversation_id` (str): Уникальный идентификатор беседы.

### `Grok`

**Описание**: Класс для взаимодействия с Grok AI.

**Принцип работы**:
Класс `Grok` наследуется от `AsyncAuthedProvider` и `ProviderModelMixin`. Он предоставляет методы для аутентификации, подготовки полезной нагрузки и создания бесед. Он также обрабатывает ответы от Grok AI, извлекая текст, изображения и метаданные.

**Атрибуты**:

- `label` (str): Метка провайдера ("Grok AI").
- `url` (str): URL Grok AI ("https://grok.com").
- `cookie_domain` (str): Домен для cookies (".grok.com").
- `assets_url` (str): URL для ресурсов Grok AI ("https://assets.grok.com").
- `conversation_url` (str): URL для управления беседами ("https://grok.com/rest/app-chat/conversations").
- `needs_auth` (bool): Требуется ли аутентификация (True).
- `working` (bool): Работоспособность провайдера (True).
- `default_model` (str): Модель по умолчанию ("grok-3").
- `models` (list): Список поддерживаемых моделей ([default_model, "grok-3-thinking", "grok-2"]).
- `model_aliases` (dict): Псевдонимы моделей ({"grok-3-r1": "grok-3-thinking"}).

**Методы**:

- `on_auth_async()`: Метод для асинхронной аутентификации.
- `_prepare_payload()`: Метод для подготовки полезной нагрузки для запроса.
- `create_authed()`: Метод для создания аутентифицированной беседы и получения ответов.

## Функции

### `on_auth_async`

```python
@classmethod
async def on_auth_async(cls, cookies: Cookies = None, proxy: str = None, **kwargs) -> AsyncIterator:
    """Асинхронно обрабатывает процесс аутентификации для Grok AI.

    Args:
        cookies (Cookies, optional): Cookie для аутентификации. По умолчанию `None`.
        proxy (str, optional): Прокси-сервер для использования при подключении. По умолчанию `None`.

    Yields:
        AsyncIterator: Возвращает результаты аутентификации (`AuthResult`) или запрос на логин (`RequestLogin`).

    Raises:
        Нет явных исключений, но может вызывать исключения из `get_args_from_nodriver` при неудачной попытке автоматического входа.

    Как работает функция:
    1. Проверяет наличие cookies. Если cookies не предоставлены, пытается получить их из домена `cls.cookie_domain`.
    2. Если cookies существуют и содержат ключ "sso", функция предполагает, что пользователь уже аутентифицирован.
       В этом случае возвращает объект `AuthResult` с cookies, информацией о прокси и заголовках по умолчанию.
    3. Если cookies отсутствуют или не содержат ключ "sso", функция инициирует процесс запроса логина, возвращая объект `RequestLogin`.
    4. После запроса логина функция пытается автоматически получить аргументы для аутентификации с использованием `get_args_from_nodriver`.
       Возвращает объект `AuthResult` с полученными аргументами, информацией о прокси и заголовках по умолчанию.

    ascii flowchart:
    A [Проверка наличия cookies]
    |
    B [Cookies есть и содержат "sso"?]
    |   Y: C [Возврат AuthResult с cookies]
    |   N: D [Запрос логина (RequestLogin)]
    |      |
    |      E [Получение аргументов аутентификации через get_args_from_nodriver]
    |      |
    |      F [Возврат AuthResult с аргументами]

    Примеры:
    - Пример 1: Пользователь уже аутентифицирован и имеет cookies.
        >>> async for result in Grok.on_auth_async(cookies={"sso": "some_sso_token"}):
        ...     print(result)
        AuthResult(cookies={"sso": "some_sso_token"}, impersonate="chrome", proxy=None, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'})

    - Пример 2: Пользователю требуется войти в систему.
        >>> async for result in Grok.on_auth_async():
        ...     print(result)
        RequestLogin(provider='Grok', url='')
        AuthResult(cookies={'auth_token': '...'}, impersonate='chrome', proxy=None, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'})
    """
    ...
```

### `_prepare_payload`

```python
@classmethod
async def _prepare_payload(cls, model: str, message: str) -> Dict[str, Any]:
    """Подготавливает полезную нагрузку (payload) для запроса к Grok AI.

    Args:
        model (str): Имя используемой модели Grok AI.
        message (str): Текст сообщения для отправки в Grok AI.

    Returns:
        Dict[str, Any]: Словарь с параметрами для запроса к Grok AI.

    Как работает функция:
    1. Определяет, какую модель использовать: "grok-latest" для "grok-2" или "grok-3" в остальных случаях.
    2. Создает словарь с параметрами, необходимыми для запроса к Grok AI, включая текст сообщения,
       вложения файлов и изображений, настройки поиска и генерации изображений.
    3. Возвращает словарь с подготовленной полезной нагрузкой.

    ascii flowchart:
    A [Получение model и message]
    |
    B [Определение имени модели (grok-latest или grok-3)]
    |
    C [Создание словаря payload с параметрами]
    |
    D [Возврат словаря payload]

    Примеры:
    - Пример 1: Подготовка payload для модели "grok-2".
        >>> payload = await Grok._prepare_payload("grok-2", "Hello, Grok!")
        >>> print(payload)
        {'temporary': False, 'modelName': 'grok-latest', 'message': 'Hello, Grok!', 'fileAttachments': [], 'imageAttachments': [], 'disableSearch': False, 'enableImageGeneration': True, 'returnImageBytes': False, 'returnRawGrokInXaiRequest': False, 'enableImageStreaming': True, 'imageGenerationCount': 2, 'forceConcise': False, 'toolOverrides': {}, 'enableSideBySide': True, 'isPreset': False, 'sendFinalMetadata': True, 'customInstructions': '', 'deepsearchPreset': '', 'isReasoning': False}

    - Пример 2: Подготовка payload для модели "grok-3-thinking".
        >>> payload = await Grok._prepare_payload("grok-3-thinking", "Explain quantum physics.")
        >>> print(payload)
        {'temporary': False, 'modelName': 'grok-3', 'message': 'Explain quantum physics.', 'fileAttachments': [], 'imageAttachments': [], 'disableSearch': False, 'enableImageGeneration': True, 'returnImageBytes': False, 'returnRawGrokInXaiRequest': False, 'enableImageStreaming': True, 'imageGenerationCount': 2, 'forceConcise': False, 'toolOverrides': {}, 'enableSideBySide': True, 'isPreset': False, 'sendFinalMetadata': True, 'customInstructions': '', 'deepsearchPreset': '', 'isReasoning': True}
    """
    ...
```

### `create_authed`

```python
@classmethod
async def create_authed(
    cls,
    model: str,
    messages: Messages,
    auth_result: AuthResult,
    cookies: Cookies = None,
    return_conversation: bool = False,
    conversation: Conversation = None,
    **kwargs
) -> AsyncResult:
    """Создает аутентифицированный запрос к Grok AI и обрабатывает его ответ.

    Args:
        model (str): Имя используемой модели Grok AI.
        messages (Messages): Список сообщений для отправки в Grok AI.
        auth_result (AuthResult): Результат аутентификации.
        cookies (Cookies, optional): Cookie для аутентификации. По умолчанию `None`.
        return_conversation (bool, optional): Возвращать ли информацию о беседе. По умолчанию `False`.
        conversation (Conversation, optional): Объект беседы. По умолчанию `None`.

    Yields:
        AsyncResult: Возвращает результаты ответа от Grok AI, включая текст, изображения и метаданные.

    Raises:
        Exception: Возникает, если ответ от сервера не имеет статус 200.

    Как работает функция:
    1. Определяет идентификатор беседы (`conversation_id`), если он предоставлен в аргументе `conversation`.
       В противном случае устанавливает `conversation_id` в `None`.
    2. Форматирует текст сообщения (`prompt`) для отправки в Grok AI. Если `conversation_id` не `None`,
       использует последнее сообщение пользователя из `messages`.
    3. Создает асинхронную сессию (`StreamSession`) с использованием данных аутентификации из `auth_result`.
    4. Подготавливает полезную нагрузку (`payload`) для запроса с помощью метода `_prepare_payload`.
    5. Определяет URL для запроса: создает новую беседу, если `conversation_id` равен `None`,
       или отправляет сообщение в существующую беседу.
    6. Отправляет POST-запрос к Grok AI с подготовленной полезной нагрузкой.
    7. Обрабатывает ответ от сервера построчно, извлекая JSON-данные.
    8. Извлекает и передает различные типы данных из ответа, включая текст, изображения и метаданные.
    9. Если `return_conversation` установлен в `True` и `conversation_id` не `None`,
       возвращает объект `Conversation` с идентификатором беседы.

    ascii flowchart:
    A [Получение параметров: model, messages, auth_result, ...]
    |
    B [Определение conversation_id]
    |
    C [Форматирование текста сообщения (prompt)]
    |
    D [Создание асинхронной сессии StreamSession]
    |
    E [Подготовка полезной нагрузки (payload) с помощью _prepare_payload]
    |
    F [Определение URL для запроса (новая или существующая беседа)]
    |
    G [Отправка POST-запроса к Grok AI]
    |
    H [Обработка ответа построчно, извлечение JSON-данных]
    |
    I [Извлечение и передача различных типов данных (текст, изображения, метаданные)]
    |
    J [Если return_conversation и conversation_id, возврат объекта Conversation]

    Примеры:
    - Пример 1: Создание новой беседы с Grok AI.
        >>> auth_result = AuthResult(cookies={"sso": "some_sso_token"}, impersonate="chrome", proxy=None, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'})
        >>> messages = [{"role": "user", "content": "Hello, Grok!"}]
        >>> async for result in Grok.create_authed(model="grok-3", messages=messages, auth_result=auth_result):
        ...     print(result)
        Reasoning(status='🤔 Is thinking...')
        Hello, Grok!

    - Пример 2: Отправка сообщения в существующую беседу.
        >>> conversation = Conversation(conversation_id="12345")
        >>> auth_result = AuthResult(cookies={"sso": "some_sso_token"}, impersonate="chrome", proxy=None, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'})
        >>> messages = [{"role": "user", "content": "How are you?"}]
        >>> async for result in Grok.create_authed(model="grok-3", messages=messages, auth_result=auth_result, conversation=conversation):
        ...     print(result)
        Reasoning(status='🤔 Is thinking...')
        I am doing well, thank you for asking!
    """
    ...