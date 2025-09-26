#Wordle solver to find best guess

import random, os
import feedback, algorithm, filepaths

word_file = open(filepaths.five_letter_words, 'r')
word_list = word_file.read().splitlines()


#word_list = (open(f'{os.getcwd()}\\data\\words.txt','r')).read().splitlines() #this is for jayden, comment this line and use the other one
#word_list = (open(f'{os.chdir("\\data\\words.txt")}','r')).read().splitlines()
potential_list = list(word_list) 
guesses = 6


while guesses > 0:
    while True:
        # Asks user for guess
        user_guess = input("Enter your 5-letter guess: ").strip().lower()

        if user_guess == 'exit':
            break

        # Checks if it has 5 characters
        if len(user_guess) != 5 and not user_guess.isalpha():
            continue
        print(user_guess)
        # Checks if guess is a valid word
        if user_guess not in word_list:
            #print(word_list)
            print('Invalid word')
            continue
        break

    if user_guess =="exit":
        break
    while True:
        # Asks user for feedback
        user_feedback = input("What was the result of your guess: ").strip().upper()

        if user_feedback == 'exit':
            break

        # Checks if it has 5 characters
        if len(user_feedback) != 5 or not user_feedback.isalpha():
            print("5 letters pls")
            continue
        break 

    if user_feedback == "GGGGG":
        break
    if user_guess == 'exit':
        break
    else:   

        #algorithm imports
        potential_list.pop(potential_list.index(user_guess))
        potential_list = algorithm.prune_word_list(potential_list,list(user_feedback),user_guess)
        best_guess = algorithm.create_guess(potential_list,False,"place")
        if len(potential_list) < 10: print(potential_list)
        print("You should guess",best_guess)
        
        
    guesses -= 1
if guesses <= 0:
    print("You lose!")
else:
    print("You win!")

