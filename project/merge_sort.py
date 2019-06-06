# merge sort
# h/t https://www.thecrazyprogrammer.com/2017/12/python-merge-sort.html
# h/t https://www.youtube.com/watch?v=Nso25TkBsYI

def merge_sort(array):
    n = len(array)
    if n > 1:
        mid = n//2
        left = array[0:mid]
        right = array[mid:n]
        print(mid, left, right,array)
        merge_sort(left)
        merge_sort(right)
        merge(left,right,array)

def merge(left, right, array):
    array_length = len(array)
    left_index = right_index = 0
    for array_index in range(0, array_length):
        if right_index == len(right):
            array[array_index:array_length] = left[left_index:len(left)]
            break
        elif left_index == len(left):
            array[array_index:array_length] = right[right_index:len(right)]
            break
        elif left[left_index] <= right[right_index]:
                array[array_index] = left[left_index]
                left_index+=1
        else:
            array[array_index] = right[right_index]
            right_index+=1

array = [99,2,3,3,12,4,5]
l = len(array)
merge_sort(array)
print(array)
assert len(array) == l