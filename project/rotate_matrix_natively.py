# second part of course https://www.udemy.com/11-essential-coding-interview-questions/

import random_list as rl # pylint: disable=import-error

# NOTE: Feel free to use the following function for testing.
# It converts a 2-dimensional array (a list of lists) into
# an easy-to-read string format.
# import copy


def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']\n'


# Implement your function below.
# n = # rows = # columns in the given 2d array

def rotate_in_place(given_array, n):
    temp = []
    print(to_string(given_array))
    for loop in range(n//2):
        # we need to track an additional loop because our square shrinks from both ends!
        for index in range(0,n-loop-loop-1):
            temp = given_array[loop][loop+index]
            # top -> right
            given_array[loop+index][n-loop-1], temp = temp, given_array[loop+index][n-loop-1]
            # right -> bottom
            temp, given_array[n-loop-1][n-loop-1-index] = given_array[n-loop-1][n-loop-1-index], temp
            # bottom -> left
            temp, given_array[n-loop-1-index][loop] = given_array[n-loop-1-index][loop], temp
            # left -> top
            temp, given_array[loop][loop+index] = given_array[loop][loop+index], temp
            # print(to_string([x[loop:n-loop] for x in given_array[loop:n-loop]]))

    return given_array

print(to_string(rotate_in_place(rl.sequential_array(10), 10))) 

# TODO deprecate n variable. why is this even here??

def rotate_by_vectors(given_array, n):
    """rotate using 4 temp vectors. this is nice if you want to rotate back and forth."""
    print(to_string(given_array))

    # outer loop here, this will count which "layer" of the onion we are in
    for loop in range(n//2):

        top = [x[loop:n-loop] for x in given_array[loop:loop+1]][0]
        bottom = [x[loop:n-loop] for x in given_array[n-loop-1:n-loop]][0]
        left = [x[loop] for x in reversed(given_array[loop:n-loop])] # !
        right = [x[n-loop-1] for x in given_array[loop:n-loop]]

        for index in range(len(left)): # left->top
            given_array[loop][index] = left[index]
        for index in range(len(top)): # top->right
            given_array[loop+index][n-loop-1] = top[index]
        for index in range(len(right)): # right->bottom
            given_array[n-loop-1][n-loop-index-1] = right[index]
        for index in range(len(top)): # bottom->left
            given_array[loop+index][loop] = bottom[index]

    return given_array

print(to_string(rotate_by_vectors(rl.sequential_array(10), 10))) 
