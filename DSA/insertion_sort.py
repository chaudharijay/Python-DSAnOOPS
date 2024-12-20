# Array to be sorted
my_array = [64, 34, 25, 12, 22, 11, 90, 5]

# Loop through the array, starting from the second element
for i in range(1, len(my_array)):
    # Pick the current element
    key = my_array[i]

    # Move elements of my_array[0..i-1], that are
    # greater than key, to one position ahead
    j = i-1
    while j >= 0 and key < my_array[j]:
        my_array[j+1] = my_array[j]
        j -= 1
    my_array[j+1] = key

print("Sorted array is:")
print(my_array)

# time complexity = O[n^2]