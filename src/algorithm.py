#Jayden Phan - program to see the amount of letters in a list of words, and get the word with the most frequent letters in the list


def prune_word_list(word_list, feedback, user_guess): #function to remove words that cannot be the right word
    for word in word_list[::-1]: # [::-1] makes a reverse list of word_list so it can remove words from word_list without changing the index.
        pop_flag = True
        for letter_color_index in range(len(feedback)): #running a for loop in range of feedback, which is length 5
            if feedback[letter_color_index] == "G": #if letter is green
                if user_guess[letter_color_index] != word[letter_color_index]:
                    word_list.pop(word_list.index(word))#this part (word_list.index(word)) uses the index command to find the index of the word, .pop removes the word from the list
                    break
            elif feedback[letter_color_index] == "Y":
                if user_guess[letter_color_index] not in word:
                    word_list.pop(word_list.index(word))
                    break   
                if user_guess[letter_color_index] == word[letter_color_index]:
                    word_list.pop(word_list.index(word))
                    break
            elif feedback[letter_color_index] == "X": #if letter is grey
                if user_guess[letter_color_index] in word:#checking if the grey letter is in the word, if yes go to below
                    for letter in range(len(user_guess)): #for loop in range(5)
                        if user_guess[letter] == user_guess[letter_color_index]:#checks if the grey letter is in the word more than once
                            if feedback[letter] == ("G" or "Y"): #if it finds the letter again, checks if it is green or yellow. If it is then turns pop_flag off so it doesnt accidentally remove the word
                                pop_flag = False
                    if pop_flag == True:
                        word_list.pop(word_list.index(word))
                        break
    return word_list

#answer_list = prune_word_list(word_list,b,a) #testing for prune_word_list function
#print(answer_list)

def create_guess(word_list:list, first: bool, user_guess:str):
    alphabet_dict = {}
    for word in word_list:
        for letter in word:
            if letter in alphabet_dict:
                alphabet_dict[letter] += 1
            else:
                alphabet_dict[letter] = 1

    if first == True:
        for letter in user_guess:
            alphabet_dict[letter] = 0
    word_value = {}
    for word in word_list:
        unique_letters = set(word)
        score = sum(alphabet_dict[letter] for letter in unique_letters)
        word_value[word] = score
    answer = max(word_value, key=word_value.get)


    #print(word_value)
    #print((word_value.get(answer)))
    return(answer)
    #print(answer)

#creat_guess(word_list,True,"aeros")


