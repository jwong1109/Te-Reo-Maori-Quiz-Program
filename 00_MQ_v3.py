# Added 02_setup_questions_v4.py

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


# Random Question Generator
def random_question_generator():
    current_question = []
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


# Easy ask function
def easy_ask():
    ask_details = random_question_generator()
    ask_question = f"What is the month '{ask_details[1]}' \nin English?"
    question_label = Label(root, bg="#FF7200", fg="black",
                           text=ask_question,
                           font=("Arial", 20))
    question_label.grid(column=3, row=1, columnspan=3,
                        pady=20)


# Hard ask function
def hard_ask():
    ask_details = random_question_generator()
    ask_question = f"What is the month '{ask_details[0]}' \nin Te Reo Maori?"
    question_label = Label(root, bg="#FF7200", fg="black",
                           text=ask_question,
                           font=("Arial", 20))
    question_label.grid(column=3, row=1, columnspan=3,
                        pady=20)

# Submit answer function

# Feedback function

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


# Multiple Choice Buttons
choice1 = Label(root, bg="black", fg="white", text="Hōngongoi",
                font=("Arial", 17))
choice1.grid(column=3, row=2, ipadx=10, sticky=W, ipady=30)

choice2 = Label(root, bg="red", fg="white", text="Pipiri",
                font=("Arial", 17))
choice2.grid(column=4, row=2, ipadx=10, sticky=W, ipady=30)

choice3 = Label(root, bg="red", fg="white", text="Haratua",
                font=("Arial", 17))
choice3.grid(column=3, row=3, ipadx=10, sticky=W, ipady=30)

choice4 = Label(root, bg="red", fg="white", text="Hakihea",
                font=("Arial", 17))
choice4.grid(column=4, row=3, ipadx=10, sticky=W, ipady=30)

# Feedback
feedback = Label(root, bg="#FF7200", fg="light green", text="Correct!",
                 font=("Arial", 20))
feedback.grid(column=3, row=5, sticky=NW)

# Submit answer button
submit_button = Label(root, bg="blue", fg="white", text="Submit",
                      font=("Arial", 20))
submit_button.grid(column=4, row=5, sticky=NW, ipadx=5)

# Finish Quiz

root.mainloop()
