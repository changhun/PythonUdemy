
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["none_exist_key"])
except FileNotFoundError:
    file = open("a_file.txt", 'w')
    file.write("something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    file_contents = file.read()
    print(file_contents)
finally:
    file.close()




