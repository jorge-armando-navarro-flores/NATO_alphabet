import pandas


nato_alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet_data.iterrows()}

userInput = True
while userInput:
    word_input = input("Enter a word: ").upper()
    try:
        phonetic_name = [nato_alphabet_dict[letter] for letter in word_input]
        userInput = False
    except KeyError:
        print("Sorry, only letters in the alphabet please")
    else:
        print(phonetic_name)
