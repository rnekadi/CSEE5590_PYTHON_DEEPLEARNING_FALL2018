# Search in a string and find the first non-repeated characters in that string


# Author Raju Nekadi


# Input String

my_string = 'Deep data structure'


# Removing spaces from input string and converting string to lower case as D not equal to d which will give output as p

new_my_string = my_string.replace(" ", "").lower()


length = len(new_my_string)

# defining a dictionary to hold for character from string

freq_dict = {}

# Buliding the dictionary from string with count

for i in range(0, length):
    c = new_my_string[i]
    val = freq_dict.get(c)
    if val is not None:
        freq_dict[c] = val + 1
    else:
        freq_dict[c] = 1

# looping through dictionary and printing first non repeating element.

for c in new_my_string:
    if freq_dict[c] == 1:
        print('The first non repeating character is: ', c)
        break









