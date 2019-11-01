# https://www.udemy.com/11-essential-coding-interview-questions/

# NOTE: Feel free to use the following function for testing.
# It converts a 2-dimensional array (a list of lists) into
# an easy-to-read string format.
def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']\n'



# find the most common value of a list
# using a dictionary and list comprehension


def get_most_common(numbers: [int]):
    if len(numbers) == 0:
        return None
    result = {x: numbers.count(x) for x in numbers}
    return max(result, key=result.get)

# print(get_most_common([1,3,1,3,2,1]))
# print(get_most_common([]))


# find the common elements of two lists
A = [1, 3, 4, 6, 7, 9]
B = [1, 2, 4, 5, 9, 10]


def find_common_elements(list1: [int], list2: [int]):
    print(list1, list2)
    return [item for item in list1 if item in list2]

# print(find_common_elements(A, B))

# determine if two lists are rotations of each other
# assume there are no duplicates


def is_rotation(list1, list2):
    length = len(list1)
    if length != len(list2):
        print(list1, list2, "\nno match")
        return False
    temp = list1[:] + list1[:]
    print(list1, list2, temp)
    for index in range(length):
        if temp[index:index+length] == list2:
            print("match!")
            return True
    print("no match")
    return False

# list1 = [1, 2, 3, 4, 5, 6, 7]
# list2b = [4, 5, 6, 7, 1, 2, 3]
# is_rotation(list1, list2b) # True.
# list2a = [4, 5, 6, 7, 8, 1, 2, 3]
# is_rotation(list1, list2a) # False.
# list2c = [4, 5, 6, 9, 1, 2, 3]
# is_rotation(list1, list2c) # False.
# list2d = [4, 6, 5, 7, 1, 2, 3]
# is_rotation(list1, list2d) # False.
# list2e = [4, 5, 6, 7, 0, 2, 3]
# is_rotation(list1, list2e) # False.
# list2f = [1, 2, 3, 4, 5, 6, 7]
# is_rotation(list1, list2f) # True.
# list2g = [7, 1, 2, 3, 4, 5, 6]
# is_rotation(list1, list2g) # True.

# NB always check equal length
#
# alternate method:
# [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7] # represents any feasible rotation
# [.........4, 5, 6, 7, 1, 2, 3] True
# [..................7, 1, 2, 3, 4, 5, 6] True
# [.........4, 5, 6, 9, 1, 2, 3] False
# [   2, 3, 4, 5, 6, 7, 1] True
#
# accepted method:
# iterate thru first list, find the first match in the second
# compare second list's "trailing" sublist with first list's "opening" sublist
# compare second list's "opening" sublist with first list's "trailing" sublist
# if they both match, then get_rotation == True
# e.g.
# [4, 5, 6, 7], [1, 2, 3]

# Quick counting trick for dictionary with list comprehension and try/except
# using a lambda filter instead of list_comprehension:
# filtered = list(filter(lambda k: letter_count[k] == 1, letter_count))
def non_repeating(given_string):
    letter_count = {}
    for letter in given_string:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    filtered = [k for k in letter_count.keys() if letter_count[k] == 1]
    try:  # if len(filtered) == 0:
        print(filtered[0])
        return filtered[0]
    except:
        print(None)
        return None


# NOTE: The following input values will be used for testing your solution.
# non_repeating("abcab")  # should return 'c'
# non_repeating("abab")  # should return None
# non_repeating("aabbbc")  # should return 'c'
# non_repeating("aabbdbc")  # should return 'd'

def mine_sweeper(bombs: [[int]], rows, cols) -> [[int]]:
    map_grid = [[0 for i in range(cols)] for j in range(rows)]
    for [row, col] in bombs:
        map_grid[row][col] = -1
        for row_index in range( max(row-1, 0), min(row+2, rows)):
            for col_index in range( max(col-1, 0), min(col+2, cols)):
                if row_index == row and col_index == col:
                    pass
                else:
                    if map_grid[row_index][col_index] > -1:
                        map_grid[row_index][col_index] += 1
    return map_grid

print(to_string(mine_sweeper([[0,0],[0,1]],3,4)))

print(to_string(mine_sweeper([[0, 2], [2, 0]], 3, 3)))
# [[0, 1, -1],
#  [1, 2, 1],
#  [-1, 1, 0]]

print(to_string(mine_sweeper([[0, 0], [0, 1], [1, 2]], 3, 4)))
# [[-1, -1, 2, 1],
#  [2, 3, -1, 1],
#  [0, 1, 1, 1]]

print(to_string(mine_sweeper([[1, 1], [1, 2], [2, 2], [4, 3]], 5, 5)))
# [[1, 2, 2, 1, 0],
#  [1, -1, -1, 2, 0],
#  [1, 3, -1, 2, 0],
#  [0, 1, 2, 2, 1],
#  [0, 0, 1, -1, 1]]

# greedy recursive space filling algo "click" turns adjacent 0's into -2's
# first create a grid by calling mine_sweeper(?!)
# then pass that list to "click"
def click(field, num_rows, num_cols, given_i, given_j):
    """click event in mine_sweeper game"""
    this_value = field[given_i][given_j]
    if this_value == 0:
        field[given_i][given_j] = -2
        for i in range(max(given_i-1,0), min(given_i+2,num_rows)):
            for j in range(max(given_j-1,0), min(given_j+2,num_cols)):
                if not (i == given_i and j == given_j):
                    if field[i][j] == 0:
                        click(field, num_rows, num_cols, i, j)
    return field


# # NOTE: The following input values will be used for testing your solution.
field1 = [[0, 0, 0, 0, 0],
          [0, 1, 1, 1, 0],
          [0, 1, -1, 1, 0]]

print(to_string(click(field1, 3, 5, 2, 2))) # should return:
# # [[0, 0, 0, 0, 0],
# #  [0, 1, 1, 1, 0],
# #  [0, 1, -1, 1, 0]]

print(to_string(click(field1, 3, 5, 1, 4))) # should return:
# # [[-2, -2, -2, -2, -2],
# #  [-2, 1, 1, 1, -2],
# #  [-2, 1, -1, 1, -2]]


field2 = [[-1, 1, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 1, -1]]

print(to_string(click(field2, 4, 4, 0, 1))) #should return:
# # [[-1, 1, 0, 0],
# #  [1, 1, 0, 0],
# #  [0, 0, 1, 1],
# #  [0, 0, 1, -1]]

print(to_string(click(field2, 4, 4, 1, 3))) # should return:
# # [[-1, 1, -2, -2],
# #  [1, 1, -2, -2],
# #  [-2, -2, 1, 1],
# #  [-2, -2, 1, -1]]
