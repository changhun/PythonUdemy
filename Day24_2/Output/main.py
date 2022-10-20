with open("../Input/Letters/starting_letter.txt") as letter_file:
    mail_contents = letter_file.read()

with open("../Input/Names/invited_names.txt") as name_data:
    name_list = name_data.readlines()

for _name in name_list:
    name = _name.replace("\n", "")
    #name = _name.strip() # this code can replace the above line
    contents_with_name = mail_contents.replace("[name]", name)
    with open(f"./ReadyToSend/letter_for_{name}", "w") as letter_file_for_name:
        letter_file_for_name.write(contents_with_name)
