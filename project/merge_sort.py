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
    l_ptr = r_ptr = 0
    for arr_ptr in range(0, len(array)):
        if r_ptr == len(right):
            array[arr_ptr:len(array)] = left[l_ptr:len(left)]
            break
        elif l_ptr == len(left):
            array[arr_ptr:len(array)] = right[r_ptr:len(right)]
            break
        elif left[l_ptr] <= right[r_ptr]:
                array[arr_ptr] = left[l_ptr]
                l_ptr+=1
        else:
            array[arr_ptr] = right[r_ptr]
            r_ptr+=1

array = [99,2,3,3,12,4,5]
l = len(array)
merge_sort(array)
print(array)
assert len(array) == l