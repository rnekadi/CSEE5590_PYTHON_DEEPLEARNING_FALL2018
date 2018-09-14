# Program to create list and find most frequent item


import numpy as np


d1 = np.random.random_integers(0, 20, 15)

print(d1)

vectorlist = []

# Converting array to list using tolist function
vectorlist = d1.tolist()

l = len(vectorlist)


def mostfreq(arr, n):
    # Sort the array
    arr.sort()

    # find the max frequency using
    # linear traversal
    max_count = 1;
    res = arr[0];
    curr_count = 1

    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            curr_count += 1

        else:
            if curr_count > max_count:
                max_count = curr_count
                res = arr[i - 1]

            curr_count = 1

    # If last element is most frequent
    if curr_count > max_count:
        max_count = curr_count
        res = arr[n - 1]

    return res


print(mostfreq(vectorlist, l))
