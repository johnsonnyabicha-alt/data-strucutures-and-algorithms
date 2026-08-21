# if the array is all positive numbers. There is also another version when the array
# has negative numbers
data = [5,3,2,1,3,3,7,2,2]
n  = len(data)
maximum = max(data) 
print(maximum, "$$$")
counts = [0] * (maximum + 1)
for i in data:
    counts[i] += 1
print(counts, '\n 0:0, 1:1, 2:3,\n 3:3, 4:0, 5:1,\n 6:0, 7:1')

i = 0
for c in range(maximum + 1):
    while counts[c] > 0:
        data[i] = c
        i += 1
        counts[c] -= 1
print(data, 'sorted array ') 