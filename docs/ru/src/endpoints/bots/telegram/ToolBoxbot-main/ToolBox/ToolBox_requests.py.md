# Модуль `ToolBox_requests.py`

## Обзор

Модуль `ToolBox_requests.py` представляет собой основной компонент для обработки запросов от пользователей Telegram-бота. Он включает в себя классы и функции для взаимодействия с ботом, обработки текстовых и графических запросов, а также для управления тарифами и доступом к различным функциям.

## Подробнее

Модуль содержит класс `ToolBox`, который наследует функциональность от `keyboards` и `neural_networks`. Он отвечает за инициализацию бота, загрузку текстовых подсказок, определение обработчиков команд и выполнение запросов пользователей. Основная задача модуля - предоставить удобный и гибкий интерфейс для взаимодействия с пользователями бота и обработки их запросов с использованием различных AI-моделей.

## Классы

### `ToolBox`

**Описание**: Класс `ToolBox` является основным классом для управления логикой Telegram-бота.

**Наследует**:
- `keyboards`: Предоставляет методы для создания клавиатур.
- `neural_networks`: Предоставляет методы для работы с нейронными сетями.

**Атрибуты**:
- `name` (list): Список названий основных кнопок меню.
- `data` (list): Список данных, связанных с основными кнопками меню.
- `prompts_text` (dict): Словарь с текстовыми подсказками и сообщениями для бота.
- `bot` (telebot.TeleBot): Экземпляр Telegram-бота.
- `keyboard_blank` (lambda): Лямбда-функция для создания встроенных клавиатур.
- `reply_keyboard` (lambda): Лямбда-функция для создания клавиатур ответов.
- `__delay` (lambda): Лямбда-функция для отправки сообщения о задержке.
- `start_request` (lambda): Лямбда-функция для отправки стартового сообщения.
- `restart` (lambda): Лямбда-функция для отправки сообщения о перезапуске.
- `restart_markup` (lambda): Лямбда-функция для редактирования сообщения о перезапуске.
- `OneTextArea` (lambda): Лямбда-функция для отправки запроса одного текста.
- `SomeTextsArea` (lambda): Лямбда-функция для отправки запроса нескольких текстов.
- `ImageSize` (lambda): Лямбда-функция для отправки запроса размера изображения.
- `ImageArea` (lambda): Лямбда-функция для отправки запроса изображения.
- `ImageChange` (lambda): Лямбда-функция для отправки сообщения об изменении изображения.
- `BeforeUpscale` (lambda): Лямбда-функция для отправки сообщения перед улучшением изображения.
- `FreeArea` (lambda): Лямбда-функция для отправки запроса в свободном режиме.
- `TariffArea` (lambda): Лямбда-функция для отправки запроса тарифов.
- `TariffExit` (lambda): Лямбда-функция для выхода из меню тарифов.
- `TarrifEnd` (lambda): Лямбда-функция для отправки сообщения об окончании тарифа.
- `FreeTariffEnd` (lambda): Лямбда-функция для отправки сообщения об окончании бесплатного тарифа.
- `SomeTexts` (lambda): Лямбда-функция для выбора одного или нескольких текстов.

**Принцип работы**:
Класс `ToolBox` инициализирует Telegram-бота, загружает необходимые текстовые подсказки и настраивает обработчики команд. Он использует лямбда-функции для упрощения отправки различных типов сообщений и запросов пользователям. Класс также включает методы для обработки текстовых и графических запросов, а также для управления тарифами и доступом к функциям бота.

**Методы**:
- `Text_types(message)`: Отправляет сообщение с типами текстов.
- `Basic_tariff(message)`: Отправляет информацию о базовом тарифе и предлагает его подключить.
- `Pro_tariff(message)`: Отправляет информацию о профессиональном тарифе и предлагает его подключить.
- `TextCommands(message, ind: int)`: Обрабатывает команды для генерации текста.
- `SomeTextsCommand(message, ind: int, tokens: dict[str, int])`: Обрабатывает команды для генерации нескольких текстов.
- `ImageCommand(message, prompt: str, size: list[int])`: Обрабатывает команды для генерации изображений.
- `Image_Regen_And_Upscale(message, prompt: str, size: list[int], seed, num_inference_steps=4)`: Обрабатывает команды для регенерации и улучшения изображений.
- `FreeCommand(message, prompts: list[str])`: Обрабатывает команды в свободном режиме.

