# second part of course https://www.udemy.com/11-essential-coding-interview-questions/


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

def rotate(given_array, n):
    # rotated = copy.deepcopy(given_array)
    # NOTE: To solve it in place, write this function so that you
    # won't have to create `rotated`.
    # NB we can create slices of the array for a "not quite in place" solution
    # and we can use a single "temp" variable to swap cells in place
    # TODO can't we swap in place using tuple swap instead?

    # outer loop here, this will count which "layer" of the onion we are in
    for loop in range(n//2):
        top = [x[loop:n-loop] for x in given_array[loop:loop+1]]
        left = [x[loop] for x in given_array[loop:n-loop]]
        bottom = [x[loop:n-loop] for x in given_array[n-loop-1:n-loop]]
        right = [x[n-loop-1] for x in given_array[loop:n-loop]]
        print(loop, "top", top)
        print(loop, "left", left)
        print(loop, "bottom", bottom)
        print(loop, "right", right)


    return given_array


# NOTE: The following input values will be used for testing your solution.
a1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]
# print(to_string(rotate(a1, 3))) # should return:
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]

a2 = [[1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
      [13, 14, 15, 16]]
# print(to_string(rotate(a2, 4))) # should return:
# [[13, 9, 5, 1],
#  [14, 10, 6, 2],
#  [15, 11, 7, 3],
#  [16, 12, 8, 4]]


def rotate_in_place(given_array, n):
    temp = []
    for loop in range(n//2-1):
        for index in range(n-loop):
            print("top->right")
            print("source", given_array[loop][index+loop])
            print("target1", given_array[index+loop][n-loop-1])
            # TODO last value goes into temp


    return given_array

print(to_string(rotate_in_place(a2, 4))) # should return:
