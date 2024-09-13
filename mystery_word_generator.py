import random

def choose_random_word(words):
    random_word_index = random.randrange(len(words)-1)
    random_word = words[random_word_index].rstrip()
    return random_word

def choose_random_missing_letter(random_word):
    random_letter_index = random.randrange(len(random_word)-1)
    random_word.replace(random_word[random_letter_index],"_")
    mystery_word = random_word.replace(random_word[random_letter_index],"_")
    return mystery_word, random_letter_index

