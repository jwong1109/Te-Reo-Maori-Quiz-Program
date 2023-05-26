# TO BE CONTINUED... Given buttons to try the quiz again or quit the quiz

from tkinter import *
import random
import subprocess
import os
import platform

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
    random_month = random.choice(eng_months_questions)
    for month in questions:
        if month.eng_month == random_month:
            current_question.append(month.eng_month)
            current_question.append(month.maori_month)
            current_question.append(month.numeric_month)
            eng_months_questions.remove(random_month)
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
def easy_ask(track_questions):
    ask_details = random_question_generator("Easy")
    ask_question = f"What is the month '{ask_details[0][1]}' \nin English?"
    easy_question_label = Label(root, bg="#FF7200", fg="black",
                                text=ask_question,
                                font=("Arial", 20))
    easy_question_label.grid(column=3, row=1, columnspan=3,
                             pady=20)
    get_answer("Easy", ask_details[0], ask_details[1], ask_details[2],
               ask_details[3], track_questions, easy_question_label)


# Hard ask function - from 02_setup_questions_v4.py
def hard_ask(track_questions):
    ask_details = random_question_generator("Hard")
    ask_question = f"What is the month '{ask_details[0][0]}' \nin Te Reo " \
                   f"Maori?"
    hard_question_label = Label(root, bg="#FF7200", fg="black",
                                text=ask_question,
                                font=("Arial", 20))
    hard_question_label.grid(column=3, row=1, columnspan=3,
                             pady=20)
    get_answer("Hard", ask_details[0], ask_details[1], ask_details[2],
               ask_details[3], track_questions, hard_question_label)


# Get answer input
def get_answer(difficulty, correct, random1, random2, random3,
               questions_track, question_label):
    if difficulty == "Easy":
        correct_month = correct[0]
        place_correct_month = random.randint(1, 4)
        correct_choice = Button(root, bg="black", fg="black",
                                text=correct_month,
                                font=("Arial", 17), command=lambda:
                                submit_answer(difficulty, "Correct",
                                              correct_month,
                                              correct_month,
                                              questions_track,
                                              [correct_choice,
                                               incorrect_choice_1,
                                               incorrect_choice_2,
                                               incorrect_choice_3],
                                              question_label))
        incorrect_choice_1 = Button(root, bg="red", fg="black", text=random1,
                                    font=("Arial", 17), command=lambda:
                                    submit_answer(difficulty, "Incorrect",
                                                  random1,
                                                  correct_month,
                                                  questions_track,
                                                  [correct_choice,
                                                   incorrect_choice_1,
                                                   incorrect_choice_2,
                                                   incorrect_choice_3],
                                                  question_label))
        incorrect_choice_2 = Button(root, bg="red", fg="black", text=random2,
                                    font=("Arial", 17), command=lambda:
                                    submit_answer(difficulty, "Incorrect",
                                                  random2,
                                                  correct_month,
                                                  questions_track,
                                                  [correct_choice,
                                                   incorrect_choice_1,
                                                   incorrect_choice_2,
                                                   incorrect_choice_3],
                                                  question_label))
        incorrect_choice_3 = Button(root, bg="red", fg="black", text=random3,
                                    font=("Arial", 17), command=lambda:
                                    submit_answer(difficulty, "Incorrect",
                                                  random3,
                                                  correct_month,
                                                  questions_track,
                                                  [correct_choice,
                                                   incorrect_choice_1,
                                                   incorrect_choice_2,
                                                   incorrect_choice_3],
                                                  question_label))

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
        submit_answer(difficulty, "CHECK", clicked, correct_month,
                      questions_track, select_dropdown, question_label)


# Submit Button
def submit_answer(level, status, answer_pressed, correct, track,
                  answer_type, label_question):
    submit_button = Button(root, bg="blue", fg="black", text="Submit",
                           font=("Arial", 20), command=lambda: [test_answer(
                                 level, status, answer_pressed, correct,
                                 track, answer_type, label_question),
                            submit_button.destroy()])
    submit_button.grid(column=4, row=5, sticky=NW, ipadx=5)


