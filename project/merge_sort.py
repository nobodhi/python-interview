# merge sort
# h/t https://www.thecrazyprogrammer.com/2017/12/python-merge-sort.html
# h/t https://www.youtube.com/watch?v=Nso25TkBsYI

def merge_sort(array):
    n = len(array)
    if n > 1:
    
        mid = n//2
        left = []
        right = []
        
        left = array[0:mid]
        right = array[mid:n]
    
        merge_sort(left)
        merge_sort(right)
    
        merge(left,right,array)

def merge(left, right, result):
    i = j = 0
    for k in range(0, len(result)):
        if j >= len(right):
            result[k:len(result)] = left[i:len(left)]
            break
        elif i >= len(left):
            result[k:len(result)] = right[j:len(left)]
            break
        elif left[i] < right[j]:
                result[k] = left[i]
                i+=1
        else:
            result[k] = right[j]
            j+=1

array = [99,21,3,19,21,5,67,98,3,12,22,31,45]
merge_sort(array)
print(array)