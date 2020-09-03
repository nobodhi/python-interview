# quicksort

# in place
# https://www.youtube.com/watch?v=CB_NCoxzQnk
# recursive
# average complexity O(n log n), worst case O(n**2)
# uses space O(log n)
# good for large unsorted data sets
# quicksort "in place" sort is slightly more complicated

def quicksort_in_place(array, start, end):
    assert end < len(array)
    if start < end:
        print(start, end)
        print(array)
        pivot_line = partition(array, start, end)
        quicksort_in_place(array, start, pivot_line-1)
        quicksort_in_place(array, pivot_line+1, end)
    return array

def partition(array, start, end):
    pivot_line = end # could be anything
    pivot_value = array[pivot_line] 
    print("pivot", pivot_line, pivot_value)
    array[pivot_line], array[start] = array[start], array[pivot_line]
    print(array)
    pivot_line = start
    for runner in range(start, end+1):
        if array[runner] < pivot_value: # move the runner to the line and advance
            pivot_line += 1
            array[pivot_line], array[runner] = array[runner], array[pivot_line]
            print("-->", array[pivot_line])
    # now everything below the pivot_line is less than array[end]
    array[pivot_line], array[start] = array[start], array[pivot_line]
    return pivot_line

array = [32, 79, 128, 45, 26, 129, 92, 71, 68]
print(quicksort_in_place(array,0,len(array)-1))


# quicksort not in place: stable, requires O(n) space

def quicksort_stable(array):
    if not array:
        return [] # subarray is fully sorted
    pivot = array[len(array)-1] # could be anything

    head = quicksort_stable([item for item in array if item < pivot])
    tail = quicksort_stable([item for item in array if item > pivot])
    return head \
        + [pivot] \
        + tail

print("\nquicksort_stable", quicksort_stable(array))