## \file /src/utils/file.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
.. module:: src.utils.file 
	:platform: Windows, Unix
	:synopsis: read, wite, search text files

Модуль для работы с файлами.
=========================================================================================

Модуль содержит набор утилит для выполнения операций с файлами, таких как сохранение, чтение,
и получение списков файлов. Поддерживает обработку больших файлов с использованием генераторов
для экономии памяти.

Пример использования
--------------------

```python

    from pathlib import Path
    from src.utils.file import read_text_file, save_text_file

    file_path = Path('example.txt')
    content = read_text_file(file_path)
    if content:
        print(f'File content: {content[:100]}...')

    save_text_file(file_path, 'Новый текст')
```
"""
import os
import json
import fnmatch
import re
from pathlib import Path
from typing import List, Optional, Union, Generator, Iterator
from src.logger.logger import logger


def save_text_file(
    data: str | list[str] | dict,
    file_path: str | Path,
    mode: str = 'w'
) -> bool:
    """
    Сохраняет данные в текстовый файл.

    Args:
        file_path (str | Path): Путь к файлу для сохранения.
        data (str | list[str] | dict): Данные для записи. Могут быть строкой, списком строк или словарем.
        mode (str, optional): Режим записи файла ('w' для записи, 'a' для добавления).
    Returns:
        bool: `True`, если файл успешно сохранен, `False` в противном случае.
    Raises:
        Exception: При возникновении ошибки при записи в файл.

    Example:
        >>> from pathlib import Path
        >>> file_path = Path('example.txt')
        >>> data = 'Пример текста'
        >>> result = save_text_file(file_path, data)
        >>> print(result)
        True
    """
    try:
        file_path = Path(file_path)
        file_path.parent.mkdir(parents = True, exist_ok = True)

        with file_path.open(mode, encoding = 'utf-8') as file:
            if isinstance(data, list):
                file.writelines(f'{line}\n' for line in data)
            elif isinstance(data, dict):
                json.dump(data, file, ensure_ascii = False, indent = 4)
            else:
                file.write(data)
        return True
    except Exception as ex:
        logger.error(f'Ошибка при сохранении файла {file_path}.', ex)
        ...
        return False
    
def read_text_file_generator(
    file_path: str | Path,
    as_list: bool = False,
    extensions: Optional[list[str]] = None,
    chunk_size: int = 8192,
    recursive: bool = False,
    patterns: Optional[str | list[str]] = None,
) -> Generator[str, None, None] | str | list[str] | None:
    """
    Читает содержимое файла(ов) или директории.

        Args:
            file_path (str | Path): Путь к файлу или директории.
            as_list (bool, optional): Если `True`, то возвращает генератор строк или список строк, в зависимости от типа вывода.
            extensions (list[str], optional): Список расширений файлов для включения при чтении директории.
            chunk_size (int, optional): Размер чанка для чтения файла в байтах.
            recursive (bool, optional): Если `True`, то поиск файлов выполняется рекурсивно.
            patterns (str | list[str], optional): Шаблоны для фильтрации файлов при рекурсивном поиске.

        Returns:
            Generator[str, None, None] | str | list[str] | None:
            - Если `as_list` is True и `file_path` является файлом, возвращает генератор строк.
            - Если `as_list` is True и `file_path` является директорией и `recursive` is True, возвращает список строк.
            - Если `as_list` is False и `file_path` является файлом, возвращает строку.
            - Если `as_list` is False и `file_path` является директорией, возвращает объединенную строку.
            - Возвращает `None` в случае ошибки.
        Raises:
            Exception: При возникновении ошибки при чтении файла.

        Example:
            >>> from pathlib import Path
            >>> file_path = Path('example.txt')
            >>> content = read_text_file(file_path)
            >>> if content:
            ...    print(f'File content: {content[:100]}...')
            File content: Пример текста...
    Функция read_text_file может возвращать несколько разных типов данных в зависимости от входных параметров:

    Возвращаемые значения:
    ----------------------

    - Generator[str, None, None] (Генератор строк):
        Генератор при итерации выдаёт строки из файла(ов) по одной. Эффективно для работы с большими файлами, так как они не загружаются полностью в память.
        - Когда:
            file_path – это файл и as_list равен True.
            file_path – это директория, recursive равен True и as_list равен True. При этом в генератор попадают строки из всех найденных файлов.
            file_path – это директория, recursive равен False и as_list равен True. При этом в генератор попадают строки из всех найденных файлов в текущей директории.
        
    - str (Строка):
        Содержимое файла или объединенное содержимое всех файлов в виде одной строки.
        - Когда:
            file_path – это файл и as_list равен False.
            file_path – это директория, recursive равен False и as_list равен False. При этом возвращается объединенная строка, состоящая из содержимого всех файлов в директории, разделенных символами новой строки (\n).
            file_path – это директория, recursive равен True и as_list равен False. При этом возвращается объединенная строка, состоящая из содержимого всех файлов в директории и её поддиректориях, разделенных символами новой строки (\n).
 
    - list[str] (Список строк):
        Этот тип явно не возвращается функцией, однако когда file_path – это директория, recursive равен True и as_list равен True - функция возвращает генератор, который можно преобразовать в список при помощи list()
        - Когда:
            file_path – не является ни файлом, ни директорией.
            Произошла ошибка при чтении файла или директории (например, файл не найден, ошибка доступа и т.п.).


    Note:
        Если вы хотите прочитать содержимое файла построчно (особенно для больших файлов) используйте as_list = True. В этом случае вы получите генератор строк.
        Если вы хотите получить всё содержимое файла в виде одной строки используйте as_list = False.
        Если вы работаете с директорией, recursive = True будет обходить все поддиректории.
        extensions и patterns позволят вам фильтровать файлы при работе с директорией.
        chunk_size позволяет оптимизировать работу с большими файлами при чтении их по частям.
        None будет возвращён в случае ошибок.

    Важно помнить:
        В случае чтения директории, если as_list=False, функция объединяет все содержимое найденных файлов в одну строку. Это может потребовать много памяти, если файлов много или они большие.
        Функция полагается на другие функции-помощники (_read_file_lines_generator, _read_file_content, recursively_get_file_path, yield_text_from_files), которые здесь не определены и их поведение влияет на результат read_text_file.


    """
    try:
        path = Path(file_path)
        if path.is_file():
            if as_list:
                return _read_file_lines_generator(path, chunk_size = chunk_size)
            else:
                return _read_file_content(path, chunk_size = chunk_size)
        elif path.is_dir():
            if recursive:
                if patterns:
                    files = recursively_get_file_path(path, patterns)
                else:
                   files = [
                        p for p in path.rglob('*') if p.is_file() and (not extensions or p.suffix in extensions)
                    ]
                if as_list:
                    return (
                        line
                        for file in files
                        for line in yield_text_from_files(file, as_list = True, chunk_size = chunk_size)
                    )
                else:
                    return '\n'.join(filter(None, [read_text_file(p, chunk_size = chunk_size) for p in files]))
            else:
                files = [
                    p for p in path.iterdir() if p.is_file() and (not extensions or p.suffix in extensions)
                ]
                if as_list:
                    return (line for file in files for line in read_text_file(file, as_list = True, chunk_size = chunk_size) )
                else:
                    return '\n'.join(filter(None, [read_text_file(p, chunk_size = chunk_size) for p in files]))
        else:
            logger.error(f'Путь \'{file_path}\' не является файлом или директорией.')
            ...
            return None
    except Exception as ex:
        logger.error(f'Ошибка при чтении файла/директории {file_path}.', ex)
        ...
        return None



def read_text_file(
    file_path: Union[str, Path],
    as_list: bool = False,
    extensions: Optional[List[str]] = None,
    exc_info: bool = True
) -> Union[str, List[str], None]:
    """
    Read the contents of a text file or all text files in a directory.

    Args:
        file_path (str | Path): Path to the file or directory.
        as_list (bool, optional):
            If True, returns content as a list of original lines.
            If False, returns content as a single string with whitespace
            collapsed to single spaces and double quotes escaped.
            Defaults to False.
        extensions (List[str], optional): List of file extensions to include
            when reading a directory (e.g., ['.txt', '.py']). The dot prefix
            is recommended but handled if missing. Defaults to None (include all files).
        exc_info (bool, optional): If True, logs traceback information on error.
            Defaults to True.

    Returns:
        str | List[str] | None: File content as a single processed string or a
                                 list of original lines. Returns None if the
                                 path is invalid or an error occurs during reading.
    """
    try:
        path = Path(file_path)

        # --- Handle Single File ---
        if path.is_file():
            # Optional: Check extension even for single files if desired
            # if extensions:
            #     processed_extensions = [ext if ext.startswith('.') else '.' + ext for ext in extensions]
            #     if path.suffix not in processed_extensions:
            #         logger.debug(f"Skipping file {path} due to extension mismatch.")
            #         return [] if as_list else "" # Or None? Consistent return type is important

            with path.open("r", encoding="utf-8") as f:
                # Read the entire file content first
                try:
                    raw_content = f.read()
                except Exception as ex:
                    logger.critical(f'Ошибка чтения содержимого файла {str(path)}')
                    return ''

            if as_list:
                # Return list of original lines
                return raw_content.splitlines()
            else:
                # Process the content for single string output
                # 1. Collapse whitespace (including newlines) to single spaces
                content = re.sub(r'\s+', ' ', raw_content)
                # 2. Escape double quotes
                content = content.replace('"', '\\"')
                return content

        # --- Handle Directory ---
        elif path.is_dir():
            processed_extensions = None
            if extensions:
                # Ensure extensions start with a dot for consistent suffix matching
                processed_extensions = [ext if ext.startswith('.') else '.' + ext for ext in extensions]

            # Find all matching files recursively
            files_to_read = [
                p for p in path.rglob("*")
                if p.is_file() and (not processed_extensions or p.suffix in processed_extensions)
            ]

            # Recursively read each file, passing the 'as_list' flag
            contents = [
                read_text_file(p, as_list=as_list, extensions=None, exc_info=exc_info)
                for p in files_to_read
            ] # Pass extensions=None in recursive call as files are already filtered

            if as_list:
                # Combine results: flatten the list of lists (of lines)
                # Filter out None values from failed reads before flattening
                flat_list = [item for sublist in contents if sublist is not None for item in sublist]
                return flat_list
            else:
                # Combine results: join the list of strings (processed file contents)
                # Filter out None values from failed reads before joining
                valid_contents = [c for c in contents if c is not None and isinstance(c, str)]
                return "\n".join(valid_contents)

        # --- Handle Invalid Path ---
        else:
            logger.warning(f"Path '{file_path}' is not a valid file or directory.")
            return None

    # --- Handle Exceptions ---
    except Exception as ex:
        # Log the error, optionally with traceback
        if exc_info:
            logger.exception(f"Failed to read path '{file_path}'. Error: {ex}") # logger.exception includes traceback
        else:
            logger.error(f"Failed to read path '{file_path}'. Error: {ex}")
        return None

def yield_text_from_files(
    file_path: str | Path,
    as_list: bool = False,
    chunk_size: int = 8192
) -> Generator[str, None, None] | str | None:
    """
    Читает содержимое файла и возвращает его в виде генератора строк или одной строки.

    Args:
        file_path (str | Path): Путь к файлу.
        as_list (bool, optional): Если True, возвращает генератор строк. По умолчанию False.
        chunk_size (int, optional): Размер чанка для чтения файла в байтах.

    Returns:
        Generator[str, None, None] | str | None: Генератор строк, объединенная строка или None в случае ошибки.

    Yields:
       str: Строки из файла, если as_list is True.

    Example:
        >>> from pathlib import Path
        >>> file_path = Path('example.txt')
        >>> for line in yield_text_from_files(file_path, as_list=True):
        ...     print(line)
        Первая строка файла
        Вторая строка файла
    """
    try:
        path = Path(file_path)
        if path.is_file():
            if as_list:
                 yield from  _read_file_lines_generator(path, chunk_size = chunk_size)
            else:
                yield _read_file_content(path, chunk_size = chunk_size)
        else:
             logger.error(f'Путь \'{file_path}\' не является файлом.')
             ...
             return None
    except Exception as ex:
        logger.error(f'Ошибка при чтении файла {file_path}.', ex)
        ...
        return None



# # -----------------------------------------------------------

# def _yield_files_content(
#     self,
#     process_directory: str | Path,
# ) -> Iterator[tuple[Path, str]]:
#     """
#     Генерирует пути файлов и их содержимое по указанным шаблонам.

