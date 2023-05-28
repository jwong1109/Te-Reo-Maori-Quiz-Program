# Continue to act on the suggestions and feedback from usability testing:

# For the hard quiz, user cannot press Submit until they select a month from the dropdown.

# Give overall feedback based on the final score

# Import Statements
from tkinter import *
import random
import subprocess
import os
import platform

# Root Window
root = Tk()
root.title("Te Reo Maori Months Quiz")
root.geometry("700x700")
root.configure(bg="#FF7200")


# Questions Class
class Questions:
    def __init__(self, eng_month, maori_month, numeric_month):
        self.eng_month = eng_month
        self.maori_month = maori_month
        self.numeric_month = numeric_month
        questions.append(self)


def learn(num):
    learn_list = []
    placement = 10
    for month in questions:
        learn_month = Label(root, bg="white", fg="red",
                            text=f"{month.numeric_month}: {month.eng_month} = "
                                 f"{month.maori_month}",
                            font=("Arial", 16))
        learn_month.grid(column=1, row=placement, sticky=N, pady=3)
        placement += 1
        learn_list.append(learn_month)

    main_menu = Button(root, bg="black", fg="black", text="Main Menu",
                       font=("Arial", 20), command=lambda:
                       [delete_learn(learn_list), quiz_loop(num),
                        main_menu.destroy()])
    main_menu.grid(column=1, row=4, sticky=N, ipadx=10, ipady=10, padx=5)


def delete_learn(list_learn):
    for learning_month in list_learn:
        learning_month.destroy()


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


# Easy ask function
def easy_ask(track_questions):
    ask_details = random_question_generator("Easy")
    ask_question = f"What is the month\n '{ask_details[0][1]}' in English?"
    print(f"Easy: {ask_details[0][1]} in English?")  # for testing purposes
    easy_question_label = Label(root, bg="#FF7200", fg="black",
                                text=ask_question,
                                font=("Arial", 20))
    easy_question_label.grid(column=3, row=1, columnspan=3,
                             pady=20)
    get_answer("Easy", ask_details[0], ask_details[1], ask_details[2],
               ask_details[3], track_questions, easy_question_label)


