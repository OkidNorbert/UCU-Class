def quick_sort(lst):
    if len(lst) < 0:
        return lst
    
    mid_point = len(lst)//2
    
    left = lst[:mid_point]
    right = lst[mid_point:]