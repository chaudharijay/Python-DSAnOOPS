my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)
for i in range(n - 1):
    min_index = i
    # Find the minimum element in the unsorted part
    for j in range(i + 1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j
    # Swap the found minimum element with the first element of the unsorted part
    min_value = my_array.pop(min_index)
    my_array.insert(i, min_value)

print("Sorted array:", my_array)

# time complexity = o(n^2)