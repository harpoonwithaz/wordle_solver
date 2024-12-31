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
        if secret.count(guess[j]) == feedback.count("G"):
            for user_word_index in range(5):
                if feedback[user_word_index] == "Y": 
                    feedback[user_word_index] = "X"
                    
    return ''.join(feedback)

#answer = get_feedback("angla","aback",[]) #for testing
#print(answer)