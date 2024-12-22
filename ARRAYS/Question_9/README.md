# Maximum Product Subarray

## Problem Statement:
Given an integer array `nums`, find the **maximum product subarray**. The subarray can be any contiguous subarray within the array, and you need to find the maximum product of all elements in any such subarray.

## Approaches:

### Naive Approach:
1. Iterate over all possible subarrays.
2. Calculate the product of each subarray and track the maximum product encountered.
3. This approach uses extra space and has a time complexity of **O(n^2)**.

### Optimal Approach:
1. Use dynamic programming to keep track of two values at each step:
   - `max_so_far`: The maximum product subarray ending at the current index.
   - `min_so_far`: The minimum product subarray ending at the current index.
2. Swap `max_so_far` and `min_so_far` if the current number is negative.
3. Update the result with the highest product encountered.

**Time Complexity**: O(n)  
**Space Complexity**: O(1)

## Code Implementation:
```python
# Optimal Approach (Dynamic Programming)
def maxProduct(nums):
    if not nums:
        return 0
    
    max_so_far = min_so_far = result = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_so_far, min_so_far = min_so_far, max_so_far  # Swap if the current number is negative
        
        max_so_far = max(nums[i], max_so_far * nums[i])  # Choose max between the current number and product with max_so_far
        min_so_far = min(nums[i], min_so_far * nums[i])  # Choose min between the current number and product with min_so_far
        
        result = max(result, max_so_far)  # Update the result with the highest product found
    
    return result
