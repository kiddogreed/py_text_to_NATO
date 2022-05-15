import pandas
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:{"A": "Alfa", "B": "Bravo"}
nato = pandas.read_csv('nato_phonetic_alphabet.csv')
letters = [letter for letter in nato.letter]
code = [c for c in nato.code]
super_nato = {key: code for (key, code) in zip(letters, code)}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = str(input("Enter word:")).upper()
final_nato = [super_nato[letter] for letter in user_input if letter in super_nato]
#
# for letter in user_input:
#     if letter in super_nato:
#         #print(super_nato[letter])
#         final_nato.append(super_nato[letter])

print(f"Hello, {final_nato}!")

# print(letters)
# print(code)
# code_dict = {index: row for (index, row) in nato.iterrows()}
# code_new = {key: val for (key,val) in code_dict.items() }
