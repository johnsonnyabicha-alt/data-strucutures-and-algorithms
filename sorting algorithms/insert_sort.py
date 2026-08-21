nums = [-5,3,2,1,-3,-3,7,2,2] 
n  = len(nums)
for i in range(1,n): # loop each num
    for j in range(i,0,-1): # start from i and go backwards
        if nums[j] < nums[j-1]:# check if curr term is less prev term
            nums[j],nums[j-1] = nums[j-1],nums[j]# if true 
        else:
            break # if its not you break out of the sequence
print(nums)

# for i in range(1,n): # loop each num
#     for j in range(i,0,-1): # start from i and go backwards
#         if nums[j] < nums[j-1]:# check if curr term is less prev term
#             nums[j],nums[j-1] = nums[j-1],nums[j]# if true 
#         else:
#             break # if its not you break out of the sequence
                # think of the breaking out, as creating the sorted array
                # basically saying that the array is sorted
                #but the outer loop keeps going
# print(nums)