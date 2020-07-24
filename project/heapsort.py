# pylint: disable=import-error
from random_list import random_list 

#  this is actually just a selection sort! the trick is to create a max heap
#  and then pop off the root successively from 0 to n into a sorted array.
#  we can do this by passing the length of the remaining heap as a parameter
#  instead of looking at len(array) in max_heapify. that way we only re-heapify
#  the unsorted part of the array as we successifly swap the root and nth element.

def build_max_heap(array):
    """reverse sort in place using a max heap"""
    for index in reversed(range(0,len(array))):
        print(index)
        max_heapify(array, index)

def max_heapify(array, index):
    left = index + 1 # this is just array sorting - in a heap the left and right children are 2i+1 and 2i+2
    right = index + 2
    biggest = index
    if left < len(array):
        if array[index] < array[left]:
            biggest = left
    if right < len(array):
        if array[biggest] < array[right]:
            biggest = right
    if biggest != index:
        array[index], array[biggest] = array[biggest], array[index]
        max_heapify(array, biggest)

array = random_list(10)
print(array)
build_max_heap(array)
print(array)
array = random_list(10)