#     Args:
#         process_directory (Path | str): Абсолютный путь к стартовой директории

#     Returns:
#         bool: Iterator
#     """

#     process_directory: Path = process_directory if isinstance(process_directory, Path) else Path(process_directory)

#     # Компиляция паттернов исключаемых файлов
#     try:
#         exclude_files_patterns = [
#             re.compile(pattern) for pattern in Config.exclude_files_patterns
#         ]

#     except Exception as ex:
#         logger.error(
#             f'Не удалось скомпилировать регулярки из списка:/n{Config.exclude_files_patterns=}\n ', ex
#         )
#         ...

#     # Итерация по всем файлам в директории
#     for file_path in process_directory.rglob('*'):
#         # Проверка на соответствие шаблонам включения
#         if not any(
#             fnmatch.fnmatch(file_path.name, pattern) for pattern in Config.include_files_patterns
#         ):
#             continue

#         # Прверка исключенных директорий
#         if any(exclude_dir in file_path.parts for exclude_dir in Config.exclude_dirs):
#             continue

#         # Проверка исключенных файлов по паттерну
#         if any(exclude.match(str(file_path.name)) for exclude in exclude_files_patterns):
#             continue

#         # Проверка конкретных исключенных файлов
#         if str(file_path.name) in Config.exclude_files:
#             continue

