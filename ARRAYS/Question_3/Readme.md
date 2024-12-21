### **Question 3: Find the Missing Number in an Array**

---

### **Problem Statement**

You are given an array containing \( n \) distinct integers ranging from \( 1 \) to \( n+1 \). The array is missing exactly one number from this range. Find the missing number.

#### **Example**
- Input: `arr = [1, 2, 4, 6, 3, 7, 8]`
- Output: `5`  
The range is \( 1 \) to \( 8 \), and \( 5 \) is missing.

---

### **Naive Approach**

#### **Explanation**
1. Iterate through numbers from \( 1 \) to \( n+1 \).
2. For each number, check if it is in the array.
3. The first number that is not found is the missing number.

#### **Time Complexity**
- Iterating through \( 1 \) to \( n+1 \): \( O(n) \).
- Checking if a number exists in the array: \( O(n) \).  
**Overall Complexity**: \( O(n^2) \).

#### **Code**
```python
def find_missing_number_naive(arr, n):
    for num in range(1, n + 2):  # Numbers from 1 to n+1
        if num not in arr:
            return num

# Example Usage
arr = [1, 2, 4, 6, 3, 7, 8]
n = len(arr)  # Length of the array
print("Missing Number (Naive):", find_missing_number_naive(arr, n))
```

---

### **Best Approach (Using Sum Formula)**

#### **Explanation**
1. The sum of the first \( n+1 \) natural numbers is given by the formula:
   \[
   S = \frac{(n+1) \times (n+2)}{2}
   \]
2. Calculate the actual sum of the array.
3. The missing number is the difference between the expected sum and the actual sum.

#### **Time Complexity**
- Summing the array: \( O(n) \).
- Using the formula: \( O(1) \).  
**Overall Complexity**: \( O(n) \).

#### **Code**
```python
def find_missing_number_best(arr, n):
    total_sum = (n + 1) * (n + 2) // 2  # Sum of first n+1 natural numbers
    array_sum = sum(arr)  # Sum of the elements in the array
    return total_sum - array_sum

# Example Usage
arr = [1, 2, 4, 6, 3, 7, 8]
n = len(arr)  # Length of the array
print("Missing Number (Best):", find_missing_number_best(arr, n))
```

---

### **Example**

#### **Input**:
`arr = [1, 2, 4, 6, 3, 7, 8]`

#### **Output**:
- **Naive Approach**: `5`
- **Best Approach**: `5`

---

### **README.md**

```markdown
# Find the Missing Number in an Array

## Problem Statement
Given an array containing \( n \) distinct integers ranging from \( 1 \) to \( n+1 \), find the one missing number.

---

## Approaches

### 1. Naive Approach
- **Explanation**:
  - Iterate through all numbers from \( 1 \) to \( n+1 \).
  - Check if each number exists in the array.
  - The first number that is not found is the missing number.
- **Time Complexity**: \( O(n^2) \).
- **Code**:
  ```python
  def find_missing_number_naive(arr, n):
      for num in range(1, n + 2):
          if num not in arr:
              return num
  ```

---

### 2. Best Approach (Using Sum Formula)
- **Explanation**:
  - Calculate the expected sum of numbers from \( 1 \) to \( n+1 \) using the formula:
    \[
    S = \frac{(n+1) \times (n+2)}{2}
    \]
  - Subtract the actual sum of the array from the expected sum to find the missing number.
- **Time Complexity**: \( O(n) \).
- **Code**:
  ```python
  def find_missing_number_best(arr, n):
      total_sum = (n + 1) * (n + 2) // 2
      array_sum = sum(arr)
      return total_sum - array_sum
  ```

---

## Example

### Input
`arr = [1, 2, 4, 6, 3, 7, 8]`

### Output
- **Naive Approach**: `5`
- **Best Approach**: `5`
```

---

Let me know if we can proceed to **Question 4: Sort an Array of 0s, 1s, and 2s (Dutch National Flag Problem)**! 😊