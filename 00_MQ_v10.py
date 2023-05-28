# Final Version with comments

# Combined easy_ask and hard_ask function into one ask_function

# Import Statements
from tkinter import *
import random  # to randomly generate questions and random multiple choices
import subprocess  # for opening a text file
import os  # import operating system for opening a text file
import platform  # to know whether user's computer is Windows or Mac

# Root Window
root = Tk()
root.title("Te Reo Maori Months Quiz")  # Title of the window
root.geometry("700x700")  # Screen size 700px width, 700px height
root.configure(bg="#FF7200")  # Background of the colour orange


# Questions Class
class Questions:
    def __init__(self, eng_month, maori_month, numeric_month):
        self.eng_month = eng_month
        self.maori_month = maori_month
        self.numeric_month = numeric_month
        questions.append(self)  # add these details to the question list


# Learn Months Function if user wishes to see all the months first
def learn(num):
    learn_list = []  # List to contain all the month labels
    placement = 10  # first learn month label to place in row 10
    for month in questions:  # for each month in all the questions
        # create a label for each month, showing the month in English and Maori
        learn_month = Label(root, bg="white", fg="red",
                            text=f"{month.numeric_month}: {month.eng_month} = "
                                 f"{month.maori_month}",
                            font=("Arial", 16))
        learn_month.grid(column=1, row=placement, sticky=N, pady=3)
        placement += 1  # the next learn month label will be placed directly
        # in the next row
        learn_list.append(learn_month)  # add all the learn month labels to
        # the learn_list
    # Main Menu Button - when clicked:
    # the delete_learn function called to delete all learn months labels,
    # this main menu button is deleted, and the quiz_loop function is called
    # to return to the instructions page
    main_menu = Button(root, bg="black", fg="black", text="Main Menu",
                       font=("Arial", 20), command=lambda:
                       [delete_learn(learn_list), quiz_loop(num),
                        main_menu.destroy()])
    main_menu.grid(column=1, row=4, sticky=N, ipadx=10, ipady=10, padx=5)


# Delete all learn months labels
def delete_learn(list_learn):
    for learning_month in list_learn:  # for each learn month label in the
        # learn_list
        learning_month.destroy()  # delete the learn month label


# Add the Maori months to the months dropdown
def months_dropdown():
    maori_months_choices = []  # List to contain each Maori Month
    for month in questions:  # for each month in all the questions
        maori_months_choices.append(month.maori_month)  # add its Maori
        # translation into the maori months choices list
    random.shuffle(maori_months_choices)  # Randomly shuffle the order of
    # the Maori months in the list
    return maori_months_choices  # return the maori months list to the
    # get_answer_input function to create the dropdown for Maori months


# Random Question Generator
def random_question_generator():
    current_question = []  # List to contain all details associated with the
    # current question
    eng_month_choices = []  # List to contain each English Month
    for month in questions:  # for each month in all the questions
        eng_month_choices.append(month.eng_month)  # add its English
        # translation into the English months choices list
    random_month = random.choice(eng_months_questions)  # randomly generate
    # a new month for question from the english months question list in the
    # main routine, which constantly updates itself after a question is asked
    for month in questions:  # for each month in all the questions
        if month.eng_month == random_month:  # if the randomly
            # generated English month for question matches the English
            # translation of the month in the list
            current_question.append(month.eng_month)  # add the English
            # translation of the month to the current question list
            current_question.append(month.maori_month)  # add the Maori
            # translation of the month to the current question list
            current_question.append(month.numeric_month)  # add the number
            # of the month to the current question list
            eng_months_questions.remove(random_month)  # remove the randomly
            # generated question month from the questions list
            eng_month_choices.remove(random_month)  # remove the random
            # month from the english month choices list so the correct month
            # will only appear in one of the multiple choice buttons
    # Generate three other random options will only be used for the easy quiz
    random_option_1 = random.choice(eng_month_choices)  # generate a random
    # english month for an incorrect multiple choice button from the
    # english months choices list, which includes all the English months
    # except for the correct English month
    eng_month_choices.remove(random_option_1)  # remove the 1st randomly
    # generated incorrect month from the english month choices list so it
    # won't be repeated in another multiple choice option
    random_option_2 = random.choice(eng_month_choices)  # generate another
    # random english month for an incorrect multiple choice button
    # from the english months choices list
    eng_month_choices.remove(random_option_2)  # remove the 2nd randomly
    # generated incorrect month from the english month choices list
    random_option_3 = random.choice(eng_month_choices)  # generate another
    # random english month for an incorrect multiple choice button from the
    # english months choices list
    eng_month_choices.remove(random_option_3)  # remove the 3rd randomly
    # generated incorrect month from the english month choices list

    question_details = current_question, \
        random_option_1, random_option_2, random_option_3  # make the
    # variable question_details be the list of
    # current question details and the three random options
    return question_details  # return these question_details into the ask
    # function for question


