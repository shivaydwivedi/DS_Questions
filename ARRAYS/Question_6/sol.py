# Question 6: Find the First Repeating Element in an Array of Integers

# Naive Approach (Two Nested Loops)

def first_repeating_naive(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                return arr[i]
    return "No repeating element"

# Example Usage
arr = [10, 5, 3, 4, 3, 5, 6]
result = first_repeating_naive(arr)
print(f"First Repeating Element: {result}")


# Best Approach (Using Hashing)

def first_repeating_hashing(arr):
    seen = {}
    for num in arr:
        if num in seen:
            return num
        seen[num] = True
    return "No repeating element"

# Example Usage
arr = [10, 5, 3, 4, 3, 5, 6]
result = first_repeating_hashing(arr)
print(f"First Repeating Element: {result}")
