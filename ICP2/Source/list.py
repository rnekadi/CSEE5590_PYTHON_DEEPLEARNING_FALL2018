#  A Python program to take list of numbers as input and to return a tuple of first and last numbers in the list

# Defining the Empty List
out_list = []

# Appending Items into the list
for i in range(0, 4):
    number = int(input('Please enter the number : '))
    out_list.append(number)
print(out_list)

# Defining the first and last of list using len
first_list_index = 0
last_list_index = len(out_list) - 1

# Creating the tuple using the First and last Element from list
tup = (out_list[first_list_index], out_list[last_list_index])
print(tup)

