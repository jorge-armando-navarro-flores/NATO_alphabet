import pandas


nato_alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet_data.iterrows()}

word_input = input("Enter a word: ")
phonetic_name = [nato_alphabet_dict[letter.upper()] for letter in word_input]
print(phonetic_name)
