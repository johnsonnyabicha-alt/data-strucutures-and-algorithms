# TIME COMPLEXITY = best case((n log n)), worst case(O(n^2))- if you choose bad pivot
# SPACE COMPLEXITY = O(log N), but we coded this in O(n) because it is easier to write.
e= [-5,3,2,1,-3,-3,7,2,2]
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    p = arr[-1]
    L = [i for i in arr[:-1] if i <= p]
    R = [i for i in arr[:-1] if i > p]
    L = quick_sort(L)
    R = quick_sort(R)
    return L + [p] + R
print(quick_sort(e))
