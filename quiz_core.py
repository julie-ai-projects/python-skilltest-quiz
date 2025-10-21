# quiz_core.py

def check_answer(user_answer, correct_answer):
    return user_answer.strip().lower() == correct_answer.strip().lower()

def ask_question(question, options=None, correct=None, hint=None):
    return {"question": question, "options": options, "correct": correct, "hint": hint}

QUESTIONS = [
    ask_question(
        "Что делает функция len() в Python?",
        ["Возвращает длину объекта", "Преобразует строку в число", "Создает список", "Удаляет элемент"],
        correct="Возвращает длину объекта",
        hint="Функция len() возвращает длину строки, списка или словаря."
    ),
    ask_question(
        "Какой результат выражения 3 * 'hi' ?",
        ["'hi3'", "'hi hi hi'", "'hihihi'", "Ошибка"],
        correct="'hihihi'",
        hint="Оператор * повторяет строку указанное количество раз."
    ),
    ask_question(
        "Как создать список чисел от 0 до 4 включительно?",
        ["list(0, 4)", "range(0, 4)", "list(range(5))", "[0, 1, 2, 3, 4]"],
        correct="list(range(5))",
        hint="range(5) создаёт последовательность чисел от 0 до 4."
    ),
    ask_question(
        "Что выведет код: x = [1, 2, 3]; print(x[-1])",
        ["1", "2", "3", "Ошибка"],
        correct="3",
        hint="Отрицательный индекс -1 возвращает последний элемент списка."
    ),
]
