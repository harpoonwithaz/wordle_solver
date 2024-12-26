import os, random
os.chdir ("Wordle")
global keyword, alphabet, alphabet_color, word_list, potenial_list
word_list_file = open("words.txt","r")
word_list = word_list_file.read().splitlines()
potenial_list = word_list
key_index = random.randrange(0,len(word_list)-1)
keyword = "piles"
# keyword = list[key_index]
alphabet = list("abcdefghijklmnopqrstuvwxyz")
alphabet_color = list("00000000000000000000000000")
print(keyword)

def check_real_word(userword):
    x = int(len(word_list)//2) #setting the index to the middle of the list of words
    factor = int(len(word_list)//3) #factor is how much to change the index by
    counter = 0
    while counter < 12: #technically, becuase of how powers of two work, this should be done in 12 runs or less. If it goes past that then the word should not exist.
        counter += 1 #adds one each round, so the while loop ends after 12 rounds
        if userword != word_list[x]:#if the words do not match
            if userword<word_list[x]: #if the userword is smaller than the current comparison word, then then comparison word gets smaller
                x = int(round(x-factor,1)) 
            else: #if the userword is bigger than the current comparison word, then then comparison word gets bigger
                x = int(round(x+factor,1))
        else:
            return True #if the word is in the dictionary, then return true
        factor = factor//2 #floor divide this by two to always half the range of words to search in.
        if factor < 1:#making sure factor doesnt go to 0
            factor = 1
    return False #returns false becuase too many loops ran

def ask_guess():
    guess = "default"
    valid = False
    while valid == False:
        guess = (input("What word do you want to guess: ")).strip().lower()
        if guess == "pixel7":
            valid == True
            break
        if len(guess) != 5:
            print("Not 5 letters!!")
            continue
        valid = check_real_word(guess)
        if valid != True:
            print("Not a valid word. ")
        
    return guess

def word_color_check(guessword):
    returnlist = [0,0,0,0,0]
    print(keyword)


    for greenindex in range(5):
        if keyword[greenindex] == guessword[greenindex]:
            returnlist[greenindex] = 1
            alphabetindex = alphabet.index(keyword[greenindex])
            alphabet_color[alphabetindex] = 1

    for x in range(5):
        for y in range(5):
            truecounter = 0
            colorcounter = 0
            if keyword[x] == guessword[y]:
                if returnlist[y] != 2 and returnlist[y] != 1:
                        for z in range(5):
                            if guessword[z] == keyword[x]:
                                truecounter =+ 1
                                if (returnlist[z] == 1) or (returnlist[z] == 2):
                                    colorcounter =+ 1
                        if colorcounter < truecounter:
                            returnlist[y] = 2
                            alphabetindex = alphabet.index(keyword[x])
                            if alphabet_color[alphabetindex] != 1:
                                alphabet_color[alphabetindex] = 2                    
                            break

    for x in range(5):
        if returnlist[x] == 0:
            returnlist[x] = 3
            alphabetindex = alphabet.index(guessword[x])
            if int(alphabet_color[alphabetindex]) == 0:
                alphabet_color[alphabetindex] = 3
            
            
    return returnlist


def colorprint(word, lister):
    
    # Color escape codes:
    # Gray:
    # \033[1;30m
    # Green:
    # \033[1;32m
    # Yellow:
    # \033[1;33m

    for y in range(len(lister)):
        if lister[y] == 1:
            x = "\033[1;32m"
        elif lister[y] == 2:
            x = "\033[1;33m"
        elif lister[y] == (3 or 4):
            x = "\033[1;30m"
        else:
            x = "\033[0;37m"
        print(x+word[y],end="")

def sortlist():
    for z in range(len(alphabet_color)): #removes words with grey letters in them
        if alphabet_color[z] == 3:#changes alphabet_color of that word to 4, so that it doesn't do this function the next time.
            alphabet_color[z] = 4#because we already removed all the words with grey letters, we don't need to recheck the same letter
            for x in range(len(potenial_list)-1, -1, -1):
                for y in range(5):
                    if potenial_list[x][y] == alphabet[z]:
                        potenial_list.pop(x)
                        break
    
for a in range(5):
    userinput = ask_guess()
    if userinput == "pixel7":
        break
    if userinput != keyword:
        color_list = word_color_check(userinput)
        colorprint(userinput,color_list)
        
        print("")
        colorprint(alphabet,alphabet_color)

        #print(potenial_list)

        print("\033[0;37m")



    else:
        print("You win!")
        break


'''
for x in range(len(lister)-1,-1,-1):
    for y in range(5):
        print(x,y)
        if lister[x][y] == "z":
            lister.pop(x)
            break
'''
    



print("\033[0;37m")