# checks user's guess compared to the secret
def get_feedback(guess : str, secret : str, word_list : list) -> list:
    """
    guess (str): guess of the 
    secret (str): secret word generated
    word_list (list): list of 5 letter words
    """
    feedback = []

    # Provides feedback for the guess compared to the secret
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            feedback.append('G')  # Green: correct letter and position
        elif guess[i] in secret:
            feedback.append('Y')  # Yellow: correct letter but wrong position
        else:
            feedback.append('X')  # Gray: letter not in the word
    for j in range(5):
        if feedback[j] == "Y":
            green_count = yellow_count = 0
            secret_count = secret.count(guess[j])
            for x in range(5):
                if secret[x] == guess[j] and feedback[x] == "G":
                    green_count += 1
                if secret[x] == guess[j] and feedback[x] == "Y":
                    yellow_count += 1
            if green_count + yellow_count > secret_count:
                feedback[j] = 'X'

                    
    return ''.join(feedback)

#answer = get_feedback("earls","angle",[]) #for testing
#print(answer)