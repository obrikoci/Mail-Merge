with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    with open("./Input/Names/invited_names.txt") as names_file:
        names = names_file.readlines()
        for name in names:
            new_name = name.strip()
            new_letter = letter.replace("[name]", new_name)
            with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", mode="w") as completed_letter:
                completed_letter.write(new_letter)
