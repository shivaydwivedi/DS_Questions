# Question 15: Maximum Product Subarray

# Naive Approach

def max_product_naive(arr):
    n = len(arr)
    max_product = float('-inf')
    
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= arr[j]
            max_product = max(max_product, product)
    
    return max_product

# Example Usage
arr = [2, 3, -2, 4]
result = max_product_naive(arr)
print(f"Maximum Product Subarray: {result}")


# Best Approach (Dynamic Programming)

def max_product_optimized(arr):
    n = len(arr)
    if n == 0:
        return 0
    
    max_product = min_product = global_max = arr[0]
    
    for i in range(1, n):
        if arr[i] < 0:
            max_product, min_product = min_product, max_product
        
        max_product = max(arr[i], arr[i] * max_product)
        min_product = min(arr[i], arr[i] * min_product)
        
        global_max = max(global_max, max_product)
    
    return global_max

# Example Usage
arr = [2, 3, -2, 4]
result = max_product_optimized(arr)
print(f"Maximum Product Subarray: {result}")

