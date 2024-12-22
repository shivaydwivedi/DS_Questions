# Question 4: Sort an Array of 0s, 1s, and 2s (Dutch National Flag Problem)

# Naive Approach (Counting Elements)

def sort_array_naive(arr):
    count_0, count_1, count_2 = 0, 0, 0

    # Count occurrences of 0, 1, and 2
    for num in arr:
        if num == 0:
            count_0 += 1
        elif num == 1:
            count_1 += 1
        elif num == 2:
            count_2 += 1

    # Overwrite array based on counts
    arr[:count_0] = [0] * count_0
    arr[count_0:count_0 + count_1] = [1] * count_1
    arr[count_0 + count_1:] = [2] * count_2

    return arr

# Example Usage
arr = [0, 2, 1, 2, 0, 1, 1, 0]
print("Sorted Array (Naive):", sort_array_naive(arr))


# Best Approach (Dutch National Flag Algorithm)

def sort_array_best(arr):
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

# Example Usage
arr = [0, 2, 1, 2, 0, 1, 1, 0]
print("Sorted Array (Best):", sort_array_best(arr))