# Ask function - to create a question
def ask(track_questions, level):
    # call the random_question_generator to generate a random month for
    # question (and three incorrect months for multiple choice in the easy
    # quiz)
    ask_details = random_question_generator()
    if level == "Easy":  # if this is an easy quiz
        # format the question to ask for the Maori month in English
        ask_question = f"What is the month\n '{ask_details[0][1]}' in English?"
    else:  # if this is a hard quiz
        # format the question to ask for the English month in Maori
        ask_question = f"What is the month\n '{ask_details[0][0]}' in Te Reo " \
                   f"Maori?"
    # Create the question label to display in the GUI with its question text
    # based on the above question format
    question_label = Label(root, bg="#FF7200", fg="black",
                           text=ask_question,
                           font=("Arial", 20))
    question_label.grid(column=3, row=1, columnspan=3, pady=20)
    # Call the get_answer_input function with the parameters of quiz_type,
    # details of current question, the three incorrect random choice,
    # the question tracker, and the question label
    get_answer(level, ask_details[0], ask_details[1], ask_details[2],
               ask_details[3], track_questions, question_label)


# Get answer input
def get_answer(difficulty, correct, random1, random2, random3,
               questions_track, question_label):
    if difficulty == "Easy":  # if this is an easy quiz
        correct_month = correct[0]  # the first item in the current question
        # details list is the correct English month answer
        place_correct_month = random.randint(1, 4)  # generate a random
        # position for the correct month
        # Create the multiple choice buttons below - when any one of
        # them are clicked, it will call the test_answer function with the
        # quiz_type, grade, user's selected answer, correct month,
        # the question tracker, the multiple choice buttons, and the
        # question label, and the main menu button is deleted
        correct_choice = Button(root, bg="black", fg="black",
                                text=correct_month,
                                font=("Arial", 17), command=lambda:
                                [test_answer(difficulty, "Correct",
                                            correct_month,
                                            correct_month,
                                            questions_track,
                                            [correct_choice,
                                             incorrect_choice_1,
                                             incorrect_choice_2,
                                             incorrect_choice_3],
                                             question_label),
                                 main_menu.destroy()])
        incorrect_choice_1 = Button(root, bg="red", fg="black", text=random1,
                                    font=("Arial", 17), command=lambda:
                                    [test_answer(difficulty, "Incorrect",
                                                random1,
                                                correct_month,
                                                questions_track,
                                                [correct_choice,
                                                 incorrect_choice_1,
                                                 incorrect_choice_2,
                                                 incorrect_choice_3],
                                                question_label),
                                     main_menu.destroy()])
        incorrect_choice_2 = Button(root, bg="red", fg="black", text=random2,
                                    font=("Arial", 17), command=lambda:
                                    [test_answer(difficulty, "Incorrect",
                                                random2,
                                                correct_month,
                                                questions_track,
                                                [correct_choice,
                                                 incorrect_choice_1,
                                                 incorrect_choice_2,
                                                 incorrect_choice_3],
                                                question_label),
                                     main_menu.destroy()])
        incorrect_choice_3 = Button(root, bg="red", fg="black", text=random3,
                                    font=("Arial", 17), command=lambda:
                                    [test_answer(difficulty, "Incorrect",
                                                random3,
                                                correct_month,
                                                questions_track,
                                                [correct_choice,
                                                 incorrect_choice_1,
                                                 incorrect_choice_2,
                                                 incorrect_choice_3],
                                                question_label),
                                     main_menu.destroy()])
        # if the correct_month position is generated with the integer 1
        if place_correct_month == 1:
            # place the correct month in the top-left multiple choice and
            # the rest of the incorrect options in the other multiple choice
            # buttons
            correct_choice.grid(column=3, row=2, ipadx=10, sticky=W, ipady=30)
            incorrect_choice_1.grid(column=4, row=2, ipadx=10, sticky=W,
                                    ipady=30)
            incorrect_choice_2.grid(column=3, row=3, ipadx=10, sticky=W,
                                    ipady=30, pady=5)
            incorrect_choice_3.grid(column=4, row=3, ipadx=10, sticky=W,
                                    ipady=30, pady=5)
        # if the correct_month position is generated with the integer 2
        elif place_correct_month == 2:
            # place the correct month in the top-right multiple choice and
            # the rest of the incorrect options in the other multiple choice
            # buttons
            correct_choice.grid(column=4, row=2, ipadx=10, sticky=W, ipady=30)
            incorrect_choice_1.grid(column=3, row=2, ipadx=10, sticky=W,
                                    ipady=30)
            incorrect_choice_2.grid(column=3, row=3, ipadx=10, sticky=W,
                                    ipady=30, pady=5)
            incorrect_choice_3.grid(column=4, row=3, ipadx=10, sticky=W,
                                    ipady=30, pady=5)
        # if the correct_month position is generated with the integer 3
        elif place_correct_month == 3:
            # place the correct month in the botton-left multiple choice and
            # the rest of the incorrect options in the other multiple choice
            # buttons
            correct_choice.grid(column=3, row=3, ipadx=10, sticky=W,
                                ipady=30, pady=5)
            incorrect_choice_1.grid(column=3, row=2, ipadx=10, sticky=W,
                                    ipady=30)
            incorrect_choice_2.grid(column=4, row=2, ipadx=10, sticky=W,
                                    ipady=30)
            incorrect_choice_3.grid(column=4, row=3, ipadx=10, sticky=W,
                                    ipady=30, pady=5)
        # if the correct_month position is generated with the integer 4
        elif place_correct_month == 4:
            # place the correct month in the botton-right multiple choice and
            # the rest of the incorrect options in the other multiple choice
            # buttons
            correct_choice.grid(column=4, row=3, ipadx=10, sticky=W,
                                ipady=30, pady=5)
            incorrect_choice_1.grid(column=3, row=2, ipadx=10, sticky=W,
                                    ipady=30)
            incorrect_choice_2.grid(column=4, row=2, ipadx=10, sticky=W,
                                    ipady=30)
            incorrect_choice_3.grid(column=3, row=3, ipadx=10, sticky=W,
                                    ipady=30, pady=5)
        # Create the main menu button for user to go back to the main page
        # if they want to revise again or restart a new quiz
        # When clicked: delete the question label, all the multiple choice
        # buttons, and the main menu button itself, and the quiz_loop function
        # is called to return to the instructions page
        main_menu = Button(root, bg="black", fg="black", text="Main Menu",
                           font=("Arial", 20), command=lambda: [
                            question_label.destroy(), correct_choice.destroy(),
                            incorrect_choice_1.destroy(), incorrect_choice_2.destroy(),
                            incorrect_choice_3.destroy(), quiz_loop(questions_track),
                            main_menu.destroy()])
        main_menu.grid(column=1, row=4, sticky=N, ipadx=10, ipady=10, padx=5)

    else:  # if this is a hard quiz
        correct_month = correct[1]  # the second item in the current question
        # details list is the correct Maori month answer
        clicked = StringVar()  # Setting the dropdown to a string variable
        clicked.set("Select Maori Month...")  # Initial set the dropdown,
        # asking the user to choose a Maori Month
        months_options = months_dropdown()  # list of the Maori months
        # Send dropdown menu to 'clicked' button
        # Lists out the options for Maori months
        select_dropdown = OptionMenu(root, clicked, *months_options)
        select_dropdown.config(bg="red")
        select_dropdown.grid(column=4, row=2, ipadx=10, sticky=W, ipady=10)
        # Call the submit answer function with the quiz_type, question status,
        # user's selected answer, correct month,
        # the question tracker, the dropdown itself, and the
        # question label
        submit_answer(difficulty, "CHECK", clicked, correct_month,
                      questions_track, select_dropdown, question_label)


