# Added 01_setup_interface_v4.py

# Import Statements
from tkinter import *

# Root Window
root = Tk()
root.title("Te Reo Maori Months Quiz")
root.geometry("600x700")
root.configure(bg="#FF7200")

# Questions Class

# Functions go here

# Random month generator function

# Easy ask function

# Hard ask function

# Submit answer function

# Feedback function

# Final score function

# Export record of score, questions, and answers to text file function

# ******** Main Routine ********

# Necessary Lists and Variables

# Add Questions to Class

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
easy_button = Label(root, bg="red", fg="white", text="EASY",
                    font=("Arial", 20))
easy_button.grid(column=0, row=4, sticky=N, ipadx=10, ipady=10, padx=5)

hard_button = Label(root, bg="black", fg="white", text="HARD",
                    font=("Arial", 20))
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

# Question Label
question_label = Label(root, bg="#FF7200", fg="black",
                       text="Question 1: What is July in \nTe Reo Maori?",
                       font=("Arial", 20))
question_label.grid(column=3, row=1, columnspan=3,
                    pady=20)

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
