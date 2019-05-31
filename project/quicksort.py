# quicksort

# in place
# https://www.youtube.com/watch?v=CB_NCoxzQnk
# recursive
# average complexity O(n log n), worst case O(n**2)
# good for large unsorted data sets
# quicksort "in place" sort is slightly more complicated

def quicksort_in_place(array, start, end):
    assert end < len(array)
    print(array)
    if start < end:
        pivot_line = partition(array, start, end)
        quicksort_in_place(array, start, pivot_line-1)
        quicksort_in_place(array, pivot_line+1, end)
    return array

def partition(array, start, end):
    pivot_line = start-1 # list index is the LAST fucking thing
    pivot_value = array[end] # this is the pivot we'll use (could be random)
    print("the pivot line is now {} and the pivot value is {}".format(pivot_line, pivot_value))
    for runner in range(start, end):
        if array[runner] <= pivot_value: # move the runner to the line and advance
            pivot_line += 1
            array[pivot_line], array[runner] = array[runner], array[pivot_line]
            print("-->", array[pivot_line])
    # now everything below the pivot_line is less than array[end]
    array[pivot_line+1], array[end] = array[end], array[pivot_line+1]
    return pivot_line+1

array = [32, 79, 128, 45, 26, 129, 92, 71, 68]
print(quicksort_in_place(array,0,len(array)-1))

# array2 = [2,1,3,4,5,6,7,9,8]
# print(quicksort_in_place(array2,0,len(array2)-1))

# regular quicksort. this uses space O(log n)

