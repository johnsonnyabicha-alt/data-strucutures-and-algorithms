data = [-5,3,2,1,-3,-3,7,2,2]
from_index = 0
to_index = len(data) - 1
def selection_sort(data, from_index, to_index):
    # base case
    if from_index >= to_index:
        return data
    
    min_index = from_index
    for i in range(from_index +  1, to_index + 1):
        if data[i] < data[min_index]:
            min_index = i
    data[from_index], data[min_index] = data[min_index], data[from_index]
    
    selection_sort(data,from_index + 1, to_index)
print(selection_sort(data,from_index, to_index))
                
        