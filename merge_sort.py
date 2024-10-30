def merge_sort(array):
    if len(array) <= 1:
        return array
    
    
    mid_poimt = len(array) // 2
    
    left_array = array[:mid_poimt]
    right_array = array[mid_poimt:]

    merge_sort(left_array)
    merge_sort(right_array)

    merge(array,left_array,right_array)



def merge(array, left, right):
    i=j=k=0
    while i < len(left) and j < len(right):
        if  left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1
       
m = [4,7,89,4,2,54,2,2,4,5,6,8888]
b = merge_sort(m)
print(b)