## Методы класса

### `Text_types`

```python
def Text_types(self, message):
    """
    Отправляет пользователю сообщение с вариантами типов текстов для выбора.

    Args:
        message: Объект сообщения от Telegram.

    Returns:
        types.Message: Отредактированное сообщение с вариантами типов текстов.
    """
    name = ["Коммерческий  🛍️", "SMM 📱", "Брейншторм 💡", "Реклама 📺", "Заголовки 🔍", "SEO 🌐", "Новость 📰", "Редактура 📝", "В меню"]
    data = ["comm-text", "smm-text", "brainst-text", "advertising-text", "headlines-text", "seo-text", "news", "editing", "exit"]
    return self.bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text="📝 Выберите тип текста", reply_markup=self.keyboard_blank(self, name, data))
```

**Назначение**:
Функция отправляет пользователю сообщение с различными типами текстов, которые он может выбрать.

**Параметры**:
- `message`: Объект сообщения от Telegram, содержащий информацию о чате и пользователе.

**Возвращает**:
- `types.Message`: Отредактированное сообщение с вариантами типов текстов.

**Как работает функция**:
- Определяет списки `name` и `data`, содержащие названия и идентификаторы типов текстов.
- Вызывает метод `self.bot.edit_message_text` для редактирования сообщения пользователя, добавляя к нему клавиатуру с вариантами типов текстов.

**Примеры**:
```python
# Пример вызова функции Text_types
# Предположим, что у вас есть объект message, полученный от Telegram
message = ...  # Объект message от Telegram
toolbox = ToolBox()
result = toolbox.Text_types(message)
# result будет содержать отредактированное сообщение с вариантами типов текстов
```

### `Basic_tariff`

```python
def Basic_tariff(self, message):
    """
    Отправляет пользователю информацию о базовом тарифе и предлагает его подключить.

    Args:
        message: Объект сообщения от Telegram.
    """
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("Подключить тариф BASIC", pay=True))
    keyboard.add(types.InlineKeyboardButton("К тарифам", callback_data="tariff_exit"))
    price = [types.LabeledPrice(label='BASIC', amount=99*100)]
    self.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    self.bot.send_invoice(chat_id=message.chat.id, title = 'BASIC',
        description = "Безлимитная генерация текста, в том числе по готовым промптам.",
        invoice_payload = 'basic_invoice_payload',
        start_parameter='subscription',
        provider_token = os.environ['PROVIDE_TOKEN'],
        currency='RUB', prices=price, reply_markup=keyboard)
```

**Назначение**:
Функция отправляет пользователю информацию о базовом тарифе и предлагает его подключить.

**Параметры**:
- `message`: Объект сообщения от Telegram, содержащий информацию о чате и пользователе.

**Как работает функция**:
- Создает встроенную клавиатуру с кнопками "Подключить тариф BASIC" и "К тарифам".
- Определяет цену для базового тарифа.
- Удаляет текущее сообщение пользователя.
- Отправляет счет (invoice) пользователю с информацией о базовом тарифе и кнопками для оплаты.

**Примеры**:
```python
# Пример вызова функции Basic_tariff
# Предположим, что у вас есть объект message, полученный от Telegram
message = ...  # Объект message от Telegram
toolbox = ToolBox()
toolbox.Basic_tariff(message)
# Пользователю будет отправлен счет с информацией о базовом тарифе
```

### `Pro_tariff`

```python
def Pro_tariff(self, message):
    """
    Отправляет пользователю информацию о профессиональном тарифе и предлагает его подключить.

    Args:
        message: Объект сообщения от Telegram.
    """
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("Подключить тариф PRO", pay=True))
    keyboard.add(types.InlineKeyboardButton("К тарифам", callback_data="tariff_exit"))
    price = [types.LabeledPrice(label='PRO', amount=199*100)]
    self.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    self.bot.send_invoice(chat_id=message.chat.id, title = 'PRO',
        description = "Безлимитная генерация текста (в том числе по готовым промптам) и изображений.",
        invoice_payload = 'pro_invoice_payload',
        start_parameter='subscription',
        provider_token = os.environ['PROVIDE_TOKEN'],
        currency='RUB', prices=price, reply_markup=keyboard)
```

