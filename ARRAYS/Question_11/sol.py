# Question 11: Find the Leaders in an Array

# Naive Approach

def find_leaders_naive(arr):
    n = len(arr)
    leaders = []
    for i in range(n):
        is_leader = True
        for j in range(i + 1, n):
            if arr[i] < arr[j]:
                is_leader = False
                break
        if is_leader:
            leaders.append(arr[i])
    return leaders

# Example Usage
arr = [16, 17, 4, 3, 5, 2]
result = find_leaders_naive(arr)
print(f"Leaders: {result}")


# Best Approach (Traverse from Right)

def find_leaders_best(arr):
    n = len(arr)
    leaders = []
    max_from_right = float('-inf')
    
    # Traverse from right to left
    for i in range(n - 1, -1, -1):
        if arr[i] >= max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]
    
    # Reverse the result to maintain order
    return leaders[::-1]

# Example Usage
arr = [16, 17, 4, 3, 5, 2]
result = find_leaders_best(arr)
print(f"Leaders: {result}")
