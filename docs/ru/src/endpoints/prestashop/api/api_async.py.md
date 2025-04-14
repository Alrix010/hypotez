# Модуль для асинхронного взаимодействия с API PrestaShop
========================================================

Модуль содержит класс `PrestaShopAsync`, который предоставляет асинхронные методы для взаимодействия с API PrestaShop,
включая операции CRUD, поиск и загрузку изображений.

## Обзор

Этот модуль предназначен для асинхронного взаимодействия с API PrestaShop, позволяя выполнять различные операции, такие как создание, чтение, обновление и удаление данных, а также поиск и загрузку изображений. Он обеспечивает асинхронное выполнение запросов, что позволяет более эффективно использовать ресурсы и повысить производительность.

## Подробнее

Модуль предоставляет класс `PrestaShopAsync`, который инкапсулирует логику взаимодействия с API PrestaShop. Он использует библиотеку `aiohttp` для выполнения асинхронных HTTP-запросов и поддерживает форматы данных JSON и XML. Класс предоставляет методы для выполнения основных операций CRUD, поиска ресурсов, загрузки изображений и получения списка доступных API.

## Классы

### `Format`

```python
class Format(Enum):
    """Data types return (JSON, XML)

    .. deprecated::
        I prefer JSON 👍 :))

    :param Enum: (int): 1 => JSON, 2 => XML
    """
    JSON = 'JSON'
    XML = 'XML'
```

**Описание**: Enum, определяющий форматы данных для взаимодействия с API (JSON, XML).

**Атрибуты**:
- `JSON`: Представляет формат JSON.
- `XML`: Представляет формат XML.

### `PrestaShopAsync`

```python
class PrestaShopAsync:
    """! Async Class for interacting with the PrestaShop API using JSON and XML.

    This class provides asynchronous methods to interact with the PrestaShop API,
    allowing for CRUD operations, searching, and uploading images. It also provides
    error handling for responses and methods to handle the API's data.

    Example usage:

    .. code-block:: python

        async def main():
            api = PrestaShopAsync(
                API_DOMAIN='https://your-prestashop-domain.com',
                API_KEY='your_api_key',
                default_lang=1,
                debug=True,
                data_format='JSON',
            )

            await api.ping()

            data = {
                'tax': {
                    'rate': 3.000,
                    'active': '1',
                    'name': {
                        'language': {
                            'attrs': {'id': '1'},
                            'value': '3% tax'
                        }
                    }
                }
            }

            # Create tax record
            rec = await api.create('taxes', data)

            # Update the same tax record
            update_data = {
                'tax': {
                    'id': str(rec['id']),
                    'rate': 3.000,
                    'active': '1',
                    'name': {
                        'language': {
                            'attrs': {'id': '1'},
                            'value': '3% tax'
                        }
                    }
                }
            }

            update_rec = await api.write('taxes', update_data)

            # Remove this tax
            await api.unlink('taxes', str(rec['id']))

            # Search the first 3 taxes with '5' in the name
            import pprint
            recs = await api.search('taxes', filter='[name]=%[5]%', limit='3')

            for rec in recs:
                pprint(rec)

            # Create binary (product image)
            await api.create_binary('images/products/22', 'img.jpeg', 'image')

        if __name__ == "__main__":
            asyncio.run(main())

    """
    client: ClientSession = None
    debug = False
    lang_index: Optional[int] = 1
    data_format:str = 'JSON'
    ps_version = ''
    API_DOMAIN:str = None
    API_KEY:str = None
```

**Описание**: Асинхронный класс для взаимодействия с API PrestaShop с использованием JSON и XML.

**Атрибуты**:
- `client` (ClientSession): Асинхронный HTTP-клиент для выполнения запросов.
- `debug` (bool): Флаг для включения/выключения режима отладки.
- `lang_index` (Optional[int]): Индекс языка по умолчанию.
- `data_format` (str): Формат данных по умолчанию ('JSON' или 'XML').
- `ps_version` (str): Версия PrestaShop.
- `API_DOMAIN` (str): Домен API PrestaShop.
- `API_KEY` (str): Ключ API PrestaShop.

