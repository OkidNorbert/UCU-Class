def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_i = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_i]:
                min_i = j
                
        lst[i],lst[min_i] = lst[min_i],lst[i]
    return lst

a = [300,434,5,444,66]
print(selection_sort(a))