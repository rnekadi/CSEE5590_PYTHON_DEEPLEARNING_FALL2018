# A Python program to count number of words and characters in a file and the print the output


# Getting file name  from user
filename = input('Enter the Filename')
infile = open(filename, 'r') # Opening file in read mode as 'r'
wordcount = 0   # defining Word Count and Char Count variable
charcount = 0
line = infile.readline()   # Start reading the line using
while line != "":
    wordcount = len(line.split())  # Getting Word Count using len and split function
    wordslist = line.split()    # creating temporary list in order to avoid space to come in Char count
    charcount = sum(len(word) for word in wordslist)  # looping through word and from wordlist and counting char in same
    print("%s %d %d" % (line, wordcount, charcount))  # use of formatter for string and int type
    wordcount = 0
    charcount = 0
    line = infile.readline()  # going to next line till end