**Методы**:
- `__init__`: Инициализирует класс `PrestaShopAsync`.
- `ping`: Проверяет работоспособность веб-сервиса асинхронно.
- `_check_response`: Проверяет код состояния ответа и обрабатывает ошибки асинхронно.
- `_parse_response_error`: Разбирает ответ об ошибке от API PrestaShop асинхронно.
- `_prepare`: Подготавливает URL для запроса.
- `_exec`: Выполняет HTTP-запрос к API PrestaShop асинхронно.
- `_parse`: Разбирает XML или JSON ответ от API асинхронно.
- `create`: Создает новый ресурс в API PrestaShop асинхронно.
- `read`: Читает ресурс из API PrestaShop асинхронно.
- `write`: Обновляет существующий ресурс в API PrestaShop асинхронно.
- `unlink`: Удаляет ресурс из API PrestaShop асинхронно.
- `search`: Ищет ресурсы в API PrestaShop асинхронно.
- `create_binary`: Загружает бинарный файл в ресурс API PrestaShop асинхронно.
- `_save`: Сохраняет данные в файл.
- `get_data`: Получает данные из ресурса API PrestaShop и сохраняет их асинхронно.
- `remove_file`: Удаляет файл из файловой системы.
- `get_apis`: Получает список всех доступных API асинхронно.
- `get_languages_schema`: Получает схему для языков асинхронно.
- `upload_image_async`: Загружает изображение в API PrestaShop асинхронно.
- `upload_image`: Загружает изображение в API PrestaShop асинхронно.
- `get_product_images`: Получает изображения для продукта асинхронно.

## Функции

### `__init__`

```python
def __init__(self,
                api_domain:str,
                api_key:str,
                data_format: str = 'JSON',
                debug: bool = True) -> None:
    """! Initialize the PrestaShopAsync class.

    Args:
        data_format (str, optional): Default data format ('JSON' or 'XML'). Defaults to 'JSON'.
        default_lang (int, optional): Default language ID. Defaults to 1.
        debug (bool, optional): Activate debug mode. Defaults to True.

    Raises:
        PrestaShopAuthenticationError: When the API key is wrong or does not exist.
        PrestaShopException: For generic PrestaShop WebServices errors.
    """
    self.API_DOMAIN = api_domain
    self.API_KEY = api_key
    self.debug = debug
    self.data_format = data_format

    self.client = ClientSession(
        auth=aiohttp.BasicAuth(self.API_KEY, ''),
        timeout=ClientTimeout(total=60)
    )
```

**Назначение**: Инициализация класса `PrestaShopAsync`.

**Параметры**:
- `api_domain` (str): Домен API PrestaShop.
- `api_key` (str): Ключ API PrestaShop.
- `data_format` (str, optional): Формат данных по умолчанию ('JSON' или 'XML'). По умолчанию 'JSON'.
- `debug` (bool, optional): Активирует режим отладки. По умолчанию `True`.

**Вызывает исключения**:
- `PrestaShopAuthenticationError`: Если ключ API неверный или не существует.
- `PrestaShopException`: Для общих ошибок веб-сервисов PrestaShop.

**Как работает функция**:
1. Присваивает значения атрибутам экземпляра класса из переданных аргументов.
2. Инициализирует асинхронный HTTP-клиент `ClientSession` с использованием переданного API-ключа для аутентификации и устанавливает таймаут для запросов.

```
A: Инициализация атрибутов класса
|
-- B: Инициализация асинхронного HTTP-клиента
```

**Примеры**:

```python
api = PrestaShopAsync(api_domain='https://your-prestashop-domain.com', api_key='your_api_key', data_format='JSON', debug=True)
```

### `ping`

