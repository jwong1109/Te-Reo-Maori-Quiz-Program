# Trial 2: Create a random month question generator function using a random
# choice from the list itself

import random


class Questions:
    def __init__(self, eng_month, maori_month, numeric_month):
        self.eng_month = eng_month
        self.maori_month = maori_month
        self.numeric_month = numeric_month
        questions.append(self)


def random_question_generator():
    month_choices = []
    for month in questions:
        month_choices.append(month.eng_month)
    random_month = random.choice(month_choices)
    for month in questions:
        if month.eng_month == random_month:
            current_question.append(month.eng_month)
            current_question.append(month.maori_month)
            current_question.append(month.numeric_month)
            return current_question


current_question = []
questions = []
num_questions = 0
num_correct = 0

Questions("January", "Kohi-tātea", 1)
Questions("February", "Hui-tanguru", 2)
Questions("March", "Poutū-te-rangi", 3)
Questions("April", "Paenga-whāwhā", 4)
Questions("May", "Haratua", 5)
Questions("June", "Pipiri", 6)
Questions("July", "Hōngongoi", 7)
Questions("August", "Here-turi-kōkā", 8)
Questions("September", "Mahuru", 9)
Questions("October", "Whiringa-ā-nuku", 10)
Questions("November", "Whiringa-ā-rangi", 11)
Questions("December", "Hakihea", 12)

# For testing purposes
print(random_question_generator())
