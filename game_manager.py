strikes = ["""
/----
|   0
|
|   
|  
_______
""",
"""
/----
|   0
|   |
|
|
_______
""",
"""
/----
|   0
|  /|
|
|
_______
""",
"""
/----
|   0
|  /|\\
|   
|
_______
""",
"""
/----
|   0
|  /|\\
|   |
|  
_______
""",
"""
/----
|   0
|  /|\\
|   |
|  / 
_______
""",
"""
/----
|   0
|  /|\\
|   |
|  / \\
_______
"""]

def check_answer_correctness(answer, random_word, random_letter_index):
    if answer == random_word[random_letter_index]:
        print(f"The word was: {random_word}\n\nWell Done! You are awesome!")
    else:
        print(f"The word was: {random_word}\n\nWrong! Do better next time.")