```python
async def ping(self) -> bool:
    """! Test if the webservice is working perfectly asynchronously.

    Returns:
        bool: Result of the ping test. Returns `True` if the webservice is working, otherwise `False`.
    """
    async with self.client.request(
        method='HEAD',
        url=self.API_DOMAIN
    ) as response:
        return await self._check_response(response.status, response)
```

**Назначение**: Проверка работоспособности веб-сервиса PrestaShop асинхронно.

**Возвращает**:
- `bool`: Результат проверки связи. Возвращает `True`, если веб-сервис работает, иначе `False`.

**Как работает функция**:
1. Выполняет HEAD-запрос к API_DOMAIN, используя асинхронный HTTP-клиент.
2. Передает код ответа и объект ответа в метод `_check_response` для проверки.

```
A: Выполнение HEAD-запроса к API_DOMAIN
|
-- B: Проверка ответа с помощью _check_response
```

**Примеры**:

```python
async def main():
    api = PrestaShopAsync(api_domain='https://your-prestashop-domain.com', api_key='your_api_key')
    result = await api.ping()
    print(f"Ping result: {result}")
```

### `_check_response`

```python
def _check_response(self, status_code: int, response, method: Optional[str] = None, url: Optional[str] = None,
                        headers: Optional[dict] = None, data: Optional[dict] = None) -> bool:
    """! Check the response status code and handle errors asynchronously.

    Args:
        status_code (int): HTTP response status code.
        response (aiohttp.ClientResponse): HTTP response object.
        method (str, optional): HTTP method used for the request.
        url (str, optional): The URL of the request.
        headers (dict, optional): The headers used in the request.
        data (dict, optional): The data sent in the request.

    Returns:
        bool: `True` if the status code is 200 or 201, otherwise `False`.
    """
    if status_code in (200, 201):
        return True
    else:
        self._parse_response_error(response, method, url, headers, data)
        return False
```

**Назначение**: Проверка кода состояния ответа и обработка ошибок асинхронно.

**Параметры**:
- `status_code` (int): Код состояния HTTP-ответа.
- `response` (aiohttp.ClientResponse): Объект HTTP-ответа.
- `method` (str, optional): HTTP-метод, использованный для запроса.
- `url` (str, optional): URL запроса.
- `headers` (dict, optional): Заголовки, использованные в запросе.
- `data` (dict, optional): Данные, отправленные в запросе.

**Возвращает**:
- `bool`: `True`, если код состояния 200 или 201, иначе `False`.

**Как работает функция**:
1. Проверяет, находится ли `status_code` в диапазоне (200, 201).
2. Если `status_code` не равен 200 или 201, вызывает метод `_parse_response_error` для обработки ошибки.

```
A: Проверка кода состояния HTTP-ответа
|
-- B: Обработка ошибки с помощью _parse_response_error (если status_code не равен 200 или 201)
```

**Примеры**:

```python
async def main():
    api = PrestaShopAsync(api_domain='https://your-prestashop-domain.com', api_key='your_api_key')
    async with aiohttp.ClientSession() as session:
        async with session.get(api.API_DOMAIN) as response:
            result = api._check_response(response.status, response)
            print(f"Check response result: {result}")
```

### `_parse_response_error`

```python
def _parse_response_error(self, response, method: Optional[str] = None, url: Optional[str] = None,
                              headers: Optional[dict] = None, data: Optional[dict] = None):
    """! Parse the error response from PrestaShop API asynchronously.

    Args:
        response (aiohttp.ClientResponse): HTTP response object from the server.
        method (str, optional): HTTP method used for the request.
        url (str, optional): The URL of the request.
        headers (dict, optional): The headers used in the request.
        data (dict, optional): The data sent in the request.
    """
    if self.data_format == 'JSON':
        status_code = response.status
        if not status_code in (200, 201):
            text = response.text()
            logger.critical(f"""response status code: {status_code}
                url: {response.request_info.url}
                --------------
                headers: {response.headers}
                --------------
                response text: {text}""")
        return response
    else:
        error_answer = self._parse(response.text())
        if isinstance(error_answer, dict):
            error_content = (error_answer
                             .get('PrestaShop', {})
                             .get('errors', {})
                             .get('error', {}))
            if isinstance(error_content, list):
                error_content = error_content[0]
            code = error_content.get('code')
            message = error_content.get('message')
        elif isinstance(error_answer, ElementTree.Element):
            error = error_answer.find('errors/error')
            code = error.find('code').text
            message = error.find('message').text
        logger.error(f'XML response error: {message} \n Code: {code}')
        return code, message
```

