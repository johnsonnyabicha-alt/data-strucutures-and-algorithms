def selection_sort(data: list, from_index: int, to_index:int):
    to_index = len(data)
    for i in range(from_index, to_index):
        min_index = i
        for j in range(i + 1,  to_index):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    return data 
print(selection_sort([-5,3,2,1,-3,-3,7,2,2],0, 7) )

        