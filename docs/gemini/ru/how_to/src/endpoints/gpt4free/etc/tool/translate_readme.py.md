## Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код переводит текст из файла `README.md` на указанный язык и сохраняет результат в новый файл `README-{iso}.md`. 

Шаги выполнения
-------------------------
1. **Настройка параметров**:
    - **`iso`**: ISO-код языка, на который необходимо перевести текст (например, "GE" для грузинского).
    - **`language`**: Название языка, которое будет использоваться в запросе к GPT4Free (например, "german" для немецкого).
    - **`translate_prompt`**: Префикс запроса к GPT4Free для перевода. Он включает в себя инструкцию перевести Markdown-документ, не затрагивая инлайн-код. 
2. **Чтение исходного файла `README.md`**:  
    -  Файл `README.md` читается с использованием `open` и `fp.read()`.
3. **Обработка текста**:
    - **Разделение на части**: Исходный текст разделяется на части по заголовкам второго уровня (`## `).
    - **Перевод каждой части**: Для каждой части текста выполняется асинхронный перевод с помощью `asyncio.gather()`. 
4. **Создание нового файла**:
    - Создается новый файл с именем `README-{iso}.md`.
    - Переведенный текст записывается в новый файл.

Пример использования
-------------------------

```python
import sys
from pathlib import Path
import asyncio

sys.path.append(str(Path(__file__).parent.parent.parent))

import g4f
g4f.debug.logging = True
from g4f.debug import access_token
provider = g4f.Provider.OpenaiChat

iso = "GE"
language = "german"
translate_prompt = f"""
Translate this markdown document to {language}.
Don't translate or change inline code examples.
```md
"""
keep_note = "Keep this: [!Note] as [!Note].\\n"
blocklist = [
    '## ©️ Copyright',
    '## 🚀 Providers and Models',
    '## 🔗 Related GPT4Free Projects'
]
allowlist = [
    "### Other",
    "### Models"
]

# ... (остальной код)

with open("README.md", "r") as fp:
    readme = fp.read()

print("Translate readme...")
readme = asyncio.run(translate_readme(readme))

file = f"README-{iso}.md"
with open(file, "w") as fp:
    fp.write(readme)
print(f'"{file}" saved')
```

В этом примере:
-  `iso`  устанавливается как "GE", что означает грузинский язык.
-  `language`  устанавливается как "german".
-  `translate_prompt`  содержит инструкцию по переводу.
-  `blocklist`  и  `allowlist`  определяют разделы, которые будут обработаны отдельно.
-  `asyncio.run(translate_readme(readme))`  используется для выполнения асинхронного перевода.
-  `README-{iso}.md`  - имя нового файла для переведенного текста.