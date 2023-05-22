# Added 04_submit_answer_button_v3.py

# Import Statements
from tkinter import *
import random

# Root Window
root = Tk()
root.title("Te Reo Maori Months Quiz")
root.geometry("600x700")
root.configure(bg="#FF7200")


# Questions Class
class Questions:
    def __init__(self, eng_month, maori_month, numeric_month):
        self.eng_month = eng_month
        self.maori_month = maori_month
        self.numeric_month = numeric_month
        questions.append(self)


# Add the Maori months to the months dropdown
def months_dropdown():
    maori_months_choices = []
    for month in questions:
        maori_months_choices.append(month.maori_month)
    random.shuffle(maori_months_choices)
    return maori_months_choices


# Random Question Generator
def random_question_generator(difficulty):
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


# Easy ask function
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


# Hard ask function
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


# Get answer input - the multiple choices temporarily as labels
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
        select_dropdown.grid(column=3, row=2, ipadx=10, sticky=W, ipady=10)
        submit_answer("CHECK", clicked, correct_month)


# Submit answer function
def submit_answer(status, answer_pressed, correct):
    submit_button = Button(root, bg="blue", fg="black", text="Submit",
                           font=("Arial", 20), command=lambda: test_answer(
                                 status, answer_pressed, correct))
    submit_button.grid(column=4, row=5, sticky=NW, ipadx=5)


# Feedback function
# Test Answer
def test_answer(mark, user_answer, correct_answer):
    if mark == "CHECK":
        user_answer = user_answer.get()
    if user_answer == correct_answer:
        mark = "Correct"
    else:
        mark = "Incorrect"
    print(f"ANSWER PRESSED: {user_answer}")
    print(f"CORRECT ANSWER: {correct_answer}")
    print(f"MARK: {mark}!")


# Final score function

# Export record of score, questions, and answers to text file function

# ******** Main Routine ********

# Necessary Lists and Variables
questions = []
num_questions = 0
num_correct = 0

# Add Questions to Class
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

# Labels
# Comic Book Store Label
title_label = Label(root, bg="red", fg="black", text="Te Reo Maori Months "
                                                     "Quiz",
                    font=("Arial", 30, "bold"))
title_label.grid(column=1, columnspan=3, row=0, sticky=N, ipadx=10)

# Instructions on the left
instructions_label = Label(root, bg="red", fg="black",
                           text="Use this 12 questions quiz \n to test your "
                                "knowledge of\n months in the Te Reo\n "
                                "Maori language.\n \nYou can select below "
                                "an\n easy quiz or a hard quiz.",
                           font=("Arial", 20))
instructions_label.grid(column=0, row=2, columnspan=2, rowspan=2, ipady=5)

# Easy and Hard Button
easy_button = Button(root, bg="white", fg="red", text="EASY",
                     font=("Arial", 20), command=easy_ask)
easy_button.grid(column=0, row=4, sticky=N, ipadx=10, ipady=10, padx=5)

hard_button = Button(root, bg="white", fg="red", text="HARD",
                     font=("Arial", 20), command=hard_ask)
hard_button.grid(column=1, row=4, sticky=N, ipadx=10, ipady=10, padx=5)

# Score Tracker
score_tracker = Label(root, bg="#FF7200", fg="white", text="Score Tracker",
                      font=("Arial", 20))
score_tracker.grid(column=0, row=6, columnspan=2, sticky=N, pady=5)

correct_tracker = Label(root, bg="#FF7200", fg="light green", text="1 Correct",
                        font=("Arial", 20))
correct_tracker.grid(column=0, row=7, sticky=N)

incorrect_tracker = Label(root, bg="white", fg="red", text="0 Incorrect",
                          font=("Arial", 20))
incorrect_tracker.grid(column=1, row=7, sticky=N)

# White line separating the instructions and the questions
white_line = Label(root, bg="white", fg="white", text="a",
                   font=("Arial", 1))
white_line.grid(column=2, row=1, rowspan=5, sticky=NW, ipady=225, pady=30,
                padx=5)


# Finish Quiz

root.mainloop()