**Назначение**: Разбор ответа об ошибке от API PrestaShop асинхронно.

**Параметры**:
- `response` (aiohttp.ClientResponse): Объект HTTP-ответа от сервера.
- `method` (str, optional): HTTP-метод, использованный для запроса.
- `url` (str, optional): URL запроса.
- `headers` (dict, optional): Заголовки, использованные в запросе.
- `data` (dict, optional): Данные, отправленные в запросе.

**Как работает функция**:
1. Проверяет формат данных (`self.data_format`).
2. Если формат JSON, извлекает код состояния и текст ответа, затем логирует критическую информацию об ошибке.
3. Если формат XML, вызывает метод `_parse` для разбора XML-ответа, извлекает код и сообщение об ошибке, затем логирует ошибку.

```
A: Проверка формата данных (JSON или XML)
|
-- B1: Если JSON: Извлечение кода состояния и текста ответа, логирование информации об ошибке
|
-- B2: Если XML: Разбор XML-ответа с помощью _parse, извлечение кода и сообщения об ошибке, логирование ошибки
```

**Примеры**:

```python
async def main():
    api = PrestaShopAsync(api_domain='https://your-prestashop-domain.com', api_key='your_api_key')
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(f'{api.API_DOMAIN}/nonexistent_resource') as response:
                if response.status != 200:
                    api._parse_response_error(response)
        except Exception as ex:
            logger.error(f"Error: {ex}")
```

### `_prepare`

```python
def _prepare(self, url: str, params: dict) -> str:
    """! Prepare the URL for the request.

    Args:
        url (str): The base URL.
        params (dict): The parameters for the request.

    Returns:
        str: The prepared URL with parameters.
    """
    req = PreparedRequest()
    req.prepare_url(url, params)
    return req.url
```

**Назначение**: Подготовка URL для запроса.

**Параметры**:
- `url` (str): Базовый URL.
- `params` (dict): Параметры для запроса.

**Возвращает**:
- `str`: Подготовленный URL с параметрами.

**Как работает функция**:
1. Создает экземпляр `PreparedRequest`.
2. Подготавливает URL с использованием базового URL и параметров.

```
A: Создание экземпляра PreparedRequest
|
-- B: Подготовка URL с использованием базового URL и параметров
```

**Примеры**:

```python
api = PrestaShopAsync(api_domain='https://your-prestashop-domain.com', api_key='your_api_key')
url = api._prepare(api.API_DOMAIN, {'param1': 'value1', 'param2': 'value2'})
print(f"Prepared URL: {url}")
```

### `_exec`

