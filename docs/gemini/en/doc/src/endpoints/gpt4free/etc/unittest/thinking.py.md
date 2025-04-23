# Модуль тестирования процесса мышления

## Обзор

Этот модуль содержит тесты для класса `ThinkingProcessor`, который используется для обработки фрагментов текста, содержащих теги `<think>` и `</think>`, указывающие на процесс мышления. Тесты проверяют правильность обработки различных сценариев, включая начало, конец и продолжение процесса мышления.

## Подробнее

Модуль использует библиотеку `unittest` для определения тестовых случаев и методы класса `ThinkingProcessor` для проверки логики обработки текста. Тесты охватывают различные ситуации, такие как фрагменты текста без тегов мышления, фрагменты с началом и концом тегов мышления, а также фрагменты, представляющие собой продолжение процесса мышления.

## Классы

### `TestThinkingProcessor`

**Описание**: Класс, содержащий тестовые методы для проверки функциональности `ThinkingProcessor`.

**Наследует**:
- `unittest.TestCase`: Базовый класс для создания тестовых случаев.

**Атрибуты**:
- Отсутствуют.

**Методы**:
- `test_non_thinking_chunk()`: Проверяет обработку фрагмента текста, не содержащего теги мышления.
- `test_thinking_start()`: Проверяет обработку фрагмента текста, содержащего открывающий тег `<think>`.
- `test_thinking_end()`: Проверяет обработку фрагмента текста, содержащего закрывающий тег `</think>`.
- `test_thinking_start_and_end()`: Проверяет обработку фрагмента текста, содержащего как открывающий, так и закрывающий теги мышления.
- `test_ongoing_thinking()`: Проверяет обработку фрагмента текста, представляющего собой продолжение процесса мышления.
- `test_chunk_with_text_after_think()`: Проверяет обработку фрагмента текста с текстом после тега `</think>`.

## Методы класса

### `test_non_thinking_chunk`

```python
    def test_non_thinking_chunk(self):
        chunk = "This is a regular text."
        expected_time, expected_result = 0, [chunk]
        actual_time, actual_result = ThinkingProcessor.process_thinking_chunk(chunk)
        self.assertEqual(actual_time, expected_time)
        self.assertEqual(actual_result, expected_result)
```

**Цель**: Проверяет, что фрагмент текста без тегов `<think>` обрабатывается правильно.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- Ничего.

**Как работает функция**:
- Определяет фрагмент текста, не содержащий тегов мышления.
- Вызывает `ThinkingProcessor.process_thinking_chunk()` с этим фрагментом.
- Проверяет, что возвращаемое время равно 0, а результат содержит исходный фрагмент текста.

**Примеры**:

```python
    test_non_thinking_chunk(self)
```

### `test_thinking_start`

```python
    def test_thinking_start(self):
        chunk = "Hello <think>World"
        expected_time = time.time()
        expected_result = ["Hello ", Reasoning(status="🤔 Is thinking...", is_thinking="<think>"), Reasoning("World")]
        actual_time, actual_result = ThinkingProcessor.process_thinking_chunk(chunk)
        self.assertAlmostEqual(actual_time, expected_time, delta=1)
        self.assertEqual(actual_result[0], expected_result[0])
        self.assertEqual(actual_result[1], expected_result[1])
        self.assertEqual(actual_result[2], expected_result[2])
```

**Цель**: Проверяет, что фрагмент текста, начинающийся с тега `<think>`, обрабатывается правильно.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- Ничего.

**Как работает функция**:
- Определяет фрагмент текста, начинающийся с тега `<think>`.
- Вызывает `ThinkingProcessor.process_thinking_chunk()` с этим фрагментом.
- Проверяет, что возвращаемое время приблизительно равно текущему времени, а результат содержит текст до тега, объект `Reasoning` с соответствующим статусом и текст после тега.

**Примеры**:

```python
    test_thinking_start(self)
```

### `test_thinking_end`

```python
    def test_thinking_end(self):
        start_time = time.time()
        chunk = "token</think> content after"
        expected_result = [Reasoning("token"), Reasoning(status="Finished", is_thinking="</think>"), " content after"]
        actual_time, actual_result = ThinkingProcessor.process_thinking_chunk(chunk, start_time)
        self.assertEqual(actual_time, 0)
        self.assertEqual(actual_result[0], expected_result[0])
        self.assertEqual(actual_result[1], expected_result[1])
        self.assertEqual(actual_result[2], expected_result[2])
```

