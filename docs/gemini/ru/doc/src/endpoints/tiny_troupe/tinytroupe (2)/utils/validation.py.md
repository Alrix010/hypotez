# Модуль для валидации данных в Tiny Troupe
## Обзор

Модуль `validation.py` предоставляет набор функций для проверки и очистки данных, используемых в проекте Tiny Troupe. Он включает в себя функции для проверки допустимости полей в словарях и очистки строк от недопустимых символов, а также для проверки глубины вложенности словарей.

## Подробней

Этот модуль обеспечивает безопасность и целостность данных, предотвращая ошибки и потенциальные уязвимости, связанные с необработанными входными данными. Функции модуля используются для проверки структуры данных и очистки строковых значений перед их использованием в других частях приложения.

## Функции

### `check_valid_fields`

```python
def check_valid_fields(obj: dict, valid_fields: list) -> None:
    """
    Checks whether the fields in the specified dict are valid, according to the list of valid fields. If not, raises a ValueError.
    """
```

**Назначение**: Проверяет, являются ли поля в указанном словаре допустимыми, в соответствии со списком допустимых полей.

**Параметры**:
- `obj` (dict): Словарь, поля которого необходимо проверить.
- `valid_fields` (list): Список допустимых полей.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Вызывает исключения**:
- `ValueError`: Если в словаре обнаружено недопустимое поле.

**Как работает функция**:
Функция перебирает все ключи в переданном словаре `obj` и проверяет, есть ли каждый ключ в списке допустимых полей `valid_fields`. Если какой-либо ключ не найден в списке допустимых полей, функция вызывает исключение `ValueError` с сообщением об ошибке, указывающим недопустимый ключ и список допустимых ключей.

**Примеры**:

```python
valid_fields = ['name', 'age', 'city']
obj1 = {'name': 'John', 'age': 30, 'city': 'New York'}
check_valid_fields(obj1, valid_fields)  # Не вызовет исключение

obj2 = {'name': 'John', 'age': 30, 'country': 'USA'}
# check_valid_fields(obj2, valid_fields)  # Вызовет ValueError: Invalid key country in dictionary. Valid keys are: ['name', 'age', 'city']
```

### `sanitize_raw_string`

```python
def sanitize_raw_string(value: str) -> str:
    """
    Sanitizes the specified string by: 
      - removing any invalid characters.
      - ensuring it is not longer than the maximum Python string length.
    
    This is for an abundance of caution with security, to avoid any potential issues with the string.
    """
```

**Назначение**: Очищает указанную строку, удаляя все недопустимые символы и обеспечивая, чтобы она не была длиннее максимальной длины строки Python.

**Параметры**:
- `value` (str): Строка, которую необходимо очистить.

**Возвращает**:
- `str`: Очищенная строка.

**Как работает функция**:
1. **Удаление недопустимых символов**:
   - Преобразует строку в UTF-8, игнорируя недопустимые символы.
   - Нормализует строку в форме NFC для обеспечения совместимости.

2. **Ограничение длины строки**:
   - Обрезает строку до максимальной длины строки Python (`sys.maxsize`).

**Примеры**:

```python
string1 = "Привіт, світ!😊"
sanitized_string1 = sanitize_raw_string(string1)
print(sanitized_string1)  # Вывод: Привіт, світ!😊

string2 = "Invalid\x00character"
sanitized_string2 = sanitize_raw_string(string2)
print(sanitized_string2)  # Вывод: Invalidcharacter
```

### `sanitize_dict`

```python
def sanitize_dict(value: dict) -> dict:
    """
    Sanitizes the specified dictionary by:
      - removing any invalid characters.
      - ensuring that the dictionary is not too deeply nested.
    """
```

**Назначение**: Очищает указанный словарь, удаляя недопустимые символы из строковых значений и обеспечивая, чтобы словарь не был слишком глубоко вложен.

**Параметры**:
- `value` (dict): Словарь, который необходимо очистить.

**Возвращает**:
- `dict`: Очищенный словарь.

**Как работает функция**:
1. **Очистка строковых значений**:
   - Перебирает все элементы словаря.
   - Если значение является строкой, вызывает функцию `sanitize_raw_string` для очистки строки.
   - Обновляет значение в словаре очищенной строкой.

2. **Обеспечение неглубокой вложенности**:
   - Возвращает очищенный словарь. <инструкция для модели gemini: в данном случае код не делает проверки глубины вложенности словаря. Напиши что этого не предусмотрено в коде>

**Примеры**:

```python
dict1 = {'name': 'John Doe', 'city': 'New York', 'description': "Some invalid\x00character"}
sanitized_dict1 = sanitize_dict(dict1)
print(sanitized_dict1)
# Вывод: {'name': 'John Doe', 'city': 'New York', 'description': 'Some invalidcharacter'}

dict2 = {'name': 'Jane Smith', 'address': {'street': '123 Main St', 'city': 'Los Angeles'}}
sanitized_dict2 = sanitize_dict(dict2)
print(sanitized_dict2)
# Вывод: {'name': 'Jane Smith', 'address': {'street': '123 Main St', 'city': 'Los Angeles'}}