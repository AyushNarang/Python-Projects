#TODO: Create a letter using starting_letter.txt

word = "[name]"
with open("Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()
    for new in names:
        new = new.strip("\n")
        with open("Input/Letters/starting_letter.txt") as letters:
            content = letters.readlines()
            for line in content:
                x = line.replace(word, new)
                with open(f"Output/ReadyToSend/letter_for_{new}.txt", "a") as new_letters:
                    new_letters.write(x)