**Назначение**:
Функция отправляет пользователю информацию о профессиональном тарифе и предлагает его подключить.

**Параметры**:
- `message`: Объект сообщения от Telegram, содержащий информацию о чате и пользователе.

**Как работает функция**:
- Создает встроенную клавиатуру с кнопками "Подключить тариф PRO" и "К тарифам".
- Определяет цену для профессионального тарифа.
- Удаляет текущее сообщение пользователя.
- Отправляет счет (invoice) пользователю с информацией о профессиональном тарифе и кнопками для оплаты.

**Примеры**:
```python
# Пример вызова функции Pro_tariff
# Предположим, что у вас есть объект message, полученный от Telegram
message = ...  # Объект message от Telegram
toolbox = ToolBox()
toolbox.Pro_tariff(message)
# Пользователю будет отправлен счет с информацией о профессиональном тарифе
```

### `TextCommands`

```python
def TextCommands(self, message, ind: int):
    """
    Обрабатывает команды для генерации текста на основе заданного индекса и введенных пользователем данных.

    Args:
        message: Объект сообщения от Telegram.
        ind (int): Индекс команды в списке команд.

    Returns:
        tuple[int, int, int]: Кортеж, содержащий количество входящих и исходящих токенов, а также флаг успешности операции (1).
    """
    info = []
    incoming_tokens = 0; outgoing_tokens = 0; response = None
    if 'TEXT' in pc.commands_size[ind]:
        info.append(message.text)
        msg = self.bot.send_message(chat_id=message.chat.id, text=self.prompts_text['text_list'][ind][1])
        def Text_next_step(message):
            """
            Внутренняя функция для обработки следующего шага в генерации текста.

            Args:
                message: Объект сообщения от Telegram.
            """
            nonlocal info, incoming_tokens, outgoing_tokens, response
            info += message.text.split(';')
            while len(info) < len(pc.commands_size[ind]):
                info.append("Параметр отсутствует")
            prompt = pc.get_prompt(ind=ind, info=info)
            response, incoming_tokens, outgoing_tokens = self.__gpt_4o_mini(prompt=[{ "role": "user", "content": prompt }], message=message)
            self.restart(message)
        self.bot.register_next_step_handler(msg, Text_next_step)
        while response is None:
            time.sleep(0.5)
        return incoming_tokens, outgoing_tokens, 1
    else:
        info = message.text.split(';')
        while len(info) < len(pc.commands_size[ind]):
            info.append("Параметр отсутствует")
        prompt = pc.get_prompt(ind=ind, info=info)
        response, incoming_tokens, outgoing_tokens = self.__gpt_4o_mini(prompt=[{ "role": "user", "content": prompt }], message=message)
        self.restart(message)
        return incoming_tokens, outgoing_tokens, 1
```

**Назначение**:
Функция обрабатывает команды для генерации текста на основе заданного индекса и введенных пользователем данных.

**Параметры**:
- `message`: Объект сообщения от Telegram, содержащий информацию о чате и пользователе.
- `ind` (int): Индекс команды в списке команд.

**Возвращает**:
- `tuple[int, int, int]`: Кортеж, содержащий количество входящих и исходящих токенов, а также флаг успешности операции (1).

**Как работает функция**:
- Инициализирует пустой список `info` для хранения информации, введенной пользователем.
- Проверяет, содержит ли команда текст (`'TEXT' in pc.commands_size[ind]`).
- Если команда содержит текст, отправляет пользователю запрос на ввод дополнительной информации.
- Регистрирует обработчик следующего шага (`Text_next_step`) для получения дополнительной информации от пользователя.
- После получения всей необходимой информации формирует промпт и отправляет его в модель GPT-4o mini для генерации текста.
- Если команда не содержит текст, сразу формирует промпт на основе введенной пользователем информации и отправляет его в модель GPT-4o mini.
- Перезапускает бота (`self.restart(message)`).
- Возвращает количество входящих и исходящих токенов, а также флаг успешности операции (1).

