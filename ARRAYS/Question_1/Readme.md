**Question 1: Find the Maximum Sum Subarray (Kadane's Algorithm)**.



### **Problem Statement**

You are given an array of integers (both positive and negative). Your task is to find the contiguous subarray (containing at least one number) which has the maximum sum, and return that sum.

---

### **Naive Approach**

#### **Explanation**
The naive approach is to calculate the sum of all possible subarrays and find the maximum among them.

1. Use two nested loops:
   - The outer loop selects the starting point of the subarray.
   - The inner loop calculates the sum of subarrays starting from the selected index.
2. Compare each sum and keep track of the maximum.

#### **Time Complexity**
- Outer loop: \(O(n)\)
- Inner loop: \(O(n)\)
- Overall: \(O(n^2)\)



### **Best Approach (Kadane’s Algorithm)**

#### **Explanation**
Kadane's Algorithm is an efficient way to solve the problem in \(O(n)\) time.

1. Initialize two variables:
   - `current_sum`: Tracks the maximum sum of the subarray ending at the current position.
   - `max_sum`: Tracks the overall maximum sum encountered so far.
2. Iterate through the array:
   - Add the current element to `current_sum`. If `current_sum` becomes negative, reset it to 0.
   - Update `max_sum` to the larger of `max_sum` and `current_sum`.

#### **Time Complexity**
- Iterates through the array once: \(O(n)\).


### **Example**

#### **Input**:
`arr = [-2, -3, 4, -1, -2, 1, 5, -3]`

#### **Output**:
- **Naive Approach**: Maximum sum = 7 (subarray: `[4, -1, -2, 1, 5]`).
- **Kadane's Algorithm**: Maximum sum = 7 (subarray: `[4, -1, -2, 1, 5]`).

---
