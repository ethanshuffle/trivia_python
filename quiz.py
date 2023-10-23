#This file is where the actual quiz is given. The question is asked here,
#as well as the answer processed and points awarded.

import math
import random
import time
from game_select import menu_sequence
from api_call import get_request
from scoreboard import print_scoreboard, write_score

#Used in end of round stats as well as saving score
total_right = 0
total_wrong = 0
score = 0

#Takes json file and loops through each question, as well
#as prompting the user at the end of the round to save
#their score or play again
def quiz_loop(quiz):
    global total_right, total_wrong, score
    
    for i in quiz:
        question = i["question"]
        correct_answer = i["correctAnswer"]
        incorrect_answers = i["incorrectAnswers"]
        answer_choices = incorrect_answers.copy()
        answer_choices.append(correct_answer)
        random.shuffle(answer_choices)
        
        print("")
        print_question(question, answer_choices, correct_answer)
    
    #End of round stats
    print("")
    print("You have ", total_right, " correct and ", total_wrong, " wrong")
    print("Total score: ", score)
    print("")
    
    save = input("Would you like to save your score?(y/n): ")

    if (save == 'y'):
        write_score(score)
        print('')
        print_scoreboard()
    
    print("")
    choice = input("Play again?(y/n): ")
    print("")

    if (choice == 'y'):
        total_right = 0
        total_wrong = 0
        print(" ___   _    _____  ___   _   _      _    __   ")
        print("| |_) \ \_/  | |  | |_) | | \ \  / | |  / /\  ")
        print("|_|    |_|   |_|  |_| \ |_|  \_\/  |_| /_/--\ ")
        cat, dif = menu_sequence()
        quiz_loop(get_request(cat, dif))
    else:
        return 0 #close game

#Prints the question and answers choices
def print_question(question, answer_choices, correct_answer):
    print(question)
    
    time.sleep(4)

    num = 0
    for i in answer_choices:
        num += 1
        print(num, ". ", i)
    
    print("")

    answer_input(answer_choices, correct_answer)

#Processes the user's answer and determines if it is right or wrong
def answer_input(answer_choices, correct_answer):
    global total_right, total_wrong, score
    
    #Timer used for calculating score. Waits on user input to stop
    starttime = time.time()
    choice = "5"
    response_time = ""

    while choice.lower() != "1" and choice.lower() != "2" and choice.lower() != "3" and choice.lower() != "4":
        
        choice = input("Select a choice 1 through 4: ")
        response_time = round((time.time() - starttime), 2)
        
    match choice:
        case '1':
            answer = answer_choices[0]
        case '2':
            answer = answer_choices[1]
        case '3':
            answer = answer_choices[2]
        case '4':
            answer = answer_choices[3]
        case _:
            return 0 #misclick results in incorrect answer
    
    #Only awards points on right answers, obviously
    if (answer == correct_answer):
        total_right += 1
        #There is a 20 seconds window to answer before you get no points
        if (response_time > 20):
            score += 0
        else:
            score += calculate_score(response_time)
    else:
        total_wrong += 1 
    print("")
    print("Correct answer: ", correct_answer)

#Score is calculated using Kahoot's method, which can be found here:
#https://support.kahoot.com/hc/en-us/articles/115002303908-How-points-work#:~:text=This%20is%20how%20points%20are%20calculated%3A%201%20Divide,5%20Round%20to%20the%20nearest%20whole%20number.%20
def calculate_score(response_time):
    return math.ceil((1 - ((response_time / 20) / 2)) * 1000)
