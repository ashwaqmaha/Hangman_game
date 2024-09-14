import random

def choose_random_word(words):
    random_word_index = random.randrange(len(words)-1)
    random_word = words[random_word_index].rstrip()
    return random_word

def choose_random_missing_letters(random_word):
    random_letter_index = random.randrange(len(random_word))
    mysteryword = [char if char == random_word[random_letter_index] else "_" for char in random_word]
    mystery_word = " ".join(mysteryword)
    return mystery_word, random_word

