import os, random
#jayden was here
os.chdir ("Wordle")
global keyword, alphabet, alphabet_color, word_list
word_list_file = open("words.txt","r")
word_list = word_list_file.read().splitlines()
key_index = random.randrange(0,len(word_list)-1)
keyword = "piles"
# keyword = list[key_index]
alphabet = list("abcdefghijklmnopqrstuvwxyz")
alphabet_color = list("00000000000000000000000000")
print(keyword)

def check_real_word(userword):
    x = int(round(len(word_list)/2,1))
    factor = int(round(len(word_list)/2,1))
    counter = 0
    while counter < 13:
        counter += 1
        factor = factor/2
        if factor < 1:
            factor = 1
        for y in range(5):
            if userword[y] != word_list[x][y]:
                if ord(userword[y])<ord(word_list[x][y]):
                    x = int(round(x-factor,1))
                else:
                    x = int(round(x+factor,1))
                break
    if userword == word_list[x]:
        return True
    else:
        return False

def ask_guess():
    guess = "default"
    valid = False
    while valid == False:
        guess = (input("What word do you want to guess: ")).strip().lower()
        valid = check_real_word(guess)
        if len(guess) != 5:
            print("Not 5 letters!!")
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


    return returnlist


def colorprint(word, value):
    if value == 1:
        x = "\033[1;32m"
    elif value == 2:
        x = "\033[1;33m"
    elif value == 3:
        x = "\033[1;30m"
    else:
        x = "\033[0;37m"
    print(x+word,end="")


    
for a in range(5):
    userinput = ask_guess()
    if userinput != keyword:
        color_list = word_color_check(userinput)
        for c in range(5):
            colorprint(userinput[c],color_list[c])
        
        print("")
        for c in range(26):
            colorprint(alphabet[c],alphabet_color[c])
        
        print("\033[0;37m")  

    else:
        print("You win!")
        break


    



print("\033[0;37m")
