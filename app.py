# app.py
import gradio as gr
from quiz_core import QUESTIONS, check_answer

score = 0
current_question = 0

def quiz_app(user_answer):
    global current_question, score

    if current_question == 0:
        current_question += 1
        q = QUESTIONS[current_question - 1]
        return f"🐍 Добро пожаловать в SkillTest Python Quiz!\n\n{q['question']}", gr.Radio(q["options"])

    q = QUESTIONS[current_question - 1]
    feedback = ""
    if check_answer(user_answer, q["correct"]):
        score_feedback = "✅ Правильно!"
        score_plus = 1
    else:
        score_feedback = "❌ Неправильно."
        feedback = f"\n💡 Подсказка: {q['hint']}"
        score_plus = 0

    score += score_plus

    if current_question < len(QUESTIONS):
        current_question += 1
        next_q = QUESTIONS[current_question - 1]
        return (
            f"{score_feedback}{feedback}\n\nСледующий вопрос:\n\n{next_q['question']}",
            gr.Radio(next_q["options"])
        )
    else:
        if score <= 2:
            level = "Beginner 🐣"
        elif score <= 3:
            level = "Intermediate 💡"
        else:
            level = "Advanced 🎉"

        result = f"{score_feedback}{feedback}\n\n📊 Результаты:\nБаллы: {score}/{len(QUESTIONS)}\nВаш уровень: {level}"
        current_question = 0
        score = 0
        return result, gr.Textbox(label="Введите 'старт' для новой игры")

interface = gr.Interface(
    fn=quiz_app,
    inputs=gr.Textbox(label="Ваш ответ или 'старт' для начала"),
    outputs=[gr.Textbox(label="Сообщение"), gr.Component()],
    title="🐍 SkillTest Python Quiz",
    description="Мини-тест для проверки знаний Python. Пройди и узнай свой уровень!",
)

if __name__ == "__main__":
    interface.launch()
