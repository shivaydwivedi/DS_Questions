# Question 14: Find the Longest Subarray with a Given Sum

# Naive Approach

def longest_subarray_naive(arr, target_sum):
    max_length = 0
    n = len(arr)
    
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum == target_sum:
                max_length = max(max_length, j - i + 1)
    
    return max_length

# Example Usage
arr = [10, 5, 2, 7, 1, 9]
target_sum = 15
result = longest_subarray_naive(arr, target_sum)
print(f"Length of Longest Subarray: {result}")


# Best Approach (Using Hash Map)
def longest_subarray_optimized(arr, target_sum):
    prefix_sum_map = {}
    current_sum = 0
    max_length = 0
    
    for i in range(len(arr)):
        current_sum += arr[i]
        
        if current_sum == target_sum:
            max_length = i + 1
        
        if (current_sum - target_sum) in prefix_sum_map:
            max_length = max(max_length, i - prefix_sum_map[current_sum - target_sum])
        
        if current_sum not in prefix_sum_map:
            prefix_sum_map[current_sum] = i
    
    return max_length

# Example Usage
arr = [10, 5, 2, 7, 1, 9]
target_sum = 15
result = longest_subarray_optimized(arr, target_sum)
print(f"Length of Longest Subarray: {result}")
