import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_list = {row.letter:row.code for (index, row) in data.iterrows()}

def run():
    word = input("Input a word: ").upper()
    try:
        word_list = [nato_list[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        run()
    else:
        print(word_list)

run()