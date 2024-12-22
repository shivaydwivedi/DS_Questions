# Question 5: Find the Minimum and Maximum Element in an Array

# Naive Approach (Linear Traversal)

def find_min_max_naive(arr):
    if not arr:
        return None, None  # Edge case for empty array

    min_element = max_element = arr[0]

    for num in arr:
        if num < min_element:
            min_element = num
        if num > max_element:
            max_element = num

    return min_element, max_element

# Example Usage
arr = [3, 5, 1, 2, 4, 8, -1]
min_val, max_val = find_min_max_naive(arr)
print(f"Minimum: {min_val}, Maximum: {max_val}")


# Best Approach (Tournament Method)

def find_min_max_tournament(arr, low, high):
    # Base case: only one element
    if low == high:
        return arr[low], arr[low]
    
    # Base case: two elements
    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
    
    # Divide the array
    mid = (low + high) // 2
    min1, max1 = find_min_max_tournament(arr, low, mid)
    min2, max2 = find_min_max_tournament(arr, mid + 1, high)

    # Merge the results
    return min(min1, min2), max(max1, max2)

# Example Usage
arr = [3, 5, 1, 2, 4, 8, -1]
min_val, max_val = find_min_max_tournament(arr, 0, len(arr) - 1)
print(f"Minimum: {min_val}, Maximum: {max_val}")