```python
async def _exec(self,
              resource: str,
              resource_id: Optional[Union[int, str]] = None,
              resource_ids: Optional[Union[int, Tuple[int]]] = None,
              method: str = 'GET',
              data: Optional[dict] = None,
              headers: Optional[dict] = None,
              search_filter: Optional[Union[str, dict]] = None,
              display: Optional[Union[str, list]] = 'full',
              schema: Optional[str] = None,
              sort: Optional[str] = None,
              limit: Optional[str] = None,
              language: Optional[int] = None,
              io_format: str = 'JSON') -> Optional[dict]:
    """! Execute an HTTP request to the PrestaShop API asynchronously.

    Args:
        resource (str): The API resource (e.g., 'products', 'categories').
        resource_id (int | str, optional): The ID of the resource.
        resource_ids (int | tuple, optional): The IDs of multiple resources.
        method (str, optional): The HTTP method (GET, POST, PUT, DELETE).
        data (dict, optional): The data to be sent with the request.
        headers (dict, optional): Additional headers for the request.
        search_filter (str | dict, optional): Filter for the request.
        display (str | list, optional): Fields to display in the response.
        schema (str, optional): The schema of the data.
        sort (str, optional): Sorting parameter for the request.
        limit (str, optional): Limit of results for the request.
        language (int, optional): The language ID for the request.
        io_format (str, optional): The data format ('JSON' or 'XML').

    Returns:
        dict | None: The response from the API or `False` on failure.
    """
    self.debug = False
    if self.debug:
        # import sys
        # original_stderr = sys.stderr
        # f = open('stderr.log', 'w')
        # sys.stderr = f
        
        # prepared_url = self._prepare(f'{self.API_DOMAIN}/api/{resource}/{resource_id}' if resource_id else f'{self.API_DOMAIN}/api/{resource}',
        #                       {'filter': search_filter,
        #                        'display': display,
        #                        'schema': schema,
        #                        'sort': sort,
        #                        'limit': limit,
        #                        'language': language,
        #                        'output_format': io_format})
        
        # request_data = dict2xml(data) if data and io_format == 'XML' else data
        
        # with self.client.request(
        #     method=method,
        #     url=prepared_url,
        #     data=request_data,
        #     headers=headers,
        # ) as response:

        #     sys.stderr = original_stderr

        #     if not self._check_response(response.status, response, method, prepared_url, headers, request_data):
        #         return False

        #     if io_format == 'JSON':
        #         return response.json()
        #     else:
        #         return self._parse(await response.text())
        ...
    else:
        prepared_url = self._prepare(f'{self.API_DOMAIN}{resource}/{resource_id}' if resource_id else f'{self.API_DOMAIN}{resource}',
                              {'filter': search_filter,
                               'display': display,
                               'schema': schema,
                               'sort': sort,
                               'limit': limit,
                               'language': language,
                               'output_format': io_format})
        
        request_data = dict2xml(data) if data and io_format == 'XML' else data
        
        with self.client.request(
            method=method,
            url=prepared_url,
            data=request_data,
            headers=headers,
        ) as response:

            if not self._check_response(response.status, response, method, prepared_url, headers, request_data):
                return False

            if io_format == 'JSON':
                return response.json()
            else:
                return self._parse(await response.text())
```

**Назначение**: Выполнение HTTP-запроса к API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products', 'categories').
- `resource_id` (int | str, optional): ID ресурса.
- `resource_ids` (int | tuple, optional): ID нескольких ресурсов.
- `method` (str, optional): HTTP метод (GET, POST, PUT, DELETE).
- `data` (dict, optional): Данные для отправки с запросом.
- `headers` (dict, optional): Дополнительные заголовки для запроса.
- `search_filter` (str | dict, optional): Фильтр для запроса.
- `display` (str | list, optional): Поля для отображения в ответе.
- `schema` (str, optional): Схема данных.
- `sort` (str, optional): Параметр сортировки для запроса.
- `limit` (str, optional): Лимит результатов для запроса.
- `language` (int, optional): ID языка для запроса.
- `io_format` (str, optional): Формат данных ('JSON' или 'XML').

**Возвращает**:
- `dict | None`: Ответ от API или `False` в случае неудачи.

**Как работает функция**:
1. Устанавливает `self.debug = False`.
2. Подготавливает URL с использованием метода `_prepare`.
3. Преобразует данные в XML, если `data` предоставлены и `io_format == 'XML'`.
4. Выполняет HTTP-запрос с использованием асинхронного HTTP-клиента.
5. Проверяет ответ с использованием метода `_check_response`.
6. Разбирает ответ в формате JSON или XML.

