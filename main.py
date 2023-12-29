from question_model import Question
from data import question_data
from quiz_brain import Quiz
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

#print(question_bank)
# print(question_bank[0].text) # The HTML5 standard was published in 2014.
# print(question_bank[0].answer) # True
quiz = Quiz(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz !")
print(f"Your final score is {quiz.score} / {quiz.question_number}")

