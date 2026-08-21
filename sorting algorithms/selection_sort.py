nums = [-5,3,2,1,-3,-3,7,2,2] 
n = len(nums)
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if nums[j] < nums[min_index]:
            min_index = j
    nums[i], nums[min_index] = nums[min_index], nums[i]
print(nums)   

# for i in range(n):# start at 1st element
#     min_index = i # assume the 1st element is the min index
#     for j in range(i + 1, n): # start at 2nd element
#         if nums[j] < nums[min_index]:# if the 2nd element is less than 1st element
#             min_index = j # store it as the min element, do this till end of list 
#     nums[min_index], nums[j] = nums[j], nums[min_index]
# # once you've got min element, swap the position of the first element 
# # with the position of the min element
# # move i and j and keep doing this 
