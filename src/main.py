import random

# Imports local modules
import feedback, algorithm, filepaths

# Opens 5 letter words file and assigns the contents to a list
word_file = open(filepaths.five_letter_words, 'r')
word_list = word_file.read().splitlines()

# Selects a random word from list
#secret_word = random.choice(word_list)
secret_word = "deeds"
#['', '', '', '', 'weets', 'sinds', 'fifed', 'wraps', 'sages', 'spart', 'murre']
#word that can cause a problem. ["frass"]
#anyword that ends in: "*abel","*inds","**est","**ard","*ards","*iers","fa*ed","**ack","*o*ed","*o*es","*uffs","sa*er","*inos","*olds","*o*er"
potential_list = list(word_list) 
attempts = 6
run = True

best_guess = algorithm.create_guess(potential_list,False,"alone")
print(best_guess)

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
        if run:
            best_guess = algorithm.create_guess(potential_list,run,user_guess)
            potential_list.pop(potential_list.index(user_guess)) # Removes users guess
            potential_list = algorithm.prune_word_list(potential_list,word_feedback,user_guess)
        else:
            if user_guess in potential_list:
                potential_list.pop(potential_list.index(user_guess)) # Removes users guess
            potential_list = algorithm.prune_word_list(potential_list,word_feedback,user_guess)
            best_guess = algorithm.create_guess(potential_list,run,user_guess)

        if len(potential_list) < 10: print(potential_list)
        print("You should guess",best_guess)
        
        attempts -= 1
        if attempts > 0:
            print(f"You have {attempts} attempts remaining.\n")
        else:
            print(f"Game over! The secret word was: {secret_word}")
            break
        run = False
        print(f'Secret word btw: {secret_word}')