#         # Чтение содержимого файла
#         try:
#             content = file_path.read_text(encoding='utf-8')
#             yield file_path, content
#             # make_summary( docs_dir = start_dir.parent / 'docs' )  # <- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DEBUG  (create `summary.md`)
#         except Exception as ex:
#             logger.error(f'Ошибка при чтении файла {file_path}', ex)
#             ...
#             yield None, None

#         ...










def _read_file_content(file_path: Path, chunk_size: int) -> str:
    """
    Читает содержимое файла по чанкам и возвращает как строку.

    Args:
        file_path (Path): Путь к файлу для чтения.
        chunk_size (int): Размер чанка для чтения файла в байтах.
    Returns:
        str: Содержимое файла в виде строки.
    Raises:
        Exception: При возникновении ошибки при чтении файла.
    """
    with file_path.open('r', encoding = 'utf-8') as f:
        content = ''
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            content += chunk
        #Обработка согласно заданию
        content = re.sub(r'\s+', ' ', content)
        content = content.replace('"', '\\"')
        return content

def _read_file_lines_generator(file_path: Path, chunk_size: int) -> Generator[str, None, None]:
    """
    Читает файл по строкам с помощью генератора.

    Args:
        file_path (Path): Путь к файлу для чтения.
        chunk_size (int): Размер чанка для чтения файла в байтах.
    Yields:
        str: Строки из файла.
    Raises:
        Exception: При возникновении ошибки при чтении файла.
    """
    with file_path.open('r', encoding = 'utf-8') as f:
         while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                lines = chunk.splitlines()
                # Если чанк не закончился полной строкой, то последнюю строку добавляем к следующему чанку
                if len(lines)>0 and not chunk.endswith('\n'):
                     next_chunk = f.read(1)
                     if next_chunk != '':
                        lines[-1] = lines[-1] + next_chunk
                     else:
                        for line in lines:
                            #Обработка согласно заданию
                            line = re.sub(r'\s+', ' ', line)
                            line = line.replace('"', '\\"')
                            yield line
                        break
                
                for line in lines:
                    #Обработка согласно заданию
                    line = re.sub(r'\s+', ' ', line)
                    line = line.replace('"', '\\"')
                    yield line



