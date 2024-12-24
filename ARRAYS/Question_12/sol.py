# Question 12: Rearrange an Array in Alternating Positive and Negative Numbers

# Naive Approach

def rearrange_naive(arr):
    pos = [x for x in arr if x >= 0]
    neg = [x for x in arr if x < 0]
    result = []
    
    i, j = 0, 0
    while i < len(pos) and j < len(neg):
        result.append(neg[j])
        result.append(pos[i])
        i += 1
        j += 1
    
    # Append remaining elements
    while i < len(pos):
        result.append(pos[i])
        i += 1
    
    while j < len(neg):
        result.append(neg[j])
        j += 1
    
    return result

# Example Usage
arr = [1, 2, 3, -4, -1, 4]
result = rearrange_naive(arr)
print(f"Rearranged Array: {result}")



# Best Approach (In-Place Rearrangement)

def rearrange_in_place(arr):
    n = len(arr)
    wrong_index = -1
    
    for i in range(n):
        if wrong_index != -1:
            # Check if the element at wrong_index can be swapped
            if (arr[wrong_index] >= 0 and arr[i] < 0) or (arr[wrong_index] < 0 and arr[i] >= 0):
                arr[wrong_index:i + 1] = arr[i:i + 1] + arr[wrong_index:i]  # Rotate the array
                if i - wrong_index > 2:
                    wrong_index += 2
                else:
                    wrong_index = -1
        # Update wrong_index if the pattern breaks
        if wrong_index == -1:
            if (i % 2 == 0 and arr[i] >= 0) or (i % 2 == 1 and arr[i] < 0):
                wrong_index = i
    
    return arr

# Example Usage
arr = [1, 2, 3, -4, -1, 4]
result = rearrange_in_place(arr)
print(f"Rearranged Array: {result}")
