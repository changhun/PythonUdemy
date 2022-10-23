import pandas


nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

name = input("What is your name? ")

my_nato = [nato_dict[alpha] for alpha in name.upper()]
print(my_nato)

