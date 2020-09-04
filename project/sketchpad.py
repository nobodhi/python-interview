import time
start = time.time()

def square_sorted_list(l) -> list:
    print(l)
    '''takes a sorted int list and returns a sorted list of their squares'''
    # since the square of a negative is positive, the squares may not be in order!
    if len(l) == 0:
        return []
    result = []
    pointer_left = 0
    pointer_right = len(l)-1
    while pointer_right - pointer_left >= 0:
        # compare left and right items and insert the square of the larger
        if abs(l[pointer_left]) >= abs(l[pointer_right]):
            print("inserting {} at position 0".format(l[pointer_left]**2))
            result.insert(0, l[pointer_left]**2)
            pointer_left += 1
        else:
            print("inserting {} at position 0".format(l[pointer_right]**2))
            result.insert(0, l[pointer_right]**2)
            pointer_right -= 1
    return result


start = time.time()
print('square sorted list', square_sorted_list([-6, -4, 1, 2, 3, 7]))
# print('square sorted list', square_sorted_list([-6, -4, 1, 2, 3, 7, 9]))
# print('square sorted list', square_sorted_list([-6, -4]))
# print('square sorted list', square_sorted_list([-6]))
print(round(time.time() - start, 2), "seconds elapsed")
