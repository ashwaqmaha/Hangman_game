def get_words(file_name):
    with open(file_name,"r") as file:
        words = file.readlines()
        return words
    
   