def get_filenames_from_directory(
    directory: str | Path, ext: str | list[str] = '*'
) -> list[str]:
    """
    Возвращает список имен файлов в директории, опционально отфильтрованных по расширению.

    Args:
        directory (str | Path): Путь к директории для поиска.
        ext (str | list[str], optional): Расширения для фильтрации.
            По умолчанию '*'.

    Returns:
        list[str]: Список имен файлов, найденных в директории.

    Example:
        >>> from pathlib import Path
        >>> directory = Path('.')
        >>> get_filenames_from_directory(directory, ['.txt', '.md'])
        ['example.txt', 'readme.md']

    TODO:
        Сейчас не работает формат параметра `ext` переданный как `*.ext`, только `ext` 
    """
    if not Path(directory).is_dir():
        logger.error(f'Указанный путь \'{directory}\' не является директорией.')
        return []

    try:
        if isinstance(ext, str):
            extensions = [ext] if ext != '*' else []
        extensions = [e if e.startswith('.') else f'.{e}' for e in extensions]

        return [
            file.name
            for file in directory.iterdir()
            if file.is_file() and (not extensions or file.suffix in extensions)
        ]
    except Exception as ex:
        logger.error(f'Ошибка при получении списка имен файлов из \'{directory}\'.', ex)
        return []


