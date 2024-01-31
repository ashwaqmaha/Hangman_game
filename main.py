import random

def get_words(file_name):
    with open(file_name,"r") as file:
        words = file.readlines()
        return words
    
   
def choose_random_word(words):
    random_word_index = random.randrange(len(words)-1)
    random_word = words[random_word_index].rstrip()
    return random_word


def choose_random_missing_letter(random_word):
    random_letter_index = random.randrange(len(random_word)-1)
    random_word.replace(random_word[random_letter_index],"_")
    mystery_word = random_word.replace(random_word[random_letter_index],"_")
    return mystery_word, random_letter_index


def check_answer_correctness(answer, random_word, random_letter_index):
    if answer == random_word[random_letter_index]:
        print(f"The word was: {random_word}\n\nWell Done! You are awesome!")
    else:
        print(f"The word was: {random_word}\n\nWrong! Do better next time.")

def hangman_start():
    word_file = input("Words file? [leave empty to use short_words.txt] : ")

    if len(word_file)== 0:
        word_file = "short_words.txt"
    else:
        word_file = "complex_words.txt"
    
    words = get_words(word_file)

    random_word = choose_random_word(words)
    mystery_word, random_letter_index= choose_random_missing_letter(random_word)
    print(f"Guess the word: {mystery_word}\n")
    answer = input("Guess the missing letter: ")
    check_answer_correctness(answer,random_word,random_letter_index)

if __name__ == "__main__":
    hangman_start()
