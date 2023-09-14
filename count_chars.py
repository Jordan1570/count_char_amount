# Display a list of words with their count

# Ask the user for a string to
# use to collect the letter counts
my_string = input("Enter a string = ")
# Convert to lower-case
my_string = my_string.lower()

# Create empty dictionary. The idea is that
# this dictionary has a letter in teh string as a key
# and the count of the letters as a Value
# # You will build the dictionary in the loop below
my_dict = {}

# Iterate over characters in string
# Inside loop if dictionary does not have an entry as that
# character as key, create an entry and assign a value of 1
# else add 1 to the (existing) dictionary entry
for a_char in my_string:
    # if the character isnt in the dictionary add make it 
    if a_char not in my_dict:
        my_dict[a_char] = 1
    else:
        # Add 1 to the amount of chars
        my_dict[a_char] += 1

for letter, letter_amount in my_dict.items():
    print(f'{letter} amount = {letter_amount}')

'''
j amount = 1
o amount = 2
r amount = 1
d amount = 1
a amount = 1
n amount = 1
  amount = 1
s amount = 1
c amount = 1
t amount = 2 ## Jordan Scott
'''