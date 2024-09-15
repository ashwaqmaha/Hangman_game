import threading
import time

strikes = { 6:
"""
/----
|   0
|
|   
|  
_______
""",
5:
"""
/----
|   0
|   |
|
|
_______
""",
4:
"""
/----
|   0
|  /|
|
|
_______
""",
3:
"""
/----
|   0
|  /|\\
|   
|
_______
""",
2:
"""
/----
|   0
|  /|\\
|  /
|  
_______
""",
1:
"""
/----
|   0
|  /|\\
|  / \\
|
_______
"""}

def count_down():

    for remaining in range(60,0,-1):
        print(f"Time left: {remaining} seconds", end="\r")
        time.sleep(1)

    # Clear the previous line by printing spaces
    print(" " * 30, end="\r")  
    print("Time up")

def correct_input(user_guess,used_letters,answer,mystery_word):
        # if the letter is in answer, tell the user they correct
    print(f"Correct guess: {user_guess} is in the mystery word!\n")
    used_letters.append(user_guess)

    # check if there is more then one of given letter in answer and save it
    count_of_letter_in_answer = answer.count(user_guess)

    # check if the count_of_letter_in_answer is greater then one
    if count_of_letter_in_answer > 1:

        # get a list of all the indexes 
        indexes_of_letter = [i for i,char in enumerate(answer) if char == user_guess]

        # replace the letter in all the positions it needs to be 
        for index in indexes_of_letter:
            mystery_word[index] = user_guess
    else:
        # find the location of the letter in the answer
        letter_index = answer.index(user_guess)

        # remove the _ in mystery word  and place the letter in the correct position in mystery word
        mystery_word[letter_index] = user_guess



def check_answer_correctness(mystery_word,answer):
    # number of attempts given to users (strikes allowed)
    attempts = 6

    # list of user guessed letter already revealed
    used_letters = []
    
    # check if the user is not out of attempts 
    while attempts > 0:
        # ask user for their guess and make it lowercase for case sensitivity sake when comparing 
        user_guess = input("Guess the missing letter: ").lower()

        if user_guess == "exit":
            print("Thank you for playing, bye!")
            break

        # check if there is only one letter given and guess is a alphabete
        if len(user_guess) > 1 or not user_guess.isalpha():
            print("Invalid input. Please guess a single letter.")
            continue

        # check if guess given is already used in the mystery word
        if user_guess in used_letters:
            print(f"The letter {user_guess} is already used in mystery word")
            continue
        
        # check if the letter given by user is in the answer
        if user_guess in answer:
            if user_guess in mystery_word:
                print(f"This letter {user_guess} is given.")
                continue

            correct_input(user_guess,used_letters,answer,mystery_word)

            # display mystery word with the revealed given letter
            display_mystery_word = " ".join(mystery_word)
            print(f"The mystery word: {display_mystery_word}")

            # if the whole word is revealed, congratulate user and end game
            if "_" not in mystery_word:
                print("Congratulations! You've guessed the word correctly!")
                break

        # incorrect answer
        else:
            # display the hangman 
            print(strikes[attempts])

            # decrease the number of attempts given by 1
            attempts -= 1

            # tell the user the amount of guesses left
            print(f"Wrong guess! Attempts left: {attempts}")

    # if there is no more attempts left, end game
    if attempts == 0:
        print("Game over! You've used all attempts.")
