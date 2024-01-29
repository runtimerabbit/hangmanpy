import time
import random
import pickle






hang = ["""
H A N G M A N - Fruit Edition

   +---+
   |   |
       |
       |
       |
       |
=========""", """
H A N G M A N - Fruits Edition

  +---+
  |   |
  O   |
      |
      |
      |
=========""", """
H A N G M A N - Fruits Edition

  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
H A N G M A N - Fruits Edition

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
H A N G M A N - Fruits Edition

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """
H A N G M A N - Fruits Edition

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """
H A N G M A N - Fruits Edition

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]

def welcome():
    global name
    name = input("""
                ========================================================================
                Welcome to Hangman, Fruit edition! Please enter you desired in-game name:   """).capitalize()
    print('Hi!' ,name,'Glad to see you here, Let me teach you the rules!\nYou will be playing against a computer.\nThe computer will generate a random fruit, and you have to guess it before the computer makes a full stickman!')

def getRandomWord():
    words = ['apple', 'banana', 'mango', 'strawberry', 'orange', 'grape', 'pineapple', 'apricot',
             'lemon', 'coconut', 'watermelon', 'cherry', 'papaya', 'berry', 'peach', 'lychee']

    word1 = random.choice(words)
    word2 = random.choice(words) + random.choice(words)
    word3 = random.choice(words) + random.choice(words) + random.choice(words)
    word4 = random.choice(words) + random.choice(words) + random.choice(words) + random.choice(words)
    word5 = random.choice(words) + random.choice(words) + random.choice(words) + random.choice(words) + random.choice(words)
    
    global choose_defficulty
    choose_defficulty = input("What difficulty do you want to play on? \n Easy - 1 fruit \n Medium - 2 fruits \n Hard - 3 fruits \n Rad - 4 fruits \n Fruitmania - 5 fruits  ").lower()
    
        

    if choose_defficulty.startswith('e'):
        choose_defficulty = 'Easy'
        return word1
    elif choose_defficulty.startswith('m'):
        choose_defficulty = 'Medium'
        return word2
    elif choose_defficulty.startswith('h'):
        choose_defficulty = 'Hard'
        return word3
    elif choose_defficulty.startswith('r'):
        choose_defficulty = 'Rad'
        return word4
    elif choose_defficulty.startswith('f'):
        'Fruitmania'
        return word5
    else:
        print('Please chosse between Easy, Hard or Medium')
        getRandomWord()


def displayBoard(hang, missedLetters, correctLetters, secretWord):
    print(hang[len(missedLetters)])
    print()

    print('Missed Letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print("\n") 

    blanks = "_" * len(secretWord)

    for i in range(len(secretWord)):  # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:  # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print("\n")
    



def getGuess(alreadyGuessed):
    while True:
        guess = input('Guess a letter: ')
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess


def playAgain():
    return input("\nDo you want to play again? ").lower().startswith('y')

welcome()

missedLetters = ''
correctLetters = ''
gameIsDone = False
secretWord = getRandomWord()


def leaderboard_func():
    leaderboard_input = input('Would you like to save your results to the leader board? y/n').lower()
    leaderboard_var2 = ''

    if leaderboard_input.startswith('y'):
        leaderboard_var = leaderboard_var2 + ' ' + name + ' ' + secretWord + ' ' + missedLetters
        time.sleep(1)
        text_file = open("leaderboard.txt", "a")
        n = text_file.write(leaderboard_var)
        f = open('leaderboard.txt', 'r')
        content = f.read()
        print(content)
        f.close()
        text_file.close()
        

while True:
    displayBoard(hang, missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('\nYes! The secret word is "' +
                  secretWord + '"! You have won!')
            leaderboard_func()
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(hang) - 1:
            displayBoard(hang, missedLetters,
                         correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' +
                  str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            leaderboard_func()
            gameIsDone = True



    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord()
        else:
            break
