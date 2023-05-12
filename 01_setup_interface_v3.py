# Based on 01_setup_interface_v2_trial2.py, used labels to represent the
# position of the score tracker and a white line separating the left and the
# right of the GUI interface

from tkinter import *

# Root Window
root = Tk()
root.title("Te Reo Maori Months Quiz")
root.geometry("600x700")
root.configure(bg="#FF7200")

# Comic Book Store Label
title_label = Label(root, bg="red", fg="black", text="Te Reo Maori Months "
                                                     "Quiz",
                    font=("Arial", 30, "bold"))
title_label.grid(column=1, columnspan=3, row=0, sticky=N)

# Instructions on the left
instructions_label = Label(root, bg="red", fg="black",
                           text="Use this 12 questions quiz \n to test your "
                                "knowledge of\n months in the Te Reo\n "
                                "Maori language.\n \nYou can select below "
                                "an\n easy quiz or a hard quiz.",
                           font=("Arial", 20))
instructions_label.grid(column=0, row=2, columnspan=2, sticky=W, pady=100)

# Easy and Hard Buttons

easy_button = Label(root, bg="red", fg="white", text="EASY",
                    font=("Arial", 20))
easy_button.grid(column=0, row=3, sticky=N, ipadx=10, ipady=10, padx=5)

hard_button = Label(root, bg="black", fg="white", text="HARD",
                    font=("Arial", 20))
hard_button.grid(column=1, row=3, sticky=N, ipadx=10, ipady=10, padx=5)

# Score Tracker
score_tracker = Label(root, bg="#FF7200", fg="white", text="Score Tracker",
                      font=("Arial", 20))
score_tracker.grid(column=0, row=4, columnspan=2, sticky=N, pady=50)

correct_tracker = Label(root, bg="#FF7200", fg="light green", text="1 Correct",
                        font=("Arial", 20))
correct_tracker.grid(column=0, row=5, sticky=N)

incorrect_tracker = Label(root, bg="white", fg="red", text="0 Incorrect",
                          font=("Arial", 20))
incorrect_tracker.grid(column=1, row=5, sticky=N)

# White line separating the instructions and the questions
white_line = Label(root, bg="white", fg="white", text="a",
                   font=("Arial", 1))
white_line.grid(column=2, row=1, rowspan=5, sticky=NW, ipady=225, pady=30)

root.mainloop()
