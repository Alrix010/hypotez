## Как использовать блок кода `ThinkingProcessor.process_thinking_chunk`

=========================================================================================

### Описание

-------------------------

Блок кода `ThinkingProcessor.process_thinking_chunk`  предназначен для обработки фрагментов текста (чанка) с маркерами "<think>" и "</think>", которые сигнализируют о начале и завершении процесса "мышления" -  моделирования или генерации текста.

### Шаги выполнения

-------------------------

1. **Проверка наличия маркеров "<think>" и "</think>":**  Код проверяет наличие маркеров "<think>" и "</think>" в тексте. 
2. **Обработка  "мышления"**:
    - Если маркер "<think>"  встречается, функция создает объект `Reasoning` с состоянием "🤔 Is thinking..." и сохраняет его в список `actual_result`, а также добавляет текст перед маркером. 
    - Если встречается  маркер "</think>", функция создает объект `Reasoning` с состоянием "Finished" и добавляет его в список `actual_result`.
    -  Если маркер "<think>" есть, но "</think>" нет, функция считает текущее время (`actual_time`) и добавляет в список `actual_result` текст, который следует за маркером "<think>".
    - Если маркер "<think>"  и "</think>" присутствуют, функция не изменяет текущее время (`actual_time`), а добавляет в список  `actual_result`  соответствующий текст. 

### Пример использования

-------------------------

```python
    import time
    from g4f.tools.run_tools import ThinkingProcessor, Reasoning

    # Пример с "мышлением"
    chunk = "Hello <think>World"
    start_time = time.time()
    actual_time, actual_result = ThinkingProcessor.process_thinking_chunk(chunk, start_time)
    print(f"actual_time: {actual_time}")
    print(f"actual_result: {actual_result}")

    # Вывод:
    # actual_time: 1680224918.541887
    # actual_result: ['Hello ', Reasoning(status='🤔 Is thinking...', is_thinking='<think>'), Reasoning('World')]

    # Пример с завершением "мышления"
    chunk = "token</think> content after"
    start_time = time.time()
    actual_time, actual_result = ThinkingProcessor.process_thinking_chunk(chunk, start_time)
    print(f"actual_time: {actual_time}")
    print(f"actual_result: {actual_result}")

    # Вывод:
    # actual_time: 0
    # actual_result: [Reasoning('token'), Reasoning(status='Finished', is_thinking='</think>'), ' content after']
```

### Дополнительные замечания:

- Функция `ThinkingProcessor.process_thinking_chunk`  определяет  взаимодействие с "мышлением".
- Она  формирует список  `actual_result`, содержащий текст и объекты  `Reasoning`.
- Объекты  `Reasoning`  представляют собой "мыслительные" действия, которые отмечают начало, завершение  или  продолжение процесса "мышления".
-  В случае,  если процесс "мышления"  завершается,  `ThinkingProcessor.process_thinking_chunk`  использует время начала процесса.