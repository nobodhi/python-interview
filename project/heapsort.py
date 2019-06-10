# pylint: disable=import-error
from random_list import random_list 


def build_max_heap(array):
    """reverse sort in place using a max heap"""
    for index in reversed(range(0,len(array))):
        print(index)
        max_heapify(array, index)

def max_heapify(array, index):
    left = index + 1
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

def build_min_heap(array):
    """forward sort in place using a min heap"""
    for index in reversed(range(0,len(array))):
        print(index)
        min_heapify(array, index)

def min_heapify(array, index):
    left = index + 1
    right = index + 2
    smallest = index
    if left < len(array):
        if array[index] > array[left]:
            smallest = left
    if right < len(array):
        if array[smallest] > array[right]:
            smallest = right
    if smallest != index:
        array[index], array[smallest] = array[smallest], array[index]
        min_heapify(array, smallest)


array = random_list(10)
# array = [99,2,3,3,12,4,5]
print(array)
build_max_heap(array)
print(array)

array = random_list(10)
# array = [99,2,3,3,12,4,5]
print(array)
build_min_heap(array)
print(array)

