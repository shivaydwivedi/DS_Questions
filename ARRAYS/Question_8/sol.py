# Question-9: Merge the Two Sorted Arrays without Using Extra Space

# Naive Approach (Using Extra Space)
def merge_naive(arr1, arr2):
    # Create a new array to store the merged result
    merged = []
    
    i, j = 0, 0
    
    # Merge the arrays by comparing elements from both arrays
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
            
    # If any elements are left in arr1
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    
    # If any elements are left in arr2
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
    
    # Now we return the merged array, arr1 and arr2 are untouched
    return merged

# Example usage
arr1 = [1, 5, 9]
arr2 = [2, 3, 8, 10]

merged_array = merge_naive(arr1, arr2)
print("Merged Array:", merged_array)




# Best Approach (In-Place Merging using Gap Method)
def merge_in_place(arr1, arr2):
    n, m = len(arr1), len(arr2)
    gap = (n + m) // 2  # Initial gap

    while gap > 0:
        # Compare elements in the first array
        for i in range(n - gap):
            if arr1[i] > arr1[i + gap]:
                arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]
        
        # Compare elements between the two arrays
        for i in range(max(gap - n, 0), m):
            j = i + gap
            if j < m and arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
        
        # Compare elements in the second array
        for i in range(m - gap):
            if arr2[i] > arr2[i + gap]:
                arr2[i], arr2[i + gap] = arr2[i + gap], arr2[i]

        gap //= 2  # Reduce the gap

    return arr1, arr2

# Example
arr1 = [1, 5, 9]
arr2 = [2, 3, 8, 10]
print("Merged Arrays:", merge_in_place(arr1, arr2))

