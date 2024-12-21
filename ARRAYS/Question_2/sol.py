# Question 2: Rotate an Array by K Positions.

# Naive approach:

def rotate_array_naive(arr, k):
    n = len(arr)
    k %= n  # Handle cases where k > n
    for _ in range(k):
        last_element = arr.pop()  # Remove the last element
        arr.insert(0, last_element)  # Insert it at the beginning
    return arr

# Example Usage
arr = [1, 2, 3, 4, 5]
k = 2
print("Rotated Array (Naive):", rotate_array_naive(arr, k))


# Best Approach (Using Slicing):

def rotate_array_best(arr, k):
    n = len(arr)
    k %= n  # Handle cases where k > n
    return arr[-k:] + arr[:-k]

# Example Usage
arr = [1, 2, 3, 4, 5]
k = 2
print("Rotated Array (Best):", rotate_array_best(arr, k))
