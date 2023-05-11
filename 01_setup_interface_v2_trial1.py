# Trial 1: Creating Centre Title Label + Instructions on the left
# + easy, hard buttons using pack

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
title_label.pack()

# Instructions on the left
instructions_label = Label(root, bg="red", fg="black",
                           text="Use this 12 questions quiz \n to test your "
                                "knowledge of\n months in the Te Reo\n "
                                "Maori language.\n \nYou can select below "
                                "an\n easy quiz or a hard quiz.",
                           font=("Arial", 20))
instructions_label.pack(side=TOP, anchor=W, pady=100)

# Easy and Hard Buttons

easy_button = Label(root, bg="red", fg="white", text="EASY",
                    font=("Arial", 20))
easy_button.pack(side=LEFT, anchor=N, ipadx=10, ipady=10, padx=20)

hard_button = Label(root, bg="black", fg="white", text="HARD",
                    font=("Arial", 20))
hard_button.pack(side=LEFT, anchor=N, ipadx=10, ipady=10, padx=20)

root.mainloop()
