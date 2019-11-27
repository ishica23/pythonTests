import random


def loadWordFromDoc():
    try:
        word = ""
        index = 0
        print ( randomNumber )
        with open ( 'palabras.txt' , "r" ) as f:
            for line in f:
                index=index + 1
                if randomNumber == index:
                    word=line
                    break
    except FileNotFoundError as error:
        print("error"+error)    
    return word


def guessTheLetter():
    global attempts
    while (True):
        palabra=loadWordFromDoc()
        letter=input("what is the letter: ")
        print (palabra)
        print (letter)
        for i in range(countAttempts):
            if letter == palabra.strip():
                print ("Congratulations guessed the word")
                break;
            else:
                attempts= attempts -i
                print ("try again you got "+ str(attempts))
                letter=input("what is the letter")

randomNumber=random.randrange(1,3)
countAttempts=3
attempts=3

if __name__ == '__main__':
    guessTheLetter()  