```
A: Установка debug = False
|
-- B: Подготовка URL с использованием _prepare
|
-- C: Преобразование данных в XML (если необходимо)
|
-- D: Выполнение HTTP-запроса
|
-- E: Проверка ответа с использованием _check_response
|
-- F: Разбор ответа (JSON или XML)
```

**Примеры**:

```python
async def main():
    api = PrestaShopAsync(api_domain='https://your-prestashop-domain.com', api_key='your_api_key')
    data = await api._exec(resource='products', method='GET', limit='1')
    print(data)
```

### `_parse`

```python
def _parse(self, text: str) -> dict | ElementTree.Element | bool:
    """! Parse XML or JSON response from the API asynchronously.

    Args:
        text (str): Response text.

    Returns:
        dict | ElementTree.Element | bool: Parsed data or `False` on failure.
    """
    try:
        if self.data_format == 'JSON':
          data = j_loads(text)
          return data.get('PrestaShop', {}) if 'PrestaShop' in data else data
        else:
            tree = ElementTree.fromstring(text)
            return tree
    except (ExpatError, ValueError) as ex:
        logger.error(f'Parsing Error: {str(ex)}')
        return False
```

**Назначение**: Разбор XML или JSON ответа от API асинхронно.

**Параметры**:
- `text` (str): Текст ответа.

**Возвращает**:
- `dict | ElementTree.Element | bool`: Разобранные данные или `False` в случае неудачи.

**Как работает функция**:
1. Проверяет формат данных (`self.data_format`).
2. Если формат JSON, использует `j_loads` для разбора JSON и возвращает данные из ключа 'PrestaShop', если он существует.
3. Если формат XML, использует `ElementTree.fromstring` для разбора XML.
4. Обрабатывает исключения `ExpatError` и `ValueError` при разборе.

```
A: Проверка формата данных (JSON или XML)
|
-- B1: Если JSON: Разбор JSON с использованием j_loads
|
-- B2: Если XML: Разбор XML с использованием ElementTree.fromstring
|
-- C: Обработка исключений при разборе
```

**Примеры**:

```python
api = PrestaShopAsync(api_domain='https://your-prestashop-domain.com', api_key='your_api_key', data_format='JSON')
text = '{"PrestaShop": {"key": "value"}}'
data = api._parse(text)
print(data)
```

### `create`

```python
async def create(self, resource: str, data: dict) -> Optional[dict]:
    """! Create a new resource in PrestaShop API asynchronously.

    Args:
        resource (str): API resource (e.g., 'products').
        data (dict): Data for the new resource.

    Returns:
         dict: Response from the API.
    """
    return await self._exec(resource=resource, method='POST', data=data, io_format=self.data_format)
```

**Назначение**: Создание нового ресурса в API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `data` (dict): Данные для нового ресурса.

**Возвращает**:
- `dict`: Ответ от API.

**Как работает функция**:
1. Вызывает метод `_exec` с параметрами `resource`, `method='POST'`, `data` и `io_format=self.data_format`.

```
A: Вызов метода _exec с параметрами для создания ресурса
```

**Примеры**:

```python
async def main():
    api = PrestaShopAsync(api_domain='https://your-prestashop-domain.com', api_key='your_api_key')
    data = {'product': {'name': 'Test Product'}}
    response = await api.create(resource='products', data=data)
    print(response)
```

### `read`

```python
async def read(self, resource: str, resource_id: Union[int, str], **kwargs) -> Optional[dict]:
    """! Read a resource from the PrestaShop API asynchronously.

    Args:
        resource (str): API resource (e.g., 'products').
        resource_id (int | str): Resource ID.

    Returns:
        dict: Response from the API.
    """
    return await self._exec(resource=resource, resource_id=resource_id, method='GET', io_format= self.data_format)
```

**Назначение**: Чтение ресурса из API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `resource_id` (int | str): ID ресурса.

**Возвращает**:
- `dict`: Ответ от API.

