def word_replace():
    str = "This is a car. A red car. A beautiful car......"
    print(str)
    replace_word = input("Enter the word to replace: ")
    replacement_word = input("Enter the replacement word: ")
    print(str.replace(replace_word, replacement_word))


word_replace()
