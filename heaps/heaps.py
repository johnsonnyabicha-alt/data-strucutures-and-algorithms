# Build a min heap(heapify) -  Time comp: O(n), Space comp: O(1)
# Given an a array(this could be a binary tree)
A = [-4,3,1,0,2,5,10,8,12,9]
import heapq
heapq.heapify(A)
print(A)
print('------------------------', 'Heap Push')
# Heap Push O(log n ) - Inserting an element 
heapq.heappush(A, 4)
print(A)
print('------------------------', 'Heap Pop')
# Heap Pop O(log n) -  Pop from the top of the stack
minn = heapq.heappop(A)
print(A, minn)
print('------------------------', 'Heap Sort')

# Heap Sort, Time comp : O(n log n), Space comp: O(1)
def heap_sort(arr):
    heapq.heapify(arr) # make sure its a heap 
    n = len(arr)
    sorted_list = [0] * n 
    for i in range(n): # each index
        minn  = heapq.heappop(A)
        sorted_list[i] = minn 
    return sorted_list
print(heap_sort([-4,3,1,0,2,5,10,8,12,9]))

print('------------------------', 'Heap Push-Pop')
# This pushes then pops. Insert a node, then remove the root
A = [-4,3,1,0,2,5,10,8,12,9]
heapq.heapify(A)
print(A, ' : HEAP ARRAY')
heapq.heappushpop(A, 99)
print(A)
# This removes -4, and adds 99
print('------------------------', 'Max heap')
# Max Heap 
B = [-4,3,1,0,2,5,10,8,12,9]
n = len(B)
for i in range(n):
    B[i]= -B[i] # changes negatives to positives and positive to negatives

heapq.heapify(B) # now when we call heapify, the largest negatives are at the bottom of the stack
print(B)        # and the negatives that turned positive are at the top of the stack 
                # so our negatives act as the highest elements, and our less negatives or positives act as our smallest
largest = -heapq.heappop(B) # pops the largest number
print(largest)
# if we wanted to push a node inside:
heapq.heappush(B, -7) # this is pushing in 7 and not -7
print(B)
# peak at min(), Time comp : O(1)
print(A[0], "** array A")


# BUILDING HEAP FROM SCRATCH: O(n logn)
# we are not using heapify, we are actually building it using the heapify logic 
C = [-5,4,2,1,7,0,3]
heap = []
for i in C :
    heapq.heappush(heap, i)
    print(heap, len(heap)) # creates heap and check size of heap
    
# Putting tuples of items on the heap 
D = [5,4,3,5,4,3,5,5,4]
from collections import  Counter 
counter = Counter(D)
print(counter)

heap = []
for k, v in counter.items():
    print(k,v)
    heapq.heappush(heap, (v, k))
    # smallest frequency shows at the top
    
print(heap)
# basically going back to heap, if we put a tuple inside a heap 
# it sorts the lowest frequency at the top. 
# if the two or more keys have the same frequency
# we put the lowest key number at the the from top to bottom 
