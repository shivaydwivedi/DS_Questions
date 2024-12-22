### **Question 6: Find the First Repeating Element in an Array of Integers**

---

### **Problem Statement**

Given an array of integers, find the first repeating element, i.e., the element that occurs more than once and whose first occurrence is the smallest. If no repeating element exists, return a message indicating that.

#### **Example**
- Input: `arr = [10, 5, 3, 4, 3, 5, 6]`
- Output: `5` (5 is the first repeating element as it appears first at index 1 and repeats at index 5).

---

### **Naive Approach (Two Nested Loops)**

#### **Explanation**
1. Use two nested loops to compare each element with the rest of the array.
2. For each element, check if it repeats later in the array.
3. Keep track of the index of the first repeating element.

#### **Steps**
- Iterate through the array, and for each element, iterate over the remaining array to find a match.
- If a match is found, record the index and break out of the inner loop.

#### **Time Complexity**
- \( O(n^2) \), due to the nested loops.

#### **Space Complexity**
- \( O(1) \), no extra space is used.

#### **Code**
```python
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
```

---

### **Best Approach (Using Hashing)**

#### **Explanation**
1. Use a dictionary to store the first occurrence of each element.
2. Traverse the array and check if the element is already in the dictionary:
   - If yes, it is the first repeating element.
   - If no, add it to the dictionary.
3. This approach ensures \( O(n) \) time complexity.

#### **Steps**
- Traverse the array while maintaining a dictionary of seen elements.
- Return the first element that is found in the dictionary during traversal.

#### **Time Complexity**
- \( O(n) \), as we traverse the array once.

#### **Space Complexity**
- \( O(n) \), for the dictionary.

#### **Code**
```python
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
```

---

### **Example**

#### **Input**:
`arr = [10, 5, 3, 4, 3, 5, 6]`

#### **Output**:
- **Naive Approach**: `5`
- **Best Approach**: `5`

---

### **README.md**

```markdown
# Find the First Repeating Element in an Array of Integers

## Problem Statement
Given an array of integers, find the first repeating element. The first repeating element is the one that occurs more than once and has the smallest first occurrence index.

---

## Approaches

### 1. Naive Approach (Two Nested Loops)
- **Explanation**:
  - Compare each element with all the elements that come after it using two nested loops.
  - Return the first element that repeats.
- **Time Complexity**: \( O(n^2) \)
- **Space Complexity**: \( O(1) \)
- **Code**:
  ```python
  def first_repeating_naive(arr):
      n = len(arr)
      for i in range(n):
          for j in range(i + 1, n):
              if arr[i] == arr[j]:
                  return arr[i]
      return "No repeating element"
  ```

---

### 2. Best Approach (Using Hashing)
- **Explanation**:
  - Use a dictionary to keep track of elements encountered during traversal.
  - If an element is already in the dictionary, it is the first repeating element.
- **Time Complexity**: \( O(n) \)
- **Space Complexity**: \( O(n) \), for the dictionary.
- **Code**:
  ```python
  def first_repeating_hashing(arr):
      seen = {}
      for num in arr:
          if num in seen:
              return num
          seen[num] = True
      return "No repeating element"
  ```

---

## Example

### Input
`arr = [10, 5, 3, 4, 3, 5, 6]`

### Output
- **Naive Approach**: `5`
- **Best Approach**: `5`
```

---

Let me know if we should move to **Question 7: Find the Intersection of Two Sorted Arrays**, or if you need clarification. 😊