def recursively_yield_file_path(
    root_dir: str | Path, patterns: str | list[str] = '*'
) -> Generator[Path, None, None]:
    """
    Рекурсивно возвращает пути ко всем файлам, соответствующим заданным шаблонам, в указанной директории.

    Args:
        root_dir (str | Path): Корневая директория для поиска.
        patterns (str | list[str]): Шаблоны для фильтрации файлов.

    Yields:
        Path: Путь к файлу, соответствующему шаблону.

    Example:
        >>> from pathlib import Path
        >>> root_dir = Path('.')
        >>> for path in recursively_yield_file_path(root_dir, ['*.txt', '*.md']):
        ...    print(path)
        ./example.txt
        ./readme.md
    """
    try:
        patterns = [patterns] if isinstance(patterns, str) else patterns
        for pattern in patterns:
            yield from Path(root_dir).rglob(pattern)
    except Exception as ex:
         logger.error(f'Ошибка при рекурсивном поиске файлов в \'{root_dir}\'.', ex)


def recursively_get_file_path(
    root_dir: str | Path,
    patterns: str | list[str] = '*'
) -> list[Path]:
    """
    Рекурсивно возвращает список путей ко всем файлам, соответствующим заданным шаблонам, в указанной директории.

    Args:
        root_dir (str | Path): Корневая директория для поиска.
        patterns (str | list[str]): Шаблоны для фильтрации файлов.

    Returns:
        list[Path]: Список путей к файлам, соответствующим шаблонам.

    Example:
        >>> from pathlib import Path
        >>> root_dir = Path('.')
        >>> paths = recursively_get_file_path(root_dir, ['*.txt', '*.md'])
        >>> print(paths)
        [Path('./example.txt'), Path('./readme.md')]
    """
    try:
        file_paths = []
        patterns = [patterns] if isinstance(patterns, str) else patterns
        for pattern in patterns:
            file_paths.extend(Path(root_dir).rglob(pattern))
        return file_paths
    except Exception as ex:
        logger.error(f'Ошибка при рекурсивном поиске файлов в \'{root_dir}\'.', ex)
        return []


