# Question-10:Rearrange an array such that even number comes before the odd numbers




# Naive Approach (Using Extra Space)
def rearrange(arr):
    even_numbers = []
    odd_numbers = []
    
    # Separate even and odd numbers into two lists
    for num in arr:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    
    # Concatenate even and odd numbers
    return even_numbers + odd_numbers

# Example usage
arr = [12, 34, 45, 9, 8, 90, 3]
result = rearrange(arr)
print("Rearranged Array:", result)


# Optimal Approach (In-place solution)
def rearrange_in_place(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        # If left is even, move left pointer to the right
        if arr[left] % 2 == 0:
            left += 1
        # If right is odd, move right pointer to the left
        elif arr[right] % 2 != 0:
            right -= 1
        # If left is odd and right is even, swap them
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    
    return arr

# Example usage
arr = [12, 34, 45, 9, 8, 90, 3]
result = rearrange_in_place(arr)
print("Rearranged Array:", result)
