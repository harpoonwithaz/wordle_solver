import random

# Imports local modules
import feedback, algorithm, filepaths

# Opens 5 letter words file and assigns the contents to a list
word_file = open(filepaths.five_letter_words, 'r')
word_list = word_file.read().splitlines()

# Selects a random word from list

#secret_word = "quest"

#word that can cause a problem. ["label","minds","quest"]
#anyword that ends in: "*abel","*inds","**est","**ard","*ards","*iers","fa*ed"
lose = []
test_list_num = []
test_list = []

for x in range(100):
    potential_list = list(word_list) 
    attempts = 6
    run = True

    secret_word = random.choice(word_list)
    user_guess = algorithm.create_guess(potential_list,False,"alone")

    while attempts > 0:

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
            user_guess = best_guess
            if len(potential_list) < 10: print(potential_list)
            print("You should guess",best_guess)
            
            attempts -= 1
            if attempts > 0:
                print(f"You have {attempts} attempts remaining.\n")
            else:
                print(f"Game over! The secret word was: {secret_word}")
                lose.append(secret_word)
                break
            run = False
            print(f'Secret word btw: {secret_word}')
    test_list.append(secret_word)
    test_list_num.append(attempts)

for x in range(len(test_list)):
    print(test_list[x],"|",test_list_num[x])
print(lose)

