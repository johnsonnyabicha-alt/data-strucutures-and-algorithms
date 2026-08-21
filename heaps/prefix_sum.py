def prefix_sum(array):
    i = 0
    while i < len(array):
        if i == 0:
            i+=1
            continue
        array[i] = array[i-1] + array[i]
        i+=1
    return array 
print(prefix_sum([3,7,2,5]))

def prefix_sum_other_way(array):
    for i in range(1, len(array)):
        array[i] = array[i-1] + array[i]
    return array
print("==other way==")
print(prefix_sum_other_way([3,7,2,5]))