# Question 8: Rearrange an Array such that Even Numbers Come Before Odd Numbers


# Naive Approach
def rearrange_naive(arr):
    even_numbers = []
    odd_numbers = []
    for num in arr:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    return even_numbers + odd_numbers



# Best Approach
def rearrange_best(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] % 2 == 0:
            left += 1
        elif arr[right] % 2 != 0:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr

arr = [12, 34, 45, 9, 8, 90, 3]
print("Naive Approach: ", rearrange_naive(arr))
print("Best Approach: ", rearrange_best(arr))
