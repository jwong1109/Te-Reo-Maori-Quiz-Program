# If the user's answer is correct, to add 1 to the correct count
# If the user's answer is incorrect, to add 1 to the incorrect count

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


# Add the Maori months to the months dropdown - from
# 03_getting_answer_input_v3_trial2.py
def months_dropdown():
    maori_months_choices = []
    for month in questions:
        maori_months_choices.append(month.maori_month)
    random.shuffle(maori_months_choices)
    return maori_months_choices


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

    if difficulty == "Easy":
        random_option_1 = random.choice(eng_month_choices)
        eng_month_choices.remove(random_option_1)
        random_option_2 = random.choice(eng_month_choices)
        eng_month_choices.remove(random_option_2)
        random_option_3 = random.choice(eng_month_choices)
        eng_month_choices.remove(random_option_3)
    else:
        random_option_1 = random.choice(maori_month_choices)
        maori_month_choices.remove(random_option_1)
        random_option_2 = random.choice(maori_month_choices)
        maori_month_choices.remove(random_option_2)
        random_option_3 = random.choice(maori_month_choices)
        maori_month_choices.remove(random_option_3)

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


# Hard ask function - from 02_setup_questions_v4.py
def hard_ask():
    ask_details = random_question_generator("Hard")
    ask_question = f"What is the month '{ask_details[0][0]}' \nin Te Reo " \
                   f"Maori?"
    question_label = Label(root, bg="#FF7200", fg="black",
                           text=ask_question,
                           font=("Arial", 20))
    question_label.grid(column=3, row=1, columnspan=3,
                        pady=20)
    get_answer("Hard", ask_details[0], ask_details[1], ask_details[2],
               ask_details[3])


# Get answer input - from 03_getting_answer_input_v3_trial2.py
def get_answer(difficulty, correct, random1, random2, random3):
    if difficulty == "Easy":
        correct_month = correct[0]
        place_correct_month = random.randint(1, 4)
        correct_choice = Button(root, bg="black", fg="black",
                                text=correct_month,
                                font=("Arial", 17), command=lambda:
                                submit_answer("Correct", correct_month,
                                              correct_month))
        incorrect_choice_1 = Button(root, bg="red", fg="black", text=random1,
                                    font=("Arial", 17), command=lambda:
                                    submit_answer("Incorrect", random1,
                                                  correct_month))
        incorrect_choice_2 = Button(root, bg="red", fg="black", text=random2,
                                    font=("Arial", 17), command=lambda:
                                    submit_answer("Incorrect", random2,
                                                  correct_month))
        incorrect_choice_3 = Button(root, bg="red", fg="black", text=random3,
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
    else:
        correct_month = correct[1]
        clicked = StringVar()
        clicked.set("Select Maori Month...")
        months_options = months_dropdown()
        select_dropdown = OptionMenu(root, clicked, *months_options)
        select_dropdown.config(bg="red")
        select_dropdown.grid(column=4, row=2, ipadx=10, sticky=W, ipady=10)
        submit_answer("CHECK", clicked, correct_month)


# Submit Button - from 04_submit_answer_button_v3.py
def submit_answer(status, answer_pressed, correct):
    submit_button = Button(root, bg="blue", fg="black", text="Submit",
                           font=("Arial", 20), command=lambda: test_answer(
                                 status, answer_pressed, correct))
    submit_button.grid(column=4, row=5, sticky=NW, ipadx=5)


# Test Answer - from 04_submit_answer_button_v3.py
def test_answer(mark, user_answer, correct_answer):
    if mark == "CHECK":
        user_answer = user_answer.get()
    if user_answer == correct_answer:
        mark = "Correct"
    else:
        mark = "Incorrect"

    if mark == "Correct":
        # from 01_setup_interface_v4.py
        feedback = Label(root, bg="#FF7200", fg="light green", text="Correct!",
                         font=("Arial", 20))
        feedback.grid(column=3, row=5, sticky=NW)
        num_correct.set(num_correct.get() + 1)
    else:
        feedback = Label(root, bg="black",
                         fg="red", text="Incorrect! \nThe answer was: \n"
                            f"{correct_answer}",
                         font=("Arial", 20))
        feedback.grid(column=3, row=5, sticky=NW)
        num_incorrect.set(num_incorrect.get() + 1)


questions = []
num_questions = 0

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

# Easy and Hard Buttons - from 02_setup_questions_v4.py
easy_button = Button(root, bg="red", fg="black", text="EASY",
                     font=("Arial", 20), command=easy_ask)
easy_button.grid(column=0, row=4, sticky=N, ipadx=10, ipady=10, padx=5)

hard_button = Button(root, bg="black", fg="black", text="HARD",
                     font=("Arial", 20), command=hard_ask)
hard_button.grid(column=1, row=4, sticky=N, ipadx=10, ipady=10, padx=5)

# Score Tracker - labels from 01_setup_interface_v4.py
score_tracker = Label(root, bg="#FF7200", fg="white", text="Score Tracker",
                      font=("Arial", 20))
score_tracker.grid(column=0, row=6, columnspan=2, sticky=N, pady=5)

num_correct = IntVar()
num_correct.set(0)

correct_label = Label(root, bg="#FF7200", fg="light green", text="Correct",
                      font=("Arial", 20))
correct_label.grid(column=0, row=7, sticky=N)

correct_num = Label(root, bg="#FF7200", fg="light green",
                    textvariable=num_correct, font=("Arial", 20))
correct_num.grid(column=1, row=7, sticky=N)

num_incorrect = IntVar()
num_incorrect.set(0)

incorrect_label = Label(root, bg="white", fg="red", text="Incorrect",
                        font=("Arial", 20))
incorrect_label.grid(column=2, row=7, sticky=N)

incorrect_num = Label(root, bg="white", fg="red",
                      textvariable=num_incorrect, font=("Arial", 20))
incorrect_num.grid(column=3, row=7, sticky=N)

root.mainloop()
