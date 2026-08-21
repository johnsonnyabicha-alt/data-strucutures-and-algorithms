def bucket_sort(nums):
    if len(nums) <= 1:
        return nums 
    r = max(nums) - min(nums) + 1
    bucket_count = min(len(nums), r)
    bucket_width = (r + bucket_count - 1)// bucket_count
    buckets = [[] for _ in range(bucket_count)]
    for i in range(len(nums)):
        bucket_index = (nums[i] - min(nums)) // bucket_width
        buckets[bucket_index].append(nums[i])
    res = []
    for bucket in buckets:
        insertion_sort(bucket)
        res.extend(bucket)
    return res

def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        for j in range(i,0,-1):
            if bucket[j-1] > bucket[j]:
                bucket[j-1],bucket[j] = bucket[j], bucket[j-1]
            else:
                break
print(bucket_sort([29, 25, 3, 49, 9, 37, 21, 43]))