# Test Answer
def test_answer(quiz_difficulty, mark, user_answer, correct_answer, track,
                type_answer, question_quiz):
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

        for month in questions:
            if correct_answer == month.eng_month or correct_answer == \
                    month.maori_month:
                correct_questions.append([month.eng_month,
                                          month.maori_month,
                                          user_answer, track+1, quiz_difficulty])
                print("CORRECT QUESTIONS:")  # for testing purposes
                print(correct_questions)  # for testing purposes
    else:
        feedback = Label(root, bg="black",
                         fg="red", text="Incorrect! \nThe answer was: \n"
                            f"{correct_answer}",
                         font=("Arial", 20))
        feedback.grid(column=3, row=5, sticky=NW)
        num_incorrect.set(num_incorrect.get() + 1)

        for month in questions:
            if correct_answer == month.eng_month or correct_answer == \
                    month.maori_month:
                incorrect_questions.append([month.eng_month,
                                           month.maori_month,
                                            user_answer, track+1, quiz_difficulty])
                print("INCORRECT QUESTIONS:")  # for testing purposes
                print(incorrect_questions)  # for testing purposes

    track += 1
    feedback.after(3000, feedback.destroy)

    next_question(quiz_difficulty, track, type_answer, question_quiz)


def next_question(quiz, questions_track, answer_input, question):
    if quiz == "Easy":
        question.destroy()
        for choice in answer_input:
            choice.destroy()
        if questions_track != 12:
            easy_ask(questions_track)
    else:
        question.destroy()
        answer_input.destroy()
        if questions_track != 12:
            hard_ask(questions_track)

    if questions_track == 12:
        finish_quiz(quiz)


def finish_quiz(quiz_level):
    easy_button.destroy()
    hard_button.destroy()

    incorrect = Label(root, bg="white", fg="red",
                      text="MONTHS TO IMPROVE:", font=("Arial", 20))
    incorrect.grid(column=1, row=8, sticky=N, pady=10)

    placement = 9
    for question in incorrect_questions:
        improve = Label(root, bg="white", fg="red",
                        text=f"Question {question[3]}: {question[0]} ="
                             f" {question[1]}",
                        font=("Arial", 16))
        improve.grid(column=1, row=placement, sticky=N, pady=3)
        placement += 1

    export_file(quiz_level)


def export_file(quiz_type):
    list_correct = []
    list_incorrect = []
    for question in correct_questions:
        if question[4] == "Easy":
            record_question = f"Q{question[3]}: {question[1]} in " \
                              f"English? (You selected the CORRECT " \
                              f"answer: " \
                              f"{question[0].upper()})"
            list_correct.append(record_question)
        else:
            record_question = f"Q{question[3]}: {question[0]} in " \
                              f"Maori? (You selected the CORRECT answer: " \
                              f"{question[1].upper()})"
            list_correct.append(record_question)

    for question in incorrect_questions:
        if question[4] == "Easy":
            record_question = f"Q{question[3]}: {question[1]} in " \
                              f"English? \n  Your incorrect answer: " \
                              f"{question[2]}. The CORRECT answer: " \
                              f"{question[0].upper()}."
            list_incorrect.append(record_question)
        else:
            record_question = f"Q{question[3]}: {question[0]} in " \
                              f"Maori? \n  Your incorrect answer: " \
                              f"{question[2]}. The CORRECT answer: " \
                              f"{question[1].upper()}"
            list_incorrect.append(record_question)

    record_file = open("Questions_Record.txt", 'w')
    record_file.write(f"Final SCORE for your "
                      f"{quiz_type.upper()} "
                      f"Quiz:"
                      f" {len(correct_questions)}/12\n\n"
                      f"Questions answered correctly: \n")
    record_file.close()
    for record in list_correct:
        record_file = open("Questions_Record.txt", 'a')
        record_file.write(f"{record}\n")
        record_file.close()

    record_file = open("Questions_Record.txt", 'a')
    record_file.write(f"\nQuestions answered incorrectly: \n")
    record_file.close()

    for record in list_incorrect:
        record_file = open("Questions_Record.txt", 'a')
        record_file.write(f"{record}\n")
        record_file.close()

    directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(directory, 'Questions_Record.txt')

    computer_system = platform.system()
    if computer_system == 'Windows':
        os.startfile(file_path)
    else:
        subprocess.call(['open', file_path])


questions = []
incorrect_questions = []
correct_questions = []
print(incorrect_questions)
print(correct_questions)
num_questions = 0
eng_months_questions = []

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

for detail in questions:
    eng_months_questions.append(detail.eng_month)

# Easy and Hard Buttons - from 02_setup_questions_v4.py
easy_button = Button(root, bg="red", fg="black", text="EASY",
                     font=("Arial", 20), command=lambda:
                     easy_ask(num_questions))
easy_button.grid(column=0, row=4, sticky=N, ipadx=10, ipady=10, padx=5)

hard_button = Button(root, bg="black", fg="black", text="HARD",
                     font=("Arial", 20), command=lambda:
                     hard_ask(num_questions))
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
