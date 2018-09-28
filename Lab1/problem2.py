# Subtraction two Files in Python.

# shutil module for its methods to copy files
import shutil

# Open the first file in read mode
file1 = open("file1.txt", "r")

# Get the 1st character of the file
file1FirstChar = file1.read(1)

# Getting data of the file
data1 = file1.read()

# If the 1st character is not available, then the file is empty
if not file1FirstChar:
    print("The file 1 is empty!")
else:
    # Open the second file in read mode
    file2 = open("file2.txt", "r")

    # Result file with deleted words
    with open('result.txt', 'w') as result:
        # Get the 1st character of the second file
        file2FirstChar = file2.read(1)

        # Getting data of the file 1
        data2 = file2.read()

        # If the 1st character is not available, then the file is empty
        if not file2FirstChar:
            print("The file 2 is empty! Thus output will be same as File 1!")
            shutil.copyfile('file1.txt', 'result.txt')
        else:
            print("Comparing File 1 & 2 in else block 1")
            # Creating a list of the words in file 2 for comparing it with File 1 words later
            listOfWord2 = []

            # Getting all the comma separated words from the File 2
            words2 = data2.split(" ")

            # Looping through all the words of File 2
            for word2 in words2:
                listOfWord2.append(word2)

            # Getting all the comma separated words from the File 1
            words1 = data1.split(" ")

            # Looping through all the words in File 1
            for word1 in words1:
                if not word1 in listOfWord2:
                    print("writing to file 1 - " + word1)

                    # Add the word in the result file only if the word does not match with the File 2 words
                    result.write(word1 + " ")
    # Closing all the opened files
    file2.close()
file1.close()
result.close()
