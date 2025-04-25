# Модуль EasyChat

## Обзор

Модуль `EasyChat` предоставляет реализацию класса `EasyChat`, который представляет собой провайдера для доступа к модели GPT-4 Free через API `https://free.easychat.work`. Класс `EasyChat` наследует абстрактный класс `AbstractProvider` и реализует метод `create_completion` для генерации текстового ответа.

## Классы

### `class EasyChat`

**Описание**: Класс `EasyChat` представляет собой провайдера для доступа к модели GPT-4 Free через API `https://free.easychat.work`.

**Наследует**: `AbstractProvider`

**Атрибуты**:

- `url` (str): URL-адрес API `https://free.easychat.work`.
- `supports_stream` (bool): Флаг, указывающий, поддерживается ли потоковая передача данных.
- `supports_gpt_35_turbo` (bool): Флаг, указывающий, поддерживается ли модель GPT-3.5 Turbo.
- `working` (bool): Флаг, указывающий, работает ли провайдер.

**Методы**:

- `create_completion(model: str, messages: list[dict[str, str]], stream: bool, **kwargs: Any) -> CreateResult`

**Методы**:

### `def create_completion(model: str, messages: list[dict[str, str]], stream: bool, **kwargs: Any) -> CreateResult`

**Назначение**: Метод `create_completion` выполняет запрос к API `https://free.easychat.work` для генерации текстового ответа.

**Параметры**:

- `model` (str): Название модели GPT-4 Free.
- `messages` (list[dict[str, str]]): Список сообщений в формате `[{"role": "user", "content": "Текст пользователя"}, {"role": "assistant", "content": "Ответ ассистента"}]`.
- `stream` (bool): Флаг, указывающий, использовать ли потоковую передачу данных.
- `**kwargs`: Any): Словарь дополнительных аргументов.

**Возвращает**:

- `CreateResult`: Объект `CreateResult`, содержащий результат генерации текста.

**Как работает функция**:

- Метод `create_completion` выбирает случайный сервер из списка доступных серверов `active_servers`.
- Метод формирует заголовок запроса `headers` с информацией о сервере, типе запроса, языке и т.д.
- Метод формирует JSON-данные `json_data` с параметрами запроса, включая модель, сообщения, температуру, штрафы и т.д.
- Метод использует сессию `requests.Session` для отправки запроса `POST` на сервер `https://free.easychat.work/api/openai/v1/chat/completions` с использованием заголовка `headers` и JSON-данных `json_data`.
- Метод проверяет код ответа сервера. Если код ответа не равен `200`, выбрасывается исключение `Exception`.
- Если потоковая передача данных не используется, метод извлекает ответ из JSON-данных `json_data` и возвращает его в виде строки.
- Если потоковая передача данных используется, метод перебирает строки ответа и выдает каждую строку в виде JSON-объекта с ключом `content`.

**Примеры**:

```python
from hypotez.src.endpoints.gpt4free.g4f.Provider.deprecated.EasyChat import EasyChat

# Создание экземпляра класса EasyChat
easy_chat = EasyChat()

# Список сообщений
messages = [
    {"role": "user", "content": "Привет!"},
    {"role": "assistant", "content": "Привет! 👋 Чем могу помочь?"}
]

# Запрос на генерацию текста с использованием потоковой передачи данных
result = easy_chat.create_completion(
    model="gpt-4",
    messages=messages,
    stream=True
)

# Вывод результата генерации текста
for chunk in result:
    print(chunk)
```

```python
from hypotez.src.endpoints.gpt4free.g4f.Provider.deprecated.EasyChat import EasyChat

# Создание экземпляра класса EasyChat
easy_chat = EasyChat()

# Список сообщений
messages = [
    {"role": "user", "content": "Привет!"},
    {"role": "assistant", "content": "Привет! 👋 Чем могу помочь?"}
]

# Запрос на генерацию текста без использования потоковой передачи данных
result = easy_chat.create_completion(
    model="gpt-4",
    messages=messages,
    stream=False
)

# Вывод результата генерации текста
print(result)
```
```python
from hypotez.src.endpoints.gpt4free.g4f.Provider.deprecated.EasyChat import EasyChat

# Создание экземпляра класса EasyChat
easy_chat = EasyChat()

# Список сообщений
messages = [
    {"role": "user", "content": "Привет!"},
    {"role": "assistant", "content": "Привет! 👋 Чем могу помочь?"}
]

# Запрос на генерацию текста с использованием потоковой передачи данных и дополнительными параметрами
result = easy_chat.create_completion(
    model="gpt-4",
    messages=messages,
    stream=True,
    temperature=0.7,
    presence_penalty=0.2
)

# Вывод результата генерации текста
for chunk in result:
    print(chunk)
```

**Внутренние функции**: 

- Метод `create_completion` использует внутренние функции `_get_server`, `_get_headers`, `_get_json_data` и `_process_response` для выполнения отдельных задач:
    - `_get_server`: Выбирает случайный сервер из списка доступных серверов.
    - `_get_headers`: Формирует заголовок запроса.
    - `_get_json_data`: Формирует JSON-данные для запроса.
    - `_process_response`: Обрабатывает ответ сервера.
```markdown