# Submit answer function for the hard quiz
def submit_answer(level, status, answer_pressed, correct, track,
                  answer_type, label_question):
    # Create the submit answer button - when clicked, it calls a function to
    # check that the user has selected an option and hasn't left it blank
    submit_button = Button(root, bg="blue", fg="black", text="Submit",
                           font=("Arial", 20), command=lambda: [not_blank(
                                 level, status, answer_pressed, correct,
                                 track, answer_type, label_question),
                            submit_button.destroy(), main_menu.destroy()])
    submit_button.grid(column=4, row=5, sticky=NW, ipadx=5)
    # Create the main menu button for user to go back to the main page
    # if they want to revise again or restart a new quiz
    # When clicked: delete the question label, the dropdown menu,
    # the submit button, and the main
    # menu button itself. The quiz_loop function is called to return to the
    # instructions page
    main_menu = Button(root, bg="black", fg="black", text="Main Menu",
                       font=("Arial", 20), command=lambda: [
                            label_question.destroy(),
                            answer_type.destroy(),
                            quiz_loop(track),
                            main_menu.destroy(),
                            submit_button.destroy()])
    main_menu.grid(column=1, row=4, sticky=N, ipadx=10, ipady=10, padx=5)


# Not blank function for hard quiz to check that the user has selected an
# option from the dropdown menu
def not_blank(level, status, answer_pressed, correct,
              track, answer_type, label_question):
    # get the Maori month chosen from the dropdown menu
    user_answer = answer_pressed.get()
    if user_answer == "Select Maori Month...":  # if no Maori month has been
        # selected,
        # create an error message label, asking user to select a Maori month
        enter = Label(root, bg="black",
                      fg="red", text="Pls enter \na Maori month!",
                      font=("Arial", 20))
        enter.grid(column=5, row=5, sticky=W)
        enter.after(3000, enter.destroy)  # after 3 seconds, delete the
        # error message label
        # return to the submit answer function for user to select a Maori
        # month from the dropdown and re-submit
        submit_answer(level, status, answer_pressed, correct,
                      track, answer_type, label_question)
    else:  # if a Maori month has been selected
        # call the test_answer function with the quiz_type, question status,
        # user's selected answer, correct month,
        # the question tracker, the dropdown itself, and the
        # question label
        test_answer(level, status, answer_pressed, correct,
                    track, answer_type, label_question)


