# udemy course 11-essential-coding-interview-questions

# find the most common value of a list
# using a dictionary and list comprehension


def get_most_common(numbers: [int]):
    if len(numbers) == 0:
        return None
    result = {x: numbers.count(x) for x in numbers}
    return max(result, key=result.get)

# print(get_most_common([1,3,1,3,2,1]))
# print(get_most_common([]))


# find the common elements of two lists - udemy
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
non_repeating("abcab")  # should return 'c'
non_repeating("abab")  # should return None
non_repeating("aabbbc")  # should return 'c'
non_repeating("aabbdbc")  # should return 'd'
