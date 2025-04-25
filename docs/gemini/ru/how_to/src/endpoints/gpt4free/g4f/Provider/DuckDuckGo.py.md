## Как использовать `DuckDuckGo` 
=========================================================================================

Описание
-------------------------
Класс `DuckDuckGo` реализует  интерфейс асинхронного генератора  для получения ответов от DuckDuckGo AI. 

Шаги выполнения
-------------------------
1. **Инициализация:**
    - Импорт необходимых модулей: `duckduckgo_search`, `nodriver`.
    - Проверка наличия необходимых модулей с помощью `has_requirements` и `has_nodriver`.
2. **Создание асинхронного генератора:**
    - Вызов метода `create_async_generator` для создания генератора.
    - Передача параметров: `model` (имя модели), `messages` (история сообщений), `proxy` (прокси-сервер), `timeout` (таймаут).
3. **Инициализация `DDGS`:**
    -  Проверка, инициализирован ли объект `ddgs` (класса `DDGS` из `duckduckgo_search`).
    -  Если нет - создание объекта `ddgs`. 
    -  Установка `proxy` и `timeout` для `ddgs`.
4. **Аутентификация с `nodriver`:**
    -  Если `has_nodriver` - вызов метода `nodriver_auth` для аутентификации.
    -  Инициализация браузера с помощью `nodriver` и открытие страницы  `https://duckduckgo.com/aichat`.
    -  Извлечение `X-Vqd-4`, `X-Vqd-Hash-1` и `F-Fe-Version`  из заголовков запросов, отправленных на `api_base`.
    -  Сохранение извлеченных значений в  `_chat_vqd`, `_chat_vqd_hash` и `_chat_xfe` для `ddgs`.
5. **Получение ответа от `DuckDuckGo`:**
    -  Вызов метода `chat_yield`  из `ddgs` с параметрами:
        -  `get_last_user_message(messages)` - последнее сообщение пользователя из `messages`.
        -  `model` - выбранная модель.
        -  `timeout` - таймаут.
6. **Итерация по генератору:**
    -  Использование цикла `for` для перебора выданных `chunk` и получение ответа по частям (стриминговый режим).
    -  Возврат каждого `chunk` как результат генератора.

Пример использования
-------------------------

```python
from hypotez.src.endpoints.gpt4free.g4f.Provider.DuckDuckGo import DuckDuckGo

# Инициализация истории сообщений
messages = [
    {"role": "user", "content": "Привет!"},
    {"role": "assistant", "content": "Привет! 👋 Как могу помочь?"},
]

# Создание асинхронного генератора
async def main():
    async for chunk in DuckDuckGo.create_async_generator(model="gpt-4o-mini", messages=messages):
        print(chunk)

asyncio.run(main())
```