**Цель**: Проверяет, что фрагмент текста, заканчивающийся тегом `</think>`, обрабатывается правильно.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- Ничего.

**Как работает функция**:
- Определяет фрагмент текста, заканчивающийся тегом `</think>`.
- Вызывает `ThinkingProcessor.process_thinking_chunk()` с этим фрагментом и временем начала.
- Проверяет, что возвращаемое время равно 0, а результат содержит объект `Reasoning` с текстом до тега, объект `Reasoning` с соответствующим статусом и текст после тега.

**Примеры**:

```python
    test_thinking_end(self)
```

### `test_thinking_start_and_end`

```python
    def test_thinking_start_and_end(self):
        start_time = time.time()
        chunk = "<think>token</think> content after"
        expected_result = [Reasoning(status="🤔 Is thinking...", is_thinking="<think>"), Reasoning("token"), Reasoning(status="Finished", is_thinking="</think>"), " content after"]
        actual_time, actual_result = ThinkingProcessor.process_thinking_chunk(chunk, start_time)
        self.assertEqual(actual_time, 0)
        self.assertEqual(actual_result[0], expected_result[0])
        self.assertEqual(actual_result[1], expected_result[1])
        self.assertEqual(actual_result[2], expected_result[2])
        self.assertEqual(actual_result[3], expected_result[3])
```

**Цель**: Проверяет, что фрагмент текста, содержащий как открывающий, так и закрывающий теги `<think>`, обрабатывается правильно.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- Ничего.

**Как работает функция**:
- Определяет фрагмент текста, содержащий теги `<think>` и `</think>`.
- Вызывает `ThinkingProcessor.process_thinking_chunk()` с этим фрагментом и временем начала.
- Проверяет, что возвращаемое время равно 0, а результат содержит объекты `Reasoning` для начала и конца тегов, текст между тегами и текст после закрывающего тега.

**Примеры**:

```python
    test_thinking_start_and_end(self)
```

### `test_ongoing_thinking`

```python
    def test_ongoing_thinking(self):
        start_time = time.time()
        chunk = "Still thinking..."
        expected_result = [Reasoning("Still thinking...")]
        actual_time, actual_result = ThinkingProcessor.process_thinking_chunk(chunk, start_time)
        self.assertEqual(actual_time, start_time)
        self.assertEqual(actual_result, expected_result)
```

**Цель**: Проверяет, что фрагмент текста, представляющий собой продолжение процесса мышления, обрабатывается правильно.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- Ничего.

**Как работает функция**:
- Определяет фрагмент текста, представляющий собой продолжение процесса мышления.
- Вызывает `ThinkingProcessor.process_thinking_chunk()` с этим фрагментом и временем начала.
- Проверяет, что возвращаемое время равно времени начала, а результат содержит объект `Reasoning` с исходным фрагментом текста.

**Примеры**:

```python
    test_ongoing_thinking(self)
```

### `test_chunk_with_text_after_think`

```python
    def test_chunk_with_text_after_think(self):
        chunk = "Start <think>Middle</think>End"
        expected_time = 0
        expected_result = ["Start ", Reasoning(status="🤔 Is thinking...", is_thinking="<think>"), Reasoning("Middle"), Reasoning(status="Finished", is_thinking="</think>"), "End"]
        actual_time, actual_result = ThinkingProcessor.process_thinking_chunk(chunk)
        self.assertEqual(actual_time, expected_time)
        self.assertEqual(actual_result, expected_result)
```

**Цель**: Проверяет, что фрагмент текста с текстом до, внутри и после тегов `<think>` и `</think>` обрабатывается правильно.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- Ничего.

**Как работает функция**:
- Определяет фрагмент текста с текстом до, внутри и после тегов `<think>` и `</think>`.
- Вызывает `ThinkingProcessor.process_thinking_chunk()` с этим фрагментом.
- Проверяет, что возвращаемое время равно 0, а результат содержит текст до тега, объекты `Reasoning` для начала и конца тегов, текст между тегами и текст после закрывающего тега.

**Примеры**:

```python
    test_chunk_with_text_after_think(self)
```