**Внутренние функции**:
- `Text_next_step(message)`:
    - **Назначение**: Обрабатывает следующий шаг в процессе генерации текста, получая дополнительную информацию от пользователя.
    - **Параметры**:
        - `message`: Объект сообщения от Telegram, содержащий информацию о чате и введенный пользователем текст.
    - **Как работает**:
        - Добавляет введенную пользователем информацию в список `info`.
        - Заполняет список `info` значениями "Параметр отсутствует", если пользователь не предоставил все необходимые параметры.
        - Формирует промпт на основе списка `info`.
        - Отправляет промпт в модель GPT-4o mini для генерации текста.
        - Перезапускает бота (`self.restart(message)`).

**Примеры**:
```python
# Пример вызова функции TextCommands
# Предположим, что у вас есть объект message, полученный от Telegram, и индекс команды ind
message = ...  # Объект message от Telegram
ind = 0  # Индекс команды
toolbox = ToolBox()
incoming_tokens, outgoing_tokens, success = toolbox.TextCommands(message, ind)
# incoming_tokens, outgoing_tokens - количество входящих и исходящих токенов
# success - флаг успешности операции (1)
```

### `SomeTextsCommand`

```python
def SomeTextsCommand(self, message, ind: int, tokens: dict[str, int]):
    """
    Обрабатывает команды для генерации нескольких текстов на основе заданного индекса и введенных пользователем данных.

    Args:
        message: Объект сообщения от Telegram.
        ind (int): Индекс команды в списке команд.
        tokens (dict[str, int]): Словарь с информацией о количестве доступных токенов.

    Returns:
        tuple[int, int, int]: Кортеж, содержащий количество входящих и исходящих токенов, а также количество сгенерированных текстов.
    """
    n = int(message.text)
    avalib = [0, 1, 3, 5, 6]
    ans = []

    for i in range(n):
        ans.append([])
        if "TEXT" in pc.commands_size[ind]:
            msg = self.bot.send_message(chat_id=message.chat.id, text=f"Введите текст источника {i+1}")
            text = None
            def Text_next_step(message):
                """
                Внутренняя функция для обработки следующего шага ввода текста источника.

                Args:
                    message: Объект сообщения от Telegram.
                """
                nonlocal text, ans
                text = message.text
                ans[i].append(text)
            self.bot.register_next_step_handler(msg, Text_next_step)
            while text is None:
                time.sleep(0.5)
    
    index = avalib.index(ind)
    for el in range(1, len(self.prompts_text["few_texts_list"][index])):
        msg = self.bot.send_message(chat_id=message.chat.id, text=self.prompts_text["few_texts_list"][index][el])
        params = None
        def Params_addition(message):
            """
            Внутренняя функция для добавления параметров к запросу.

            Args:
                message: Объект сообщения от Telegram.
            """
            nonlocal params, ans
            params = message.text
            params = params.split(';')
            if len(params) < len(pc.commands_size[ind]):
                while len(params) < len(pc.commands_size[ind]):
                    params.append(None)
            param = params[0]
            [ans[i].append(param) if params[i] is None else ans[i].append(params[i]) for i in range(len(ans))]
        self.bot.register_next_step_handler(msg, Params_addition)
        while params is None:
            time.sleep(0.5)

    incoming_tokens = 0; outgoing_tokens = 0
    def process_prompt(i):
        """
        Внутренняя функция для обработки и отправки промпта в модель GPT-4o mini.

        Args:
            i (int): Индекс текущего текста для генерации.

        Returns:
            tuple[int, int]: Кортеж, содержащий количество входящих и исходящих токенов для текущего текста.
        """
        nonlocal incoming_tokens, outgoing_tokens
        prompt = pc.get_prompt(ind=ind, info=ans[i])
        if tokens['incoming_tokens'] - incoming_tokens > 0 and tokens['outgoing_tokens'] - outgoing_tokens > 0 or tokens['free_requests'] - i > 0:
            response, in_tokens, out_tokens = self.__gpt_4o_mini(prompt=[{"role": "user", "content": prompt}], message=message)
            return in_tokens, out_tokens
        return 0, 0
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(process_prompt, range(n)))
    
    for in_tokens, out_tokens in results:
        incoming_tokens += in_tokens
        outgoing_tokens += out_tokens
    
    self.restart(message)
    return incoming_tokens, outgoing_tokens, n
```

**Назначение**:
Функция обрабатывает команды для генерации нескольких текстов на основе заданного индекса и введенных пользователем данных.

**Параметры**:
- `message`: Объект сообщения от Telegram, содержащий информацию о чате и пользователе.
- `ind` (int): Индекс команды в списке команд.
- `tokens` (dict[str, int]): Словарь с информацией о количестве доступных токенов.

**Возвращает**:
- `tuple[int, int, int]`: Кортеж, содержащий количество входящих и исходящих токенов, а также количество сгенерированных текстов.

**Как работает функция**:
- Получает количество текстов для генерации от пользователя.
- Запрашивает у пользователя текст источника для каждого текста, если это необходимо.
- Запрашивает дополнительные параметры для каждого текста.
- Формирует промпты для каждого текста и отправляет их в модель GPT-4o mini для генерации.
- Использует `ThreadPoolExecutor` для параллельной обработки промптов.
- Перезапускает бота (`self.restart(message)`).
- Возвращает количество входящих и исходящих токенов, а также количество сгенерированных текстов.

**Внутренние функции**:
- `Text_next_step(message)`:
    - **Назначение**: Обрабатывает следующий шаг ввода текста источника.
    - **Параметры**:
        - `message`: Объект сообщения от Telegram, содержащий информацию о чате и введенный пользователем текст.
    - **Как работает**:
        - Получает текст источника от пользователя.
        - Добавляет текст источника в список `ans`.
- `Params_addition(message)`:
    - **Назначение**: Добавляет параметры к запросу.
    - **Параметры**:
        - `message`: Объект сообщения от Telegram, содержащий информацию о чате и введенные пользователем параметры.
    - **Как работает**:
        - Получает параметры от пользователя.
        - Разделяет параметры на отдельные значения.
        - Добавляет параметры в список `ans`.
- `process_prompt(i)`:
    - **Назначение**: Обрабатывает и отправляет промпт в модель GPT-4o mini.
    - **Параметры**:
        - `i` (int): Индекс текущего текста для генерации.
    - **Как работает**:
        - Формирует промпт на основе списка `ans`.
        - Проверяет, достаточно ли доступных токенов для генерации текста.
        - Отправляет промпт в модель GPT-4o mini для генерации текста.
        - Возвращает количество входящих и исходящих токенов.

**Примеры**:
```python
# Пример вызова функции SomeTextsCommand
# Предположим, что у вас есть объект message, полученный от Telegram, индекс команды ind и словарь tokens
message = ...  # Объект message от Telegram
ind = 0  # Индекс команды
tokens = {"incoming_tokens": 1000, "outgoing_tokens": 1000, "free_requests": 10}  # Словарь с информацией о токенах
toolbox = ToolBox()
incoming_tokens, outgoing_tokens, count = toolbox.SomeTextsCommand(message, ind, tokens)
# incoming_tokens, outgoing_tokens - количество входящих и исходящих токенов
# count - количество сгенерированных текстов
```

### `ImageCommand`

```python
def ImageCommand(self, message, prompt: str, size: list[int]):
    """
    Обрабатывает команду для генерации изображения на основе заданного промпта и размера.

    Args:
        message: Объект сообщения от Telegram.
        prompt (str): Текстовый промпт для генерации изображения.
        size (list[int]): Список, содержащий ширину и высоту изображения.

    Returns:
        int: Случайное число, используемое в качестве seed для генерации изображения.
    """
    seed = randint(1, 1000000)
    self.__FLUX_schnell(prompt=prompt, size=size, message=message, seed=seed, num_inference_steps=4)
    self.ImageChange(message)
    return seed
```

**Назначение**:
Функция обрабатывает команду для генерации изображения на основе заданного промпта и размера.

**Параметры**:
- `message`: Объект сообщения от Telegram, содержащий информацию о чате и пользователе.
- `prompt` (str): Текстовый промпт для генерации изображения.
- `size` (list[int]): Список, содержащий ширину и высоту изображения.

**Возвращает**:
- `int`: Случайное число, используемое в качестве seed для генерации изображения.

