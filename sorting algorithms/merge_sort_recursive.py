arr = [-5,3,2,1,-3,-3,7,2,2]
def merge_sort(arr):
    n = len(arr)
    # base case:
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    L = merge_sort(left)
    R = merge_sort(right)
    l,r = 0,0
    L_len = len(L)
    R_len = len(R)
    sorted_arr = [0] * n # this creates an array of 0s of the length of the arr
    i = 0
    while l < L_len and r < R_len:
        if L[l] < R[r]:
            sorted_arr[i] = L[l]
            l += 1
        else:     
            sorted_arr[i] = R[r]
            r += 1
        i += 1
    while l < L_len:
        sorted_arr[i] = L[l]
        i += 1
        l += 1
    while r < R_len:
        sorted_arr[i] = R[r]
        i += 1
        r += 1
    return sorted_arr
print(merge_sort(arr))          
        
    