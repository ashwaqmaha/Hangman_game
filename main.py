from game_manager import check_answer_correctness
from mystery_word_generator import choose_random_missing_letter, choose_random_word
from word_database_manager import get_words


def hangman_start():
    word_file = input("Words file? [empty = short_words.txt, 1 = complex_words.txt]: ")

    if len(word_file)== 0:
        word_file = "word_collections/short_words.txt"
    else:
        word_file = "word_collections/complex_words.txt"
    
    words = get_words(word_file)

    random_word = choose_random_word(words)
    mystery_word, random_letter_index= choose_random_missing_letter(random_word)
    print(f"Guess the word: {mystery_word}\n")
    answer = input("Guess the missing letter: ")
    check_answer_correctness(answer,random_word,random_letter_index)

if __name__ == "__main__":
    hangman_start()