**Как работает функция**:
1. Вызывает метод `_exec` с параметрами `resource`, `resource_id`, `method='GET'` и `io_format=self.data_format`.

```
A: Вызов метода _exec с параметрами для чтения ресурса
```

**Примеры**:

```python
async def main():
    api = PrestaShopAsync(api_domain='https://your-prestashop-domain.com', api_key='your_api_key')
    response = await api.read(resource='products', resource_id=1)
    print(response)
```

### `write`

```python
async def write(self, resource: str, data: dict) -> Optional[dict]:
    """! Update an existing resource in the PrestaShop API asynchronously.

    Args:
        resource (str): API resource (e.g., 'products').
        data (dict): Data for the resource.

    Returns:
        dict: Response from the API.
    """
    return await self._exec(resource=resource, resource_id=data.get('id'), method='PUT', data=data,
                          io_format=self.data_format)
```

**Назначение**: Обновление существующего ресурса в API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `data` (dict): Данные для ресурса.

**Возвращает**:
- `dict`: Ответ от API.

**Как работает функция**:
1. Вызывает метод `_exec` с параметрами `resource`, `resource_id=data.get('id')`, `method='PUT'`, `data` и `io_format=self.data_format`.

```
A: Вызов метода _exec с параметрами для обновления ресурса
```

**Примеры**:

```python
async def main():
    api = PrestaShopAsync(api_domain='https://your-prestashop-domain.com', api_key='your_api_key')
    data = {'id': 1, 'product': {'name': 'Updated Product'}}
    response = await api.write(resource='products', data=data)
    print(response)
```

### `unlink`

```python
async def unlink(self, resource: str, resource_id: Union[int, str]) -> bool:
    """! Delete a resource from the PrestaShop API asynchronously.

    Args:
        resource (str): API resource (e.g., 'products').
        resource_id (int | str): Resource ID.

    Returns:
        bool: `True` if successful, `False` otherwise.
    """
    return await self._exec(resource=resource, resource_id=resource_id, method='DELETE', io_format=self.data_format)
```

**Назначение**: Удаление ресурса из API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `resource_id` (int | str): ID ресурса.

**Возвращает**:
- `bool`: `True`, если успешно, `False` иначе.

**Как работает функция**:
1. Вызывает метод `_exec` с параметрами `resource`, `resource_id`, `method='DELETE'` и `io_format=self.data_format`.

```
A: Вызов метода _exec с параметрами для удаления ресурса
```

**Примеры**:

```python
async def main():
    api = PrestaShopAsync(api_domain='https://your-prestashop-domain.com', api_key='your_api_key')
    response = await api.unlink(resource='products', resource_id=1)
    print(response)
```

### `search`

```python
async def search(self, resource: str, filter: Optional[Union[str, dict]] = None, **kwargs) -> List[dict]:
    """! Search for resources in the PrestaShop API asynchronously.

    Args:
        resource (str): API resource (e.g., 'products').
        filter (str | dict, optional): Filter for the search.

    Returns:
         List[dict]: List of resources matching the search criteria.
    """
    return await self._exec(resource=resource, search_filter=filter, method='GET', io_format=self.data_format, **kwargs)
```

**Назначение**: Поиск ресурсов в API PrestaShop асинхронно.

**Параметры**:
- `resource` (str): API ресурс (например, 'products').
- `filter` (str | dict, optional): Фильтр для поиска.

**Возвращает**:
- `List[dict]`: Список ресурсов, соответствующих критериям поиска.

**Как работает функция**:
1. Вызывает метод `_exec` с параметрами `resource`, `search_filter=filter`, `method='GET'`, `io_format=self.data_format` и `**kwargs`.

```
A: Вызов метода _exec с параметрами для поиска ресурсов
```

**Примеры**:

```python
async def main():
    api = PrestaShopAsync(api_domain='https://your-prestashop-domain.com', api_key='your_api_key')
    response = await api.search(resource='products',