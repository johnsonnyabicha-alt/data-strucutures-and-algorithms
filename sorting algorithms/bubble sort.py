nums = [-5,3,2,1,-3,-3,7,2,2] 
n  = len(nums)
flag = True # assumes we are not done yet. 
while flag:
    flag = False# done, for now. 
    for i in range(1,n):
        if nums[i-1] > nums[i]:
            flag = True 
            nums[i], nums[i-1] = nums[i-1], nums[i]

print(nums)
# flag = False # done, for now. If swaps are done, we change back to True.
#     for i in range(1,n):
#         if nums[i-1] > nums[i]:
## This is a way to check if the whole array is sorted, because at the beginning 
## the array is true meaning we need complete the loop
## we first set it to false, the check the condition if it goes through the array
## and finds it suits the condition, it will set the loop to True so it can run 
## or if the condition is not met, meaning we have sorted the array
## we set the while loop to False, so it can no longer run.

#       BETTER NOTES:
# we start with True meaning let the loop keep going
# we set it now to false, so that once the list is sorted, end the loop
# by setting the while loop to false
# for each number in the list, if the previous number is greater than the 1st number
# swap and make sure to the loop to keep going
# if the condition is not met at one point, its okay leave it there and keep on going
#( That is basically having the if statement and then nothing after it)
#(notice is there is no else statement)
# since we've continued through the loop and we dont find an pair that satisfies 
# the condition, we set the loop to false 
# meaning the array is sorted
# we put the false at the beginning and not at the end, because we want the 
# loop to store the true signaling to keep on going and if it was at the end 
# it change the flag to false and end the loop