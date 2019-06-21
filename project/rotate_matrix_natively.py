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
        # TODO rotate top->right->bottom->left
        # a naive solution is simply perform 4 loops!


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
    temp = passes = 0
    print(to_string(given_array))
    for loop in range(n//2):
        # we need to track loop+passes because our square shrinks from both ends!
        passes += 1 
        for index in range(0,n-loop-passes):
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

# print(to_string(rotate_in_place(a2, 4))) # should return:

a3 = [[0, 1, 2, 3, 4, 5, 6, 7, 8],
[9, 10, 11, 12, 13, 14, 15, 16, 17],
[18, 19, 20, 21, 22, 23, 24, 25, 26],
[27, 28, 29, 30, 31, 32, 33, 34, 35],
[36, 37, 38, 39, 40, 41, 42, 43, 44],
[45, 46, 47, 48, 49, 50, 51, 52, 53],
[54, 55, 56, 57, 58, 59, 60, 61, 62],
[63, 64, 65, 66, 67, 68, 69, 70, 71],
[72, 73, 74, 75, 76, 77, 78, 79, 80]]

print(to_string(rotate_in_place(a3, 9)))