**Как работает функция**:
- Генерирует случайное число в диапазоне от 1 до 1000000 и сохраняет его в переменной `seed`.
- Вызывает приватный метод `self.__FLUX_schnell` для генерации изображения на основе заданного промпта, размера и seed.
- Вызывает метод `self.ImageChange` для отправки сообщения об изменении изображения.
- Возвращает случайное число `seed`.

**Примеры**:
```python
# Пример вызова функции ImageCommand
# Предположим, что у вас есть объект message, полученный от Telegram, промпт и размер изображения
message = ...  # Объект message от Telegram
prompt = "A cat sitting on a mat"  # Текстовый промпт
size = [512, 512]  # Размер изображения
toolbox = ToolBox()
seed = toolbox.ImageCommand(message, prompt, size)
# seed - случайное число, использованное для генерации изображения
```

### `Image_Regen_And_Upscale`

```python
def Image_Regen_And_Upscale(self, message, prompt: str, size: list[int], seed, num_inference_steps=4):
    """
    Обрабатывает команды для регенерации и улучшения изображений.

    Args:
        message: Объект сообщения от Telegram.
        prompt (str): Текстовый промпт для генерации изображения.
        size (list[int]): Список, содержащий ширину и высоту изображения.
        seed: Случайное число, используемое в качестве seed для генерации изображения.
        num_inference_steps (int): Количество шагов для улучшения изображения.

    Returns:
        None
    """
    return self.__FLUX_schnell(prompt=prompt, size=size, message=message, seed=seed, num_inference_steps=num_inference_steps)
```

**Назначение**:
Функция обрабатывает команды для регенерации и улучшения изображений.

**Параметры**:
- `message`: Объект сообщения от Telegram, содержащий информацию о чате и пользователе.
- `prompt` (str): Текстовый промпт для генерации изображения.
- `size` (list[int]): Список, содержащий ширину и высоту изображения.
- `seed`: Случайное число, используемое в качестве seed для генерации изображения.
- `num_inference_steps` (int): Количество шагов для улучшения изображения.

**Как работает функция**:
- Вызывает приватный метод `self.__FLUX_schnell` для генерации изображения на основе заданного промпта, размера, seed и количества шагов для улучшения.

**Примеры**:
```python
# Пример вызова функции Image_Regen_And_Upscale
# Предположим, что у вас есть объект message, полученный от Telegram, промпт, размер изображения и seed
message = ...  # Объект message от Telegram
prompt = "A cat sitting on a mat"  # Текстовый промпт
size = [512, 512]  # Размер изображения
seed = 12345  # Seed для генерации изображения
toolbox = ToolBox()
toolbox.Image_Regen_And_Upscale(message, prompt, size, seed)
```

### `FreeCommand`

```python
def FreeCommand(self, message, prompts: list[str]):
    """
    Обрабатывает команды в свободном режиме, добавляя запросы пользователя в список промптов и отправляя их в модель GPT-4o mini.

    Args:
        message: Объект сообщения от Telegram.
        prompts (list[str]): Список промптов, используемых для генерации текста.

    Returns:
        tuple[int, int, list[str]]: Кортеж, содержащий количество входящих и исходящих токенов, а также обновленный список промптов.
    """
    try:
        if type(prompts[-1].get('content', False))!=list:
            prompts.append({"content": message.text, "role": "user"})
    except:
        pass
    response, incoming_tokens, outgoing_tokens = self.__gpt_4o_mini(prompt=prompts, message=message)
    prompts.append(response)
    return incoming_tokens, outgoing_tokens, prompts
```

**Назначение**:
Функция обрабатывает команды в свободном режиме, добавляя запросы пользователя в список промптов и отправляя их в модель GPT-4o mini.

**Параметры**:
- `message`: Объект сообщения от Telegram, содержащий информацию о чате и пользователе.
- `prompts` (list[str]): Список промптов, используемых для генерации текста.

**Возвращает**:
- `tuple[int, int, list[str]]`: Кортеж, содержащий количество входящих и исходящих токенов, а также обновленный список промптов.

**Как работает функция**:
- Добавляет запрос пользователя в список промптов.
- Вызывает приватный метод `self.__gpt_4o_mini` для генерации текста на основе списка промптов.
- Добавляет ответ модели в список промптов.
- Возвращает количество входящих и исходящих токенов, а также обновленный список промптов.

