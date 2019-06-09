# pylint: disable=import-error
from random_list import random_list 

def build_max_heap(array):
    for index in reversed(range(0,len(array))):
        print(index)
        max_heapify(array, index)

def max_heapify(array, index):
    left = index + 1
    right = index + 2
    print("index", index, array[index])
    biggest = index
    if left < len(array):
        print("left", left, array[left])
        if array[index] < array[left]:
            biggest = left
    else:
        print("left out of range", left, array)
    if right < len(array):
        print("right", right, array[right])
        if array[biggest] < array[right]:
            biggest = right
    else:
        print("right out of range", right, array)
    print("biggest", biggest, array[biggest])
    if biggest != index:
        array[index], array[biggest] = array[biggest], array[index]
        max_heapify(array, biggest)

# test_array = random_list(10)
test_array = [5, 10, 15, 20]
print(test_array)
build_max_heap(test_array)
print(test_array)
