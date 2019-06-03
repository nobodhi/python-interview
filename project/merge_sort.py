# merge sort
# h/t https://www.thecrazyprogrammer.com/2017/12/python-merge-sort.html

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

# overwrites array
def merge(left, right, result):
    i = 0 # left pointer
    j = 0 # right pointer
    k = 0 # result pointer

    while (i<len(left) and j<len(right)):
        if(left[i]<right[j]):
            result[k] = left[i]
            i+=1
        else:
            result[k] = right[j]
            j+=1
        k+=1
    while(i<len(left)):
        result[k] = left[i]
        i+=1
        k+=1
    while(j<len(right)):
        result[k] = right[j]
        j+=1
        k+=1

array = [99,21,3,19]
merge_sort(array)
print(array)