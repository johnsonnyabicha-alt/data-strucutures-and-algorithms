data = [-5,-3,-2,1,3,5]

def binary_search(arr, target):
    L = 0
    R = len(data) - 1
    while L <= R:
        mid  = L + ((R - L) // 2 )
        if target == arr[mid]:
            return True 
        elif target < arr[mid]:
            R = mid  - 1
        else:
            L = mid + 1
            
    return False
            
print(binary_search(data, 5))
    