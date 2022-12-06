from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create a list of objects of the Question class based on the question_data list.
question_bank = []
# Defines the attributes of the object as the correspondent items in the dictionary inside the list.
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Create an object to the QuizBrain class and keeps asking quizzing the user until there is no question left.
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
    print()

# Once the quiz is over, it shows the user the final score.
print("\nYou've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")
