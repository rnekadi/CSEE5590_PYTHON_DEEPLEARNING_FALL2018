# Python code to reverse a string
# using loop

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str


firstName = input("Enter FirstName :")
lastName = input('Enter LastName :')

print("The original FirstName   is : ", end="")
print(firstName)
print("The Original LastName  is : ", end="")
print(lastName)

print("The reversed of FirstName is : ", end="")
print(reverse(firstName))

print("The reversed of LastName : ", end="")
print(reverse(lastName))

print("The reverse of FirstName and LastName", end=" ")
print(reverse(firstName) + ' ' + reverse(lastName))
