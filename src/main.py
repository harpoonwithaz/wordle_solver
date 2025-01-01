import random, os
import feedback, algorithm

# Reads words.txt in local directory and 
word_list = (open(f'{os.getcwd()}\\wordle_solvr\\wordle_solver\\data\\words.txt','r')).read().splitlines() #this is for jayden, comment this line and use the other one
#word_list = (open(f'{os.chdir("\\data\\words.txt")}','r')).read().splitlines()
secret_word = random.choice(word_list)
#secret_word = "tides"
#word that can cause a problem. ["label","minds","quest"]
#anyword that ends in: "abel","inds","est"
potential_list = word_list
attempts = 6

while attempts > 0:
    while True:
        # Asks user for guess
        user_guess = input("Enter your 5-letter guess: ").strip().lower()

        if user_guess == 'exit':
            break

        # Checks if it has 5 characters
        if len(user_guess) != 5 and not user_guess.isalpha():
            continue

        # Checks if guess is a valid word
        if user_guess not in word_list:
            print('Invalid word')
            continue
        break
        

    if user_guess == 'exit':
        break
    else:
        if user_guess == secret_word:
            print("\033[1;32m")
            print(f'Victory! The word was: {secret_word}')
            print("\033[0;37m")
            break

        word_feedback = feedback.get_feedback(user_guess, secret_word, word_list)

        print(f"Feedback: {word_feedback}")     

        #algorithm imports
        potential_list.pop(potential_list.index(user_guess))
        potential_list = algorithm.prune_word_list(potential_list,word_feedback,user_guess)
        best_guess = algorithm.create_guess(potential_list)
        if len(potential_list) < 10: print(potential_list)
        print("You should guess",best_guess)
        
        attempts -= 1
        if attempts > 0:
            print(f"You have {attempts} attempts remaining.\n")
        else:
            print(f"Game over! The secret word was: {secret_word}")
            break

        print(f'Secret word btw: {secret_word}')
