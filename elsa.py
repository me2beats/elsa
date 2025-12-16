import random
import time

def напечатать_привет():
    print("привет")

def напечатать_пока():
    print("пока")

def создать_список():
    я['данные'].append([])

def добавить_функцию_в_список(func_index, list_index):
    """Добавляет функцию в указанный список по индексу"""
    # Не позволяем добавлять функции в master список (индекс 0)
    if list_index == 0:
        print("Ошибка: нельзя добавлять функции в основной список функций")
        return

    if 0 <= func_index < len(я['данные'][0]) and 0 <= list_index < len(я['данные']):
        func_name = я['данные'][0][func_index]
        я['данные'][list_index].append(func_name)

def выполнить_список(list_index, timestamp=None):
    """Выполняет список команд в формате RPN (аргументы, затем функция)"""

    # Устанавливаем timestamp, если он не передан
    if timestamp is None:
        timestamp = int(time.time() * 1000)  # текущее время в миллисекундах

    try:
        if 0 <= list_index < len(я['данные']):
            # Добавляем индекс выполняемого списка и timestamp в "действия" перед выполнением (только если список существует)
            я['действия'].append([list_index, timestamp])

            stack = []  # стек для RPN вычислений
            command_list = я['данные'][list_index][:]  # делаем копию, чтобы не изменять оригинал

            for item in command_list:
                if isinstance(item, str) and callable(globals().get(item)):
                    # Если элемент - это имя функции, выполняем её
                    if item == "напечатать_привет":
                        напечатать_привет()
                    elif item == "напечатать_пока":
                        напечатать_пока()
                    elif item == "создать_список":
                        создать_список()
                    elif item == "добавить_функцию_в_список":
                        # Для выполнения этой функции нам нужно 2 значения из стека
                        # В RPN: сначала аргументы, потом операция, т.е. [arg1, arg2, func]
                        # При обработке мы достаем аргументы в обратном порядке
                        if len(stack) >= 2:
                            list_idx = int(stack.pop())  # последний добавленный - это list_index
                            func_idx = int(stack.pop())  # предпоследний - это func_index
                            добавить_функцию_в_список(func_idx, list_idx)
                    elif item == "выполнить_список":
                        # Для выполнения этой функции нам нужно 1 значение из стека
                        if len(stack) >= 1:
                            list_idx = int(stack.pop())
                            выполнить_список(list_idx)  # используем текущее время для внутреннего вызова
                else:
                    # Добавляем элемент в стек
                    stack.append(item)
        else:
            # Индекс списка вне диапазона
            я['изменения'].append([-1, list_index, timestamp])
    except Exception as e:
        # Ловим любые другие исключения и записываем в изменения
        я['изменения'].append([-1, list_index, timestamp])

def сообщение_системе(message, timestamp=None):
    """API function for users to send messages to the system"""
    # Устанавливаем timestamp, если он не передан
    if timestamp is None:
        timestamp = int(time.time() * 1000)  # текущее время в миллисекундах

    # Добавляем сообщение в изменения в формате [0, message, timestamp]
    я['изменения'].append([0, message, timestamp])

def реакция_пользователя(list_index, оценка, timestamp=None):
    """API function for users to provide feedback on executed lists"""
    # Устанавливаем timestamp, если он не передан
    if timestamp is None:
        timestamp = int(time.time() * 1000)  # текущее время в миллисекундах

    # Добавляем реакцию пользователя в изменения в формате [event_code, list_index, оценка, timestamp]
    я['изменения'].append([1, list_index, оценка, timestamp])

я = {
    'данные': [["напечатать_привет", "напечатать_пока", "создать_список", "добавить_функцию_в_список", "выполнить_список"]],
    'контексты': [],
    'наблюдения': [],
    'гипотезы': [],
    'действия': [],
    'изменения': [],
    'приятно': 0.5
}

# Пример использования:
# создать_список()  # создаст новый пустой список в данные
# добавить_функцию_в_список(0, 1)  # добавит функцию с индексом 0 во второй список (индекс 1)
# выполнить_список(1)  # выполнит команды из списка с индексом 1