from game.game_manager import check_answer_correctness
from game.mystery_word_generator import choose_random_missing_letters, choose_random_word
from game.word_database_manager import get_words

def hangman_start():
    word_file = input("Choose the word file difficulty:\n[Press Enter = short_words.txt, 1 = complex_words.txt]: ")

    if len(word_file)== 0:
        word_file = "word_collections/short_words.txt"
    else:
        word_file = "word_collections/complex_words.txt"
    
    words = get_words(word_file)

    random_word = choose_random_word(words)
    mystery_word, answer, mysteryword_list= choose_random_missing_letters(random_word)
    print("\nFill in the blanks by guessing letters. To quit the game, type 'exit'.")
    print(f"The mystery word: {mystery_word}\n")
    print(f"The answer is : {answer}")
    check_answer_correctness(mysteryword_list,answer)


if __name__ == "__main__":
    hangman_start()

