# Trial 2: Creating Centre Title Label + Instructions on the left
# + easy, hard buttons using grid

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
easy_button.grid(column=0, row=3, sticky=N, ipadx=10, ipady=10, padx=10)

hard_button = Label(root, bg="black", fg="white", text="HARD",
                    font=("Arial", 20))
hard_button.grid(column=1, row=3, sticky=N, ipadx=10, ipady=10, padx=10)

root.mainloop()