def recursively_read_text_files(
    root_dir: str | Path,
    patterns: str | list[str],
    as_list: bool = False
) -> list[str]:
    """
    Рекурсивно читает текстовые файлы из указанной корневой директории, соответствующие заданным шаблонам.

    Args:
        root_dir (str | Path): Путь к корневой директории для поиска.
        patterns (str | list[str]): Шаблон(ы) имени файла для фильтрации.
             Может быть как одиночным шаблоном (например, '*.txt'), так и списком.
        as_list (bool, optional): Если True, то возвращает содержимое файла как список строк.
             По умолчанию `False`.

    Returns:
        list[str]: Список содержимого файлов (или список строк, если `as_list=True`),
         соответствующих заданным шаблонам.

    Example:
        >>> from pathlib import Path
        >>> root_dir = Path('.')
        >>> contents = recursively_read_text_files(root_dir, ['*.txt', '*.md'], as_list=True)
        >>> for line in contents:
        ...     print(line)
        Содержимое example.txt
        Первая строка readme.md
        Вторая строка readme.md
    """
    matches = []
    root_path = Path(root_dir)

    if not root_path.is_dir():
        logger.debug(f'Корневая директория \'{root_path}\' не существует или не является директорией.')
        return []

    print(f'Поиск в директории: {root_path}')

    if isinstance(patterns, str):
        patterns = [patterns]

    for root, _, files in os.walk(root_path):
        for filename in files:
            if any(fnmatch.fnmatch(filename, pattern) for pattern in patterns):
                file_path = Path(root) / filename

                try:
                    with file_path.open('r', encoding = 'utf-8') as file:
                        if as_list:
                            matches.extend(file.readlines())
                        else:
                            matches.append(file.read())
                except Exception as ex:
                    logger.error(f'Ошибка при чтении файла \'{file_path}\'.', ex)

    return matches


def get_directory_names(directory: str | Path) -> list[str]:
    """
    Возвращает список имен директорий из указанной директории.

    Args:
        directory (str | Path): Путь к директории, из которой нужно получить имена.

    Returns:
        list[str]: Список имен директорий, найденных в указанной директории.

    Example:
        >>> from pathlib import Path
        >>> directory = Path('.')
        >>> get_directory_names(directory)
        ['dir1', 'dir2']
    """
    try:
        return [entry.name for entry in Path(directory).iterdir() if entry.is_dir()]
    except Exception as ex:
        logger.error(f'Ошибка при получении списка имен директорий из \'{directory}\'.', ex)
        return []


def remove_bom(path: str | Path) -> None:
    """
    Удаляет BOM из текстового файла или из всех файлов Python в директории.

    Args:
        path (str | Path): Путь к файлу или директории.

    Example:
        >>> from pathlib import Path
        >>> file_path = Path('example.txt')
        >>> with open(file_path, 'w', encoding='utf-8') as f:
        ...     f.write('\ufeffПример текста с BOM')
        >>> remove_bom(file_path)
        >>> with open(file_path, 'r', encoding='utf-8') as f:
        ...     print(f.read())
        Пример текста с BOM
    """
    path = Path(path)
    if path.is_file():
        try:
            with path.open('r+', encoding = 'utf-8') as file:
                content = file.read().replace('\ufeff', '')
                file.seek(0)
                file.write(content)
                file.truncate()
        except Exception as ex:
            logger.error(f'Ошибка при удалении BOM из файла {path}.', ex)
            ...
    elif path.is_dir():
        for root, _, files in os.walk(path):
             for file in files:
                 if file.endswith('.py'):
                    file_path = Path(root) / file
                    try:
                        with file_path.open('r+', encoding = 'utf-8') as f:
                            content = f.read().replace('\ufeff', '')
                            f.seek(0)
                            f.write(content)
                            f.truncate()
                    except Exception as ex:
                       logger.error(f'Ошибка при удалении BOM из файла {file_path}.', ex)
                       ...

    else:
        logger.error(f'Указанный путь \'{path}\' не является файлом или директорией.')
        ...

def find_file_in_dir(directory_path, filename):
    """
    Ищет файл с точным именем filename в директории directory_path.
    Возвращает полный путь к файлу, если найден, иначе None.
    """
    try:
        for item in os.listdir(directory_path):
            full_path = os.path.join(directory_path, item)
            # Проверяем, что это файл (а не директория) и имя совпадает
            if os.path.isfile(full_path) and item == filename:
                return full_path
    except FileNotFoundError:
        print(f"Ошибка: Директория не найдена: {directory_path}")
        return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None
    return None # Файл не найден

def main() -> None:
    """Entry point for BOM removal in Python files."""
    root_dir = Path('..', 'src')
    logger.info(f'Starting BOM removal in {root_dir}')
    remove_bom(root_dir)



if __name__ == '__main__':
    main()