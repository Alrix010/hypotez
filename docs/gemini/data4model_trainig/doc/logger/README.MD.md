### Анализ кода модуля `src/logger/README.MD`

## Обзор

Этот модуль предоставляет гибкую систему логирования, поддерживающую логирование в консоль, файлы и JSON. Он использует паттерн Singleton, чтобы гарантировать использование только одного экземпляра логгера во всем приложении. Логгер поддерживает различные уровни логирования (например, `INFO`, `ERROR`, `DEBUG`) и включает цветной вывод для консольных логов. Вы можете также настраивать форматы вывода логов и управлять логированием в различные файлы.

## Подробнее

Модуль содержит классы и функции, необходимые для создания и настройки логгера. Ключевые компоненты включают:\

*   `SingletonMeta`: Метакласс для реализации паттерна Singleton.
*   `JsonFormatter`: Пользовательский форматтер для вывода логов в формате JSON.
*   `Logger`: Основной класс логгера, который обеспечивает логирование в консоль и файлы.

## Классы

### `SingletonMeta`

**Описание**: Метакласс, реализующий паттерн Singleton для логгера.

**Атрибуты**:
- Нет

**Методы**:
- Нет

### `JsonFormatter`

**Описание**: Пользовательский форматтер для вывода логов в формате JSON.

**Атрибуты**:
- Нет

**Методы**:
- `format(record)`: Форматирует запись лога в JSON.

### `Logger`

**Описание**: Основной класс логгера, поддерживающий логирование в консоль, файлы и JSON.

**Атрибуты**:
- Нет

**Методы**:
- `__init__`: Инициализирует логгер с настройками по умолчанию.
- `_configure_logger`: Настраивает и возвращает экземпляр логгера.
- `initialize_loggers`: Инициализирует логгеры для консоли и файлового вывода (info, debug, error и JSON).
- `log`: Записывает сообщение на указанном уровне с дополнительным форматированием.
- `info`: Записывает информационное сообщение.
- `success`: Записывает сообщение об успехе.
- `warning`: Записывает предупреждающее сообщение.
- `debug`: Записывает отладочное сообщение.
- `error`: Записывает сообщение об ошибке.
- `critical`: Записывает критическое сообщение.

## Функции

### `_configure_logger`

```python
#### `_configure_logger(name: str, log_path: str, level: Optional[int] = logging.DEBUG, formatter: Optional[logging.Formatter] = None, mode: Optional[str] = 'a') -> logging.Logger`
Configures and returns a logger instance.

**Parameters:**
- `name`: Name of the logger.
- `log_path`: Path to the log file.
- `level`: Logging level, e.g., `logging.DEBUG`. Default is `logging.DEBUG`.
- `formatter`: Custom formatter (optional).
- `mode`: File mode, e.g., `'a'` for append (default).

**Returns**: Configured `logging.Logger` instance.
```

**Назначение**:
Настраивает и возвращает экземпляр логгера.

**Параметры**:

-   `name` (str): Имя логгера.
-   `log_path` (str): Путь к файлу лога.
-   `level` (Optional[int]): Уровень логирования, например, `logging.DEBUG`. По умолчанию `logging.DEBUG`.
-   `formatter` (Optional[logging.Formatter]): Пользовательский форматтер (необязательно).
-   `mode` (Optional[str]): Режим файла, например, `'a'` для добавления (по умолчанию).

**Возвращает**:
-   `logging.Logger`: Настроенный экземпляр `logging.Logger`.

**Как работает функция**:
Устанавливает уровень логирования, форматтер и режим записи в файл для переданного логгера

### `initialize_loggers`

```python
#### `initialize_loggers(info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '', errors_log_path: Optional[str] = '', json_log_path: Optional[str] = '')`
Initializes the loggers for console and file logging (info, debug, error, and JSON).

**Parameters:**
- `info_log_path`: Path for info log file (optional).
- `debug_log_path`: Path for debug log file (optional).
- `errors_log_path`: Path for error log file (optional).
- `json_log_path`: Path for JSON log file (optional).
```

**Назначение**:
Инициализирует логгеры для консольного и файлового логирования (информация, отладка, ошибка и JSON).

**Параметры**:

-   `info_log_path` (Optional[str]): Путь к файлу журнала информации (необязательно).
-   `debug_log_path` (Optional[str]): Путь к файлу журнала отладки (необязательно).
-   `errors_log_path` (Optional[str]): Путь к файлу журнала ошибок (необязательно).
-   `json_log_path` (Optional[str]): Путь к файлу журнала JSON (необязательно).

**Возвращает**:
- Нет

**Как работает функция**:
Функция создает все необходимые логгеры и определяет пути к ним.
### `log`

```python
#### `log(level, message, ex=None, exc_info=False, color=None)`
Logs a message at the specified level (e.g., `INFO`, `DEBUG`, `ERROR`) with optional exception and color formatting.

**Parameters:**
- `level`: Logging level (e.g., `logging.INFO`, `logging.DEBUG`).
- `message`: The log message.
- `ex`: Optional exception to log.
- `exc_info`: Whether to include exception information (default is `False`).
- `color`: Tuple with text and background colors for console output (optional).
```

**Назначение**:
Записывает сообщение на указанном уровне (например, `INFO`, `DEBUG`, `ERROR`) с дополнительным форматированием исключений и цветов.

**Параметры**:

-   `level`: Уровень логирования (например, `logging.INFO`, `logging.DEBUG`).
-   `message`: Сообщение журнала.
-   `ex`: Необязательное исключение для записи в журнал.
-   `exc_info`: Следует ли включать информацию об исключении (по умолчанию `False`).
-   `color`: Кортеж с цветом текста и фона для вывода в консоль (необязательно).

**Возвращает**:
- Нет

**Как работает функция**:
Форматирует сообщение лога и записывает его в консоль.

### `info`

```python
#### `info(message, ex=None, exc_info=False, colors: Optional[tuple] = None)`
Logs an info message.

**Parameters**:\
- `message`: The info message to log.\
- `ex`: Optional exception to log.\
- `exc_info`: Whether to include exception info (default is `False`).\
- `colors`: Tuple of color values for the message (optional).
```

**Назначение**:
Записывает информационное сообщение.

**Параметры**:

-   `message`: Информационное сообщение для записи в журнал.
-   `ex`: Необязательное исключение для записи в журнал.
-   `exc_info`: Следует ли включать информацию об исключении (по умолчанию `False`).
-   `colors`: Кортеж значений цвета для сообщения (необязательно).

**Возвращает**:
- Нет

**Как работает функция**:
Вызывает функцию `log` с уровнем логирования `logging.INFO`.

### `success`

```python
#### `success(message, ex=None, exc_info=False, colors: Optional[tuple] = None)`
Logs a success message.

**Parameters**:\
- Same as `info`.
```

**Назначение**:
Записывает сообщение об успехе.

**Параметры**:

-   `message`: Сообщение об успехе для записи в журнал.
-   `ex`: Необязательное исключение для записи в журнал.
-   `exc_info`: Следует ли включать информацию об исключении (по умолчанию `False`).
-   `colors`: Кортеж значений цвета для сообщения (необязательно).

**Возвращает**:
- Нет

**Как работает функция**:
Вызывает функцию `log` с уровнем логирования `logging.INFO`.

### `warning`

```python
#### `warning(message, ex=None, exc_info=False, colors: Optional[tuple] = None)`
Logs a warning message.

**Parameters**:\
- Same as `info`.
```

**Назначение**:
Записывает предупреждающее сообщение.

**Параметры**:

-   `message`: Предупреждающее сообщение для записи в журнал.
-   `ex`: Необязательное исключение для записи в журнал.
-   `exc_info`: Следует ли включать информацию об исключении (по умолчанию `False`).
-   `colors`: Кортеж значений цвета для сообщения (необязательно).

**Возвращает**:
- Нет

**Как работает функция**:
Вызывает функцию `log` с уровнем логирования `logging.WARNING`.

### `debug`

```python
#### `debug(message, ex=None, exc_info=True, colors: Optional[tuple] = None)`
Logs a debug message.

**Parameters**:\
- Same as `info`.
```

**Назначение**:
Записывает отладочное сообщение.

**Параметры**:

-   `message`: Отладочное сообщение для записи в журнал.
-   `ex`: Необязательное исключение для записи в журнал.
-   `exc_info`: Следует ли включать информацию об исключении (по умолчанию `True`).
-   `colors`: Кортеж значений цвета для сообщения (необязательно).

**Возвращает**:
- Нет

**Как работает функция**:
Вызывает функцию `log` с уровнем логирования `logging.DEBUG`.

### `error`

```python
#### `error(message, ex=None, exc_info=True, colors: Optional[tuple] = None)`
Logs an error message.

**Parameters**:\
- Same as `info`.
```

**Назначение**:
Записывает сообщение об ошибке.

**Параметры**:

-   `message`: Сообщение об ошибке для записи в журнал.
-   `ex`: Необязательное исключение для записи в журнал.
-   `exc_info`: Следует ли включать информацию об исключении (по умолчанию `True`).
-   `colors`: Кортеж значений цвета для сообщения (необязательно).

**Возвращает**:
- Нет

**Как работает функция**:
Вызывает функцию `log` с уровнем логирования `logging.ERROR`.

### `critical`

```python
#### `critical(message, ex=None, exc_info=True, colors: Optional[tuple] = None)`
Logs a critical message.

**Parameters**:\
- Same as `info`.
```

**Назначение**:
Записывает критическое сообщение.

**Параметры**:

-   `message`: Критическое сообщение для записи в журнал.
-   `ex`: Необязательное исключение для записи в журнал.
-   `exc_info`: Следует ли включать информацию об исключении (по умолчанию `True`).
-   `colors`: Кортеж значений цвета для сообщения (необязательно).

**Возвращает**:
- Нет

**Как работает функция**:
Вызывает функцию `log` с уровнем логирования `logging.CRITICAL`.

## Переменные

### `TEXT_COLORS`

```python
TEXT_COLORS = {
    "black": colorama.Fore.BLACK,
    "red": colorama.Fore.RED,
    "green": colorama.Fore.GREEN,
    "yellow": colorama.Fore.YELLOW,
    "blue": colorama.Fore.BLUE,
    "magenta": colorama.Fore.MAGENTA,
    "cyan": colorama.Fore.CYAN,
    "white": colorama.Fore.WHITE,
    "light_gray": colorama.Fore.LIGHTBLACK_EX,
    "light_red": colorama.Fore.LIGHTRED_EX,
    "light_green": colorama.Fore.LIGHTGREEN_EX,
    "light_yellow": colorama.Fore.LIGHTYELLOW_EX,
    "light_blue": colorama.Fore.LIGHTBLUE_EX,
    "light_magenta": colorama.Fore.LIGHTMAGENTA_EX,
    "light_cyan": colorama.Fore.LIGHTCYAN_EX,
}
```

Словарь, содержащий соответствия между названиями цветов текста и значениями из модуля `colorama`.

### `BG_COLORS`

```python
BG_COLORS = {
    "black": colorama.Back.BLACK,
    "red": colorama.Back.RED,
    "green": colorama.Back.GREEN,
    "yellow": colorama.Back.YELLOW,
    "blue": colorama.Back.BLUE,
    "magenta": colorama.Back.MAGENTA,
    "cyan": colorama.Back.CYAN,
    "white": colorama.Back.WHITE,
    "light_gray": colorama.Back.LIGHTBLACK_EX,
    "light_red": colorama.Back.LIGHTRED_EX,
    "light_green": colorama.Back.LIGHTGREEN_EX,
    "light_yellow": colorama.Back.LIGHTYELLOW_EX,
    "light_blue": colorama.Back.LIGHTBLUE_EX,
    "light_magenta": colorama.Back.LIGHTMAGENTA_EX,
    "light_cyan": colorama.Back.LIGHTCYAN_EX,
}
```

Словарь, содержащий соответствия между названиями цветов фона и значениями из модуля `colorama`.

### `LOG_SYMBOLS`

```python
LOG_SYMBOLS = {
    logging.INFO: "ℹ️",  # Information
    logging.WARNING: "⚠️",  # Warning
    logging.ERROR: "❌",  # Error
    logging.CRITICAL: "🔥",  # Critical
    logging.DEBUG: "🐛",  # Debug
    "EXCEPTION": "🚨",  # Exception
    "SUCCESS": "✅" # Success
}
```

Словарь, содержащий соответствия между уровнями логирования и символами для их отображения.

### `logger`

```python
logger: Logger = Logger()
```

Экземпляр класса `Logger`, используемый для логирования сообщений.

## Запуск

Этот модуль предназначен для использования в других частях проекта `hypotez`. Для логирования сообщений необходимо импортировать объект `logger` из модуля `src.logger.logger` и использовать его методы (`info`, `debug`, `warning`, `error`, `critical`, `exception`).

```python
from src.logger.logger import logger

logger.info("This is an information message")
logger.error("This is an error message", ex, exc_info=True)