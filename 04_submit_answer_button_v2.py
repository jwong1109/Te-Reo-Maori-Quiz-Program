# Continue with submitting answer for easy questions first

# Developed the command in the multiple choices and the Submit Button and Test
# Answer Function

# It should print in python the answer pressed, correct answer, and the mark
# for easy questions

from tkinter import *
import random

# Root Window - from 01_setup_interface_v4.py
root = Tk()
root.title("Te Reo Maori Months Quiz")
root.geometry("600x700")
root.configure(bg="#FF7200")


class Questions:  # from 02_setup_questions_v4.py
    def __init__(self, eng_month, maori_month, numeric_month):
        self.eng_month = eng_month
        self.maori_month = maori_month
        self.numeric_month = numeric_month
        questions.append(self)


def random_question_generator(difficulty):  # from
    # 03_getting_answer_input_v3_trial2.py
    current_question = []
    eng_month_choices = []
    maori_month_choices = []
    for month in questions:
        eng_month_choices.append(month.eng_month)
        maori_month_choices.append(month.maori_month)
    random_month = random.choice(eng_month_choices)
    for month in questions:
        if month.eng_month == random_month:
            current_question.append(month.eng_month)
            current_question.append(month.maori_month)
            current_question.append(month.numeric_month)
            eng_month_choices.remove(random_month)
            maori_month_choices.remove(month.maori_month)

    # Easy Level
    random_option_1 = random.choice(eng_month_choices)
    eng_month_choices.remove(random_option_1)
    random_option_2 = random.choice(eng_month_choices)
    eng_month_choices.remove(random_option_2)
    random_option_3 = random.choice(eng_month_choices)
    eng_month_choices.remove(random_option_3)

    question_details = current_question, \
        random_option_1, random_option_2, random_option_3
    return question_details


# Easy ask function - from 03_getting_answer_input_v3_trial2.py
def easy_ask():
    ask_details = random_question_generator("Easy")
    ask_question = f"What is the month '{ask_details[0][1]}' \nin English?"
    question_label = Label(root, bg="#FF7200", fg="black",
                           text=ask_question,
                           font=("Arial", 20))
    question_label.grid(column=3, row=1, columnspan=3,
                        pady=20)
    get_answer("Easy", ask_details[0], ask_details[1], ask_details[2],
               ask_details[3])


# Get answer input - from 03_getting_answer_input_v3_trial2.py
def get_answer(difficulty, correct, random1, random2, random3):
    if difficulty == "Easy":
        correct_month = correct[0]
        place_correct_month = random.randint(1, 4)
        correct_choice = Button(root, bg="black", fg="white",
                                text=correct_month,
                                font=("Arial", 17), command=lambda:
                                submit_answer("Correct", correct_month,
                                              correct_month))
        incorrect_choice_1 = Button(root, bg="red", fg="white", text=random1,
                                    font=("Arial", 17), command=lambda:
                                    submit_answer("Incorrect", random1,
                                                  correct_month))
        incorrect_choice_2 = Button(root, bg="red", fg="white", text=random2,
                                    font=("Arial", 17), command=lambda:
                                    submit_answer("Incorrect", random2,
                                                  correct_month))
        incorrect_choice_3 = Button(root, bg="red", fg="white", text=random3,
                                    font=("Arial", 17), command=lambda:
                                    submit_answer("Incorrect", random3,
                                                  correct_month))

        if place_correct_month == 1:
            correct_choice.grid(column=3, row=2, ipadx=10, sticky=W, ipady=30)
            incorrect_choice_1.grid(column=4, row=2, ipadx=10, sticky=W,
                                    ipady=30)
            incorrect_choice_2.grid(column=3, row=3, ipadx=10, sticky=W,
                                    ipady=30)
            incorrect_choice_3.grid(column=4, row=3, ipadx=10, sticky=W,
                                    ipady=30)
        elif place_correct_month == 2:
            correct_choice.grid(column=4, row=2, ipadx=10, sticky=W, ipady=30)
            incorrect_choice_1.grid(column=3, row=2, ipadx=10, sticky=W,
                                    ipady=30)
            incorrect_choice_2.grid(column=3, row=3, ipadx=10, sticky=W,
                                    ipady=30)
            incorrect_choice_3.grid(column=4, row=3, ipadx=10, sticky=W,
                                    ipady=30)
        elif place_correct_month == 3:
            correct_choice.grid(column=3, row=3, ipadx=10, sticky=W, ipady=30)
            incorrect_choice_1.grid(column=3, row=2, ipadx=10, sticky=W,
                                    ipady=30)
            incorrect_choice_2.grid(column=4, row=2, ipadx=10, sticky=W,
                                    ipady=30)
            incorrect_choice_3.grid(column=4, row=3, ipadx=10, sticky=W,
                                    ipady=30)
        elif place_correct_month == 4:
            correct_choice.grid(column=4, row=3, ipadx=10, sticky=W, ipady=30)
            incorrect_choice_1.grid(column=3, row=2, ipadx=10, sticky=W,
                                    ipady=30)
            incorrect_choice_2.grid(column=4, row=2, ipadx=10, sticky=W,
                                    ipady=30)
            incorrect_choice_3.grid(column=3, row=3, ipadx=10, sticky=W,
                                    ipady=30)


# Submit Button
def submit_answer(status, answer_pressed, correct):
    submit_button = Button(root, bg="blue", fg="white", text="Submit",
                           font=("Arial", 20), command=lambda: test_answer(
                                 status, answer_pressed, correct))
    submit_button.grid(column=4, row=5, sticky=NW, ipadx=5)


# Test Answer
def test_answer(mark, user_answer, correct_answer):
    print(f"ANSWER PRESSED: {user_answer}")
    print(f"CORRECT ANSWER: {correct_answer}")
    print(f"MARK: {mark}!")


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

# Easy Button - from 02_setup_questions_v4.py
easy_button = Button(root, bg="red", fg="black", text="EASY",
                     font=("Arial", 20), command=easy_ask)
easy_button.grid(column=0, row=4, sticky=N, ipadx=10, ipady=10, padx=5)

root.mainloop()
