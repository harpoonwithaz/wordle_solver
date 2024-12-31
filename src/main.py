import random, os
import feedback

# Reads words.txt in local directory and 
word_list = (open(f'{os.getcwd()}\\wordle_solvr\\wordle_solver\\data\\words.txt','r')).read().splitlines() #this is for jayden, comment this line and use the other one
#word_list = (open(f'{os.chdir("\\data\\words.txt")}','r')).read().splitlines()
#secret_word = random.choice(word_list)
secret_word = "angle"

attempts = 6

while attempts > 0:
    while True:
        # Asks user for guess
        user_guess = input("Enter your 5-letter guess: ").strip().lower()


        '''
        
        HERE WE WILL IMPLIMENT THE ALGORITHM.PY MODULE FOR MAKING THE GUESS USING FEEDBACK
        
        '''

        # Checks if it has 5 characters
        if len(user_guess) == 5 and user_guess.isalpha():
            break
            print("Invalid input. Please enter a 5-letter word.")

        # Checks if guess is a valid word
        if user_guess not in word_list:
            print('Invalid word')

    if user_guess == secret_word:
        print(f'Victory, the word was: {secret_word}')

    feedback = feedback.get_feedback(user_guess, secret_word, word_list)

    print(f"Feedback: {feedback}")
    attempts -= 1
    if attempts > 0:
        print(f"You have {attempts} attempts remaining.\n")
    else:
        print(f"Game over! The secret word was: {secret_word}")

    print(f'Secret word btw: {secret_word}')
