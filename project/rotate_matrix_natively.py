# rotate a square 2D array in place using native python

# import this local file to generate a test array
import random_list as rl  # pylint: disable=import-error

# for testing
def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']\n'



def rotate_swap(given_array, n):
    """rotate using a single temp variable that swaps cells one at a time"""
    # print(to_string(given_array))
    for loop in range(n//2):
        # we need to track an additional loop because our square shrinks from both ends!
        width = n-loop-loop
        last = n-loop-1
        for index in range(width-1):
            temp = given_array[loop][loop+index]
            # top -> right
            given_array[loop+index][last], temp = temp, given_array[loop+index][last]
            # right -> bottom
            temp, given_array[last][last-index] = given_array[last][last-index], temp
            # bottom -> left
            temp, given_array[last-index][loop] = given_array[last-index][loop], temp
            # left -> top
            temp, given_array[loop][loop+index] = given_array[loop][loop+index], temp

    return given_array


def rotate_slice(given_array, n):
    """rotate using 4 slices."""
    # print(to_string(given_array))
    for loop in range(n//2):

        top = [x[loop:n-loop] for x in given_array[loop:loop+1]][0]
        bottom = [x[loop:n-loop] for x in given_array[n-loop-1:n-loop]][0]
        left = [x[loop] for x in reversed(given_array[loop:n-loop])]  # !
        right = [x[n-loop-1] for x in given_array[loop:n-loop]]
        width = n-loop-loop
        last = n-loop-1
        for index in range(width):
            # top->right
            given_array[loop+index][last] = top[index]
            # right->bottom
            given_array[last][last-index] = right[index]
            # bottom->left
            given_array[loop+index][loop] = bottom[index]
            # left->top
            given_array[loop][loop+index] = left[index]

    return given_array


print(to_string(rotate_swap(rl.sequential_array(10), 10)))
print(to_string(rotate_slice(rl.sequential_array(10), 10)))