# Test Answer - to give quick feedback of correct/incorrect
def test_answer(quiz_difficulty, mark, user_answer, correct_answer, track,
                type_answer, question_quiz):
    # if the mark status of the answer is check, it means that the program
    # needs to check the Maori month from the dropdown
    if mark == "CHECK":
        user_answer = user_answer.get()  # get the Maori month chosen from
        # the dropdown menu
    if user_answer == correct_answer:  # if the Maori month chosen is the
        # correct answer
        mark = "Correct"  # the mark status is correct
    else:  # if the Maori month chosen not the correct answer
        mark = "Incorrect"  # the mark status is incorrect

    if mark == "Correct":  # if the mark status of the answer is correct
        # create a correct feedback label
        feedback = Label(root, bg="#FF7200", fg="light green", text="Correct!",
                         font=("Arial", 20))
        feedback.grid(column=3, row=5, sticky=W)
        # Increase the number of correct questions by 1 in the GUI interface
        num_correct.set(num_correct.get() + 1)

        for month in questions:  # for each month in all the questions
            # if the correct answer matches any of the English months or
            # Maori months,
            if correct_answer == month.eng_month or correct_answer == \
                    month.maori_month:
                # add the correct question details to the correct questions
                # list
                correct_questions.append([month.eng_month,
                                          month.maori_month,
                                          user_answer, track+1, quiz_difficulty])
    else:  # if the mark status of the answer
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

    track += 1
    feedback.after(3000, feedback.destroy)

    next_question(quiz_difficulty, track, type_answer, question_quiz)


def next_question(quiz, questions_track, answer_input, question):
    if quiz == "Easy":
        question.destroy()
        for choice in answer_input:
            choice.destroy()
    else:
        question.destroy()
        answer_input.destroy()

    if questions_track < 12:
        ask(questions_track, quiz)
    else:
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
                         [ask(num_track, "Easy"), easy_button.destroy(),
                          hard_button.destroy(), instructions_label.destroy(),
                          white_line.destroy(), learn_button.destroy()])
    easy_button.grid(column=0, row=5, sticky=N, ipadx=10, ipady=10, padx=30,
                     pady=30)

    hard_button = Button(root, bg="black", fg="black", text="HARD",
                         font=("Arial", 20), command=lambda:
                         [ask(num_track, "Hard"), easy_button.destroy(),
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

# Labels
# Comic Book Store Label
title_label = Label(root, bg="red", fg="black", text="Te Reo Maori Months "
                                                     "Quiz",
                    font=("Arial", 30, "bold"))
title_label.grid(column=1, columnspan=4, row=0, sticky=N, ipadx=10)

root.mainloop()
