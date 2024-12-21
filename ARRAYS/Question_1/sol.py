# Question 1: Find the Maximum Sum Subarray


# Naive approach:

def max_subarray_sum_naive(arr):
    n = len(arr)
    max_sum = float('-inf')  # Initialize with negative infinity
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            max_sum = max(max_sum, current_sum)
    return max_sum

# Example Usage
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print("Maximum Subarray Sum (Naive):", max_subarray_sum_naive(arr))



# Best Approach (Kadane’s Algorithm)

def max_subarray_sum_kadane(arr):
    max_sum = float('-inf')
    current_sum = 0

    for num in arr:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0

    return max_sum

# Example Usage
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print("Maximum Subarray Sum (Kadane):", max_subarray_sum_kadane(arr))

