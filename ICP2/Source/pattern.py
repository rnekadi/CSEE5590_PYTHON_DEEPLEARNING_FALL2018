#

# Function to display Letter A using asterisk
def displaya():
    n = int(input("Enter Number of lines you want to print First Letter "))
    for row in range(n):
        for col in range((n // 2) + 1):
            if ((col == 0 or col == n // 2) and row != 0 or
                    row == 0 and col != 0 and col != n // 2 or
                    row == n // 2):
                print("*",end=" ")
            else:
                print(" ",end=" ")

        print()



# Function to display Letter P using asterisk

def displayp():
    n = int(input("Enter Number of lines you want to print First Letter "))
    for row in range(n):
        for col in range((n//2) + 1):
            if (col == 0) or ((col == n//2) and (row != 0 and row < n//2)) or ((row == 0 or row == n//2) and
                                                                                        col != 0 and col != n//2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


# Function to display Letter L using asterisk

def displayl():
    n = int(input("Enter Number of lines you want to print First Letter "))
    for row in range(n):
        for col in range((n//2) + 1):
            if (col == 0) or (row == n-1 and col > 0):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


# Function to display Letter R using asterisk

def displayr():
    n = int(input("Enter Number of lines you want to print First Letter "))
    for row in range(n):
        for col in range((n//2) + 1):
            if (col == 0) or ((col == n//2) and (row != 0 and row < n//2)) or ((row == 0 or row == n//2) and
                 col != 0 and col != n//2) or (row > n//2 and col == n//2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def displays():
    n = int(input("Enter Number of lines you want to print First Letter "))
    for row in range(n):
        for col in range((n//2) + 1):
            if (row == 0 or row == n-1 or row == n//2) or (col ==0 and row >0 and row < n//2) or (col == n//2 and row > n//2 and row < n-1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()



# Logic to get input String from User and print Letters using Stars

Name = input("Enter your Name:")

Letter = Name[0]


if Letter == 'R':
    displayr()
elif Letter == 'A':
    displaya()
elif Letter == 'L':
    displayl()
elif Letter == 'P':
    displayp()
elif Letter == 'S':
    displays()
else:
    print("Letter Not Found")







