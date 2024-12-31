#Jayden Phan - program to see the amount of letters in a list of words, and get the word with the most frequent letters in the list


def get_key_from_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None  # If the value is not found


def create_guess(word_list):
    alphabet_dict = {}
    for word in word_list:
        for letter in word:
            alphabet_dict[letter]["count"] += 1
    ''' the code below is not needed. but it takes the amount of occurrences of a letter then divides it by the total amount of letters. This will get the letter as a percentage of the total letters.
    for letter in alphabet_dict:
        alphabet_dict[letter]["weight"] = round(((alphabet_dict[letter]["count"]/totalcounter)*100),3)
    '''
    #word_value = {lister[x]:0 for x in range(len(lister))}
    word_value = {}

    for word in word_list:
        unique_letters = set(word)
        score = sum(alphabet_dict[letter]["count"] for letter in unique_letters)
        word_value[word] = score

    answer = max(word_value, key=word_value.get)
    print(answer)


'''     
for key, value in word_value.items():
    print(f"{key}: {value}") 

for key, value in alphabet_dict.items():
    print(f"{key}: {value}") 
''' 

