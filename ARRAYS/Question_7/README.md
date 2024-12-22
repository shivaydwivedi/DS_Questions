# Rearrange an Array such that Even Numbers Come Before Odd Numbers

## Problem Statement:
Rearrange an array of integers such that all even numbers come before all odd numbers, without changing their relative order.

## Approaches:

### Naive Approach:
1. Create two separate lists: one for even numbers and one for odd numbers.
2. Traverse the input array and append the even numbers to the even list and odd numbers to the odd list.
3. Concatenate the even list followed by the odd list.

**Time Complexity**: O(n)  
**Space Complexity**: O(n)

### Best (Optimal) Approach:
1. Use two pointers: one starting at the beginning (`left`) and one starting at the end (`right`).
2. Move the `left` pointer forward while it points to even numbers, and move the `right` pointer backward while it points to odd numbers.
3. When the `left` pointer points to an odd number and the `right` pointer points to an even number, swap these two numbers.
4. Repeat until the `left` pointer crosses the `right` pointer.

**Time Complexity**: O(n)  
**Space Complexity**: O(1)

