# Question-9:Maximum Product Subarray

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





