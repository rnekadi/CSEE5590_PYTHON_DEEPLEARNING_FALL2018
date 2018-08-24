# Python Program for Letters and Digits Calc

S = input('Hello there please Enter your Sentence')

L = 0
D = 0
A = 0

for i in S:
    if i.isalpha():
        L = L+1
    elif i.isdigit():
        D = D+1
    else:
        A = A + 1


print("Letters:", L, ' ' + "Digits:", D, '' + "Rest:", A)




