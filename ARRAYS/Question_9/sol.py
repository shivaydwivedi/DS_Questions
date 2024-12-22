# question-9: 

# Naive Approach (Brute Force)
def maxProduct(nums):
    n = len(nums)
    max_prod = float('-inf')  # Start with the smallest possible value
    
    # Iterate over all possible subarrays
    for i in range(n):
        current_product = 1
        for j in range(i, n):
            current_product *= nums[j]
            max_prod = max(max_prod, current_product)
    
    return max_prod

# Example usage
nums = [2, 3, -2, 4]
print("Maximum Product Subarray:", maxProduct(nums))




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

# Example usage
nums = [2, 3, -2, 4]
print("Maximum Product Subarray:", maxProduct(nums))
