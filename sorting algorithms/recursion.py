# Generates a fibonacci sequence.
# Time comp = O(2^n), Space comp = O(n)
def f(n):
    # base case
    if n == 0:
        return 0 
    elif n == 1:
        return 1
    else:
        return f(n - 1) + f(n - 2 )
    
print(f(7))