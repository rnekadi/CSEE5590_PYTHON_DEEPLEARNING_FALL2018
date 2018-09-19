# Consider the following scenario. You have a list of students who are attending class "Python"
# and another list of students who are attending class "Web Application".Find the list of students
# who are attending list of student who are attending Python class but not Web Application

# Authror Raju Nekadi

# Defining List for Python Class


Python = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Defining List for Web Application

WebApp = ['b', 'e', 'f', 'g']


# List to hold list of students who are attending list of student who are attending Python class but not Web Application


pythonNotWebApp = []

# Logic to fill new list

for p in Python:
    if p not in WebApp:
        pythonNotWebApp.append(p)

# Driver Program

if __name__ == "__main__":
    print('The student who are addenting Python not WebApplication:', pythonNotWebApp)

