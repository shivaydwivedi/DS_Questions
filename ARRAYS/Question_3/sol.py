# Question 3: Find the Missing Number in an Array


# Naive approach:


def find_missing_number_naive(arr, n):
    for num in range(1, n + 2):  # Numbers from 1 to n+1
        if num not in arr:
            return num

# Example Usage
arr = [1, 2, 4, 6, 3, 7, 8]
n = len(arr)  # Length of the array
print("Missing Number (Naive):", find_missing_number_naive(arr, n))


# Best Approach (Using Sum Formula)


def find_missing_number_best(arr, n):
    total_sum = (n + 1) * (n + 2) // 2  # Sum of first n+1 natural numbers
    array_sum = sum(arr)  # Sum of the elements in the array
    return total_sum - array_sum

# Example Usage
arr = [1, 2, 4, 6, 3, 7, 8]
n = len(arr)  # Length of the array
print("Missing Number (Best):", find_missing_number_best(arr, n))