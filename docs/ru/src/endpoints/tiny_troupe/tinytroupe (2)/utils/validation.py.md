# Модуль для валидации данных

## Обзор

Модуль предоставляет набор функций для валидации и очистки данных, в частности, для проверки допустимости полей в словарях и для очистки строк от недопустимых символов. Эти функции предназначены для обеспечения безопасности и корректности обрабатываемых данных.

## Подробней

Этот модуль содержит функции для проверки структуры данных и очистки строковых значений. Валидация данных важна для предотвращения ошибок и обеспечения безопасности приложения. Санитизация строк помогает избежать проблем, связанных с некорректными или вредоносными символами.

## Функции

### `check_valid_fields`

```python
def check_valid_fields(obj: dict, valid_fields: list) -> None:
    """
    Checks whether the fields in the specified dict are valid, according to the list of valid fields. If not, raises a ValueError.
    """
```

**Назначение**: Проверяет, все ли поля в словаре `obj` допустимы, сравнивая их с перечнем допустимых полей `valid_fields`.

**Параметры**:
- `obj` (dict): Словарь, поля которого необходимо проверить.
- `valid_fields` (list): Список допустимых полей.

**Возвращает**:
- `None`: Функция ничего не возвращает. Если обнаружено недопустимое поле, она вызывает исключение `ValueError`.

**Вызывает исключения**:
- `ValueError`: Вызывается, если в словаре `obj` обнаружено поле, отсутствующее в списке `valid_fields`.

**Как работает функция**:
Функция перебирает все ключи в словаре `obj` и проверяет, содержится ли каждый ключ в списке `valid_fields`. Если какой-либо ключ отсутствует в списке допустимых полей, функция немедленно вызывает исключение `ValueError` с информативным сообщением об ошибке.

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

**Назначение**: Очищает входную строку `value`, удаляя недопустимые символы и обрезая ее до максимальной длины, допустимой в Python.

**Параметры**:
- `value` (str): Строка, которую необходимо очистить.

**Возвращает**:
- `str`: Очищенная строка.

**Как работает функция**:
1. **Удаление недопустимых символов**: Строка кодируется в формат UTF-8 с игнорированием ошибок, а затем декодируется обратно. Это позволяет удалить все недопустимые символы.
2. **Нормализация Unicode**: Строка нормализуется с использованием формы NFC, что обеспечивает консистентность представления символов Unicode.
3. **Ограничение длины**: Строка обрезается до максимальной длины, допустимой в Python (`sys.maxsize`), чтобы избежать потенциальных проблем с безопасностью и обработкой очень длинных строк.

**Примеры**:

```python
string_to_sanitize = "Hëllo, wørld! 😊"
sanitized_string = sanitize_raw_string(string_to_sanitize)
print(sanitized_string)  # Вывод: Hello, world! 😊

long_string = "A" * (sys.maxsize + 100)
sanitized_long_string = sanitize_raw_string(long_string)
print(len(sanitized_long_string))  # Вывод: 9223372036854775807 (или другое значение sys.maxsize)
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

**Назначение**: Очищает значения в словаре `value`, применяя функцию `sanitize_raw_string` ко всем строковым значениям.

**Параметры**:
- `value` (dict): Словарь, значения которого необходимо очистить.

**Возвращает**:
- `dict`: Очищенный словарь.

**Как работает функция**:
Функция перебирает все пары ключ-значение в словаре `value`. Если значение является строкой, к нему применяется функция `sanitize_raw_string` для удаления недопустимых символов и ограничения длины.

**Примеры**:

```python
dict_to_sanitize = {
    "name": "Jöhn Döe",
    "city": "Nëw Yørk",
    "age": 30
}
sanitized_dict = sanitize_dict(dict_to_sanitize)
print(sanitized_dict)  # Вывод: {'name': 'John Doe', 'city': 'New York', 'age': 30}