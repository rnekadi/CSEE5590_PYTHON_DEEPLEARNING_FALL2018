# Program to create list and find most frequent item

import numpy as np

a = np.array([1,2,3,1,2,1,1,1,3,2,2,1])
b = np.array([12,12,3,12,12,1,12,1,3,2,2,11])
print(a)
countsa = np.bincount(a)
countsb = np.bincount(b)
print(countsa)
print(countsb)

print(np.argmax(countsa))
print(np.argmax(countsb))