# Hard ask function
def hard_ask(track_questions):
    ask_details = random_question_generator("Hard")
    ask_question = f"What is the month\n '{ask_details[0][0]}' in Te Reo " \
                   f"Maori?"
    print(f"Hard: {ask_details[0][0]} in Maori?")  # for testing purposes
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
                                test_answer(difficulty, "Correct",
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
                                    test_answer(difficulty, "Incorrect",
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
                                    test_answer(difficulty, "Incorrect",
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
                                    test_answer(difficulty, "Incorrect",
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
                                    ipady=30, pady=5)
            incorrect_choice_3.grid(column=4, row=3, ipadx=10, sticky=W,
                                    ipady=30, pady=5)
        elif place_correct_month == 2:
            correct_choice.grid(column=4, row=2, ipadx=10, sticky=W, ipady=30)
            incorrect_choice_1.grid(column=3, row=2, ipadx=10, sticky=W,
                                    ipady=30)
            incorrect_choice_2.grid(column=3, row=3, ipadx=10, sticky=W,
                                    ipady=30, pady=5)
            incorrect_choice_3.grid(column=4, row=3, ipadx=10, sticky=W,
                                    ipady=30, pady=5)
        elif place_correct_month == 3:
            correct_choice.grid(column=3, row=3, ipadx=10, sticky=W,
                                ipady=30, pady=5)
            incorrect_choice_1.grid(column=3, row=2, ipadx=10, sticky=W,
                                    ipady=30)
            incorrect_choice_2.grid(column=4, row=2, ipadx=10, sticky=W,
                                    ipady=30)
            incorrect_choice_3.grid(column=4, row=3, ipadx=10, sticky=W,
                                    ipady=30, pady=5)
        elif place_correct_month == 4:
            correct_choice.grid(column=4, row=3, ipadx=10, sticky=W,
                                ipady=30, pady=5)
            incorrect_choice_1.grid(column=3, row=2, ipadx=10, sticky=W,
                                    ipady=30)
            incorrect_choice_2.grid(column=4, row=2, ipadx=10, sticky=W,
                                    ipady=30)
            incorrect_choice_3.grid(column=3, row=3, ipadx=10, sticky=W,
                                    ipady=30, pady=5)

        main_menu = Button(root, bg="black", fg="black", text="Main Menu",
                           font=("Arial", 20), command=lambda: [
                            question_label.destroy(), correct_choice.destroy(),
                            incorrect_choice_1.destroy(), incorrect_choice_2.destroy(),
                            incorrect_choice_3.destroy(), quiz_loop(questions_track),
                            main_menu.destroy()])
        main_menu.grid(column=1, row=4, sticky=N, ipadx=10, ipady=10, padx=5)

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


# Submit answer function
def submit_answer(level, status, answer_pressed, correct, track,
                  answer_type, label_question):
    submit_button = Button(root, bg="blue", fg="black", text="Submit",
                           font=("Arial", 20), command=lambda: [not_blank(
                                 level, status, answer_pressed, correct,
                                 track, answer_type, label_question),
                            submit_button.destroy()])
    submit_button.grid(column=4, row=5, sticky=NW, ipadx=5)

    if level == "Hard":
        main_menu = Button(root, bg="black", fg="black", text="Main Menu",
                           font=("Arial", 20), command=lambda: [
                            label_question.destroy(),
                            answer_type.destroy(),
                            quiz_loop(track),
                            main_menu.destroy(),
                            submit_button.destroy()])
        main_menu.grid(column=1, row=4, sticky=N, ipadx=10, ipady=10, padx=5)


def not_blank(level, status, answer_pressed, correct,
              track, answer_type, label_question):
    if answer_pressed.get() == "Select Maori Month...":
        enter = Label(root, bg="black",
                      fg="red", text="Pls enter \na Maori month!",
                      font=("Arial", 20))
        enter.grid(column=5, row=5, sticky=W)
        enter.after(3000, enter.destroy)
        submit_answer(level, status, answer_pressed, correct,
                      track, answer_type, label_question)
    else:
        test_answer(level, status, answer_pressed, correct,
                    track, answer_type, label_question)


# Feedback function
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
        feedback.grid(column=3, row=5, sticky=W)
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
        feedback.grid(column=3, row=5, sticky=W)
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
        finish_quiz(quiz, questions_track)


# Finish the Quiz function
def finish_quiz(quiz_level, track_question_num):
    improve_questions = []
    track_question_num = 0

    if len(correct_questions) == 12:
        overall_feedback = Label(root, bg="#FF7200", fg="light green",
                                 text="Excellent! Perfect Score!",
                                 font=("Arial", 20))
        overall_feedback.grid(column=1, row=9, sticky=N, pady=10)
    elif 12 > len(correct_questions) >= 6:
        overall_feedback = Label(root, bg="#FF7200", fg="light green",
                                 text="Well Done! You passed!",
                                 font=("Arial", 20))
        overall_feedback.grid(column=1, row=9, sticky=N, pady=10)
    else:
        overall_feedback = Label(root, bg="black", fg="red",
                                 text="Oh no! You did not pass.\n Learn your "
                                      "months below \nto improve next time!",
                                 font=("Arial", 20))
        overall_feedback.grid(column=1, row=9, sticky=N, pady=10)

    if len(incorrect_questions) > 0:
        incorrect = Label(root, bg="white", fg="red",
                          text="MONTHS TO IMPROVE:", font=("Arial", 20))
        incorrect.grid(column=1, row=10, sticky=N, pady=10)

        placement = 11
        for question in incorrect_questions:
            improve = Label(root, bg="white", fg="red",
                            text=f"Question {question[3]}: {question[0]} ="
                                 f" {question[1]}",
                            font=("Arial", 16))
            improve.grid(column=1, row=placement, sticky=N, pady=3)
            placement += 1
            improve_questions.append(improve)

    export_file(quiz_level)
    # Option to Quit the Quiz or Restart the Quiz
    quit_button = Button(root, bg="red", fg="black", text="QUIT the quiz",
                         font=("Arial", 20), command=lambda: root.destroy())
    quit_button.grid(column=0, row=4, sticky=N, ipadx=10, ipady=10, padx=5)

    restart_button = Button(root, bg="black", fg="black", text="RESTART the "
                                                               "quiz",
                            font=("Arial", 20), command=lambda:
                            [quit_button.destroy(), restart_button.destroy(),
                             quiz_loop(track_question_num), incorrect.destroy(),
                             delete_improve_months(improve_questions),
                             overall_feedback.destroy()])
    restart_button.grid(column=1, row=4, sticky=N, ipadx=10, ipady=10, padx=5)


def delete_improve_months(improve_questions):
    for improve in improve_questions:
        improve.destroy()


# Export record of score, questions, and answers to text file function
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
                      f" {len(correct_questions)}/12\n\n")
    record_file.close()
    if len(correct_questions) > 0:
        record_file = open("Questions_Record.txt", 'a')
        record_file.write("Questions answered correctly: \n")
        record_file.close()

        for record in list_correct:
            record_file = open("Questions_Record.txt", 'a')
            record_file.write(f"{record}\n")
            record_file.close()

    if len(incorrect_questions) > 0:
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

    return


def quiz_loop(num_track):
    num_track = 0
    num_correct.set(0)
    num_incorrect.set(0)
    incorrect_questions.clear()
    correct_questions.clear()
    eng_months_questions.clear()

    for detail in questions:
        eng_months_questions.append(detail.eng_month)

    # Instructions on the left
    instructions_label = Label(root, bg="red", fg="black",
                               text="Use this 12 questions quiz \n to test "
                                    "your knowledge of\n "
                                    "months in the Te Reo\n "
                                    "Maori language.\n \nYou can learn "
                                    "first\n or select below "
                                    "an\n easy quiz or a hard quiz.",
                                    font=("Arial", 20))
    instructions_label.grid(column=0, row=1, columnspan=2, rowspan=3,
                            ipady=5, padx=30, pady=30)

    # White line separating the instructions and the questions
    white_line = Label(root, bg="white", fg="white", text="a",
                       font=("Arial", 1))
    white_line.grid(column=2, row=1, rowspan=5, sticky=NW, ipady=225, pady=30,
                    padx=5)

    # Learn button
    learn_button = Button(root, bg="red", fg="black", text="LEARN",
                          font=("Arial", 20),
                          command=lambda: [learn(num_track), easy_button.destroy(),
                                           hard_button.destroy(),
                                           instructions_label.destroy(),
                                           white_line.destroy(),
                                           learn_button.destroy()])
    learn_button.grid(column=0, row=4, columnspan=2, ipadx=10, ipady=10)

    # Easy and Hard Buttons - from 02_setup_questions_v4.py
    easy_button = Button(root, bg="red", fg="black", text="EASY",
                         font=("Arial", 20), command=lambda:
                         [easy_ask(num_track), easy_button.destroy(),
                          hard_button.destroy(), instructions_label.destroy(),
                          white_line.destroy(), learn_button.destroy()])
    easy_button.grid(column=0, row=5, sticky=N, ipadx=10, ipady=10, padx=30,
                     pady=30)

    hard_button = Button(root, bg="black", fg="black", text="HARD",
                         font=("Arial", 20), command=lambda:
                         [hard_ask(num_track), easy_button.destroy(),
                          hard_button.destroy(), instructions_label.destroy(),
                          white_line.destroy(), learn_button.destroy()])
    hard_button.grid(column=1, row=5, sticky=N, ipadx=10, ipady=10, padx=30,
                     pady=30)

    # Score Tracker - labels from 01_setup_interface_v4.py
    score_tracker = Label(root, bg="#FF7200", fg="white", text="Score Tracker",
                          font=("Arial", 20))
    score_tracker.grid(column=0, row=7, columnspan=2, sticky=N, pady=5)

    correct_label = Label(root, bg="#FF7200", fg="light green", text="Correct",
                          font=("Arial", 20))
    correct_label.grid(column=0, row=8, sticky=N)

    correct_num = Label(root, bg="#FF7200", fg="light green",
                        textvariable=num_correct, font=("Arial", 20))
    correct_num.grid(column=1, row=8, sticky=W)

    incorrect_label = Label(root, bg="white", fg="red", text="Incorrect",
                            font=("Arial", 20))
    incorrect_label.grid(column=2, row=8, sticky=N)

    incorrect_num = Label(root, bg="white", fg="red",
                          textvariable=num_incorrect, font=("Arial", 20))
    incorrect_num.grid(column=3, row=8, sticky=W)


# ******** Main Routine ********

# Necessary Lists and Variables
questions = []

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

num_questions = 0
eng_months_questions = []
incorrect_questions = []
correct_questions = []

num_correct = IntVar()

num_incorrect = IntVar()

quiz_loop(num_questions)

# Title Label
title_label = Label(root, bg="red", fg="black", text="Te Reo Maori Months "
                                                     "Quiz",
                    font=("Arial", 30, "bold"))
title_label.grid(column=1, columnspan=4, row=0, sticky=N, ipadx=10)

root.mainloop()