**Примеры**:
```python
# Пример вызова функции FreeCommand
# Предположим, что у вас есть объект message, полученный от Telegram, и список промптов
message = ...  # Объект message от Telegram
prompts = []  # Список промптов
toolbox = ToolBox()
incoming_tokens, outgoing_tokens, prompts = toolbox.FreeCommand(message, prompts)
# incoming_tokens, outgoing_tokens - количество входящих и исходящих токенов
# prompts - обновленный список промптов
```

## Приватные методы класса

### `__gpt_4o_mini`

```python
def __gpt_4o_mini(self, prompt: list[dict], message) -> tuple[dict[str, str], int, int]:
    """
    Приватный метод для обработки запросов с использованием модели GPT-4o mini.

    Args:
        prompt (list[dict]): Список словарей, содержащих промпты для модели.
        message: Объект сообщения от Telegram.

    Returns:
        tuple[dict[str, str], int, int]: Кортеж, содержащий ответ модели, количество входящих и исходящих токенов.
    """
    send = self.__delay(message)
    response, incoming_tokens, outgoing_tokens = super()._free_gpt_4o_mini(prompt=prompt)
    self.bot.edit_message_text(chat_id=send.chat.id, message_id=send.message_id, text=PromptsCompressor.html_tags_insert(response['content']), parse_mode='html')
    return response, incoming_tokens, outgoing_tokens
```

**Назначение**:
Приватный метод для обработки запросов с использованием модели GPT-4o mini.

**Параметры**:
- `prompt (list[dict])`: Список словарей, содержащих промпты для модели.
- `message`: Объект сообщения от Telegram.

**Возвращает**:
- `tuple[dict[str, str], int, int]`: Кортеж, содержащий ответ модели, количество входящих и исходящих токенов.

**Как работает функция**:
- Отправляет сообщение о задержке пользователю.
- Вызывает метод `_free_gpt_4o_mini` из родительского класса `neural_networks` для получения ответа от модели GPT-4o mini.
- Редактирует сообщение пользователя, добавляя к нему ответ модели.
- Возвращает ответ модели, количество входящих и исходящих токенов.

**Примеры**:
```python
# Пример вызова функции __gpt_4o_mini
# Предположим, что у вас есть объект message, полученный от Telegram, и список промптов
message = ...  # Объект message от Telegram
prompt = [{"role": "user", "content": "Tell me a joke"}]  # Список промптов
toolbox = ToolBox()
response, incoming_tokens, outgoing_tokens = toolbox.__gpt_4o_mini(prompt, message)
# response - ответ модели GPT-4o mini
# incoming_tokens, outgoing_tokens - количество входящих и исходящих токенов
```

### `__FLUX_schnell`

```python
def __FLUX_schnell(self, prompt: str, size: list[int], message, seed: int, num_inference_steps: int)-> None:
    """
    Приватный метод для обработки запросов на генерацию изображений с использованием модели FLUX schnell.

    Args:
        prompt (str): Текстовый промпт для генерации изображения.
        size (list[int]): Список, содержащий ширину и высоту изображения.
        message: Объект сообщения от Telegram.
        seed (int): Случайное число, используемое в качестве seed для генерации изображения.
        num_inference_steps (int): Количество шагов для улучшения изображения.

    Returns:
        None
    """
    send = self.__delay(message)
    while True:
        try:
            photo = super()._FLUX_schnell(prompt, size, seed, num_inference_steps)
        except:
            continue
        else:
            break
    if photo:
        self.bot.send_photo(chat_id=message.chat.id, photo=photo)
        return self.bot.delete_message(chat_id=send.chat.id, message_id=send.message_id)
    self.bot.edit_message_text(chat_id=send.chat.id, message_id=send.message_id, text="При генерации возникла ошибка, попробуйте повторить позже")
```

**Назначение**:
Приватный метод для обработки запросов на генерацию изображений с использованием модели FLUX schnell.

**Параметры**:
- `prompt (str)`: Текстовый промпт для генерации изображения.
- `size (list[int])`: Список, содержащий ширину и высоту изображения.
- `message`: Объект сообщения от Telegram.
- `seed (int)`: Случайное число, используемое в качестве seed для генерации изображения.