# selection sort
# pylint: disable=import-error
from random_list import random_list as rl
# [x,x,x] [x,x,x,x,x,x,x,x,x,x]
# loop over the len of numbers
# result = [x]
# search ahead in numbers for the smallest (mark ith as smallest, loop til end)


def selection_sort(numbers: [int]) -> [int]:
    print(numbers)
    length = len(numbers)
    for index in range(length):
        smallest = index
        for runner in range(index+1, length):
            if numbers[smallest] > numbers[runner]:
                smallest = runner
        numbers[index], numbers[smallest] = numbers[smallest], numbers[index]
    return numbers


array = rl(10)
print(selection_sort(array))
