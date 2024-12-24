### **Question 11: Find the Leaders in an Array**

### **Problem Statement**

An element in an array is called a "leader" if it is greater than or equal to all the elements to its right. The rightmost element is always considered a leader. 

#### **Example**
- Input: `arr = [16, 17, 4, 3, 5, 2]`
- Output: `[17, 5, 2]`

---

### **Naive Approach**

#### **Explanation**
1. For each element, iterate through all elements to its right.
2. If the current element is greater than or equal to all elements on its right, it is a leader.
3. Add the leader to the result list.

#### **Steps**
- Start with the first element.
- For each element, compare it with all elements to its right.
- If it is greater than or equal to all elements to its right, mark it as a leader.

#### **Time Complexity**
- \( O(n^2) \), where \( n \) is the size of the array.

#### **Space Complexity**
- \( O(k) \), where \( k \) is the number of leaders.


### **Best Approach (Traverse from Right)**

#### **Explanation**
1. Traverse the array from right to left.
2. Keep track of the maximum element found so far (`max_from_right`).
3. If the current element is greater than or equal to `max_from_right`, it is a leader.
4. Add the leader to the result list.

#### **Steps**
- Start from the rightmost element, as it is always a leader.
- Maintain a variable `max_from_right` to store the maximum value seen so far.
- Compare each element with `max_from_right`:
  - If it is greater than or equal, add it to the result and update `max_from_right`.

#### **Time Complexity**
- \( O(n) \), where \( n \) is the size of the array.

#### **Space Complexity**
- \( O(k) \), where \( k \) is the number of leaders.


### **Example**

#### **Input**:
- `arr = [16, 17, 4, 3, 5, 2]`

#### **Output**:
- **Naive Approach**: `[17, 5, 2]`
- **Best Approach**: `[17, 5, 2]`

---

### **README.md**

```markdown
# Find the Leaders in an Array

## Problem Statement
An element in an array is called a "leader" if it is greater than or equal to all the elements to its right. The rightmost element is always considered a leader.

---

## Approaches

### 1. Naive Approach
- **Explanation**:
  - For each element in the array, compare it with all elements to its right.
  - If the element is greater than or equal to all elements on its right, it is a leader.
- **Time Complexity**: \( O(n^2) \), where \( n \) is the size of the array.
- **Space Complexity**: \( O(k) \), where \( k \) is the number of leaders.
- **Code**:
  ```python
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
  ```

---

### 2. Best Approach (Traverse from Right)
- **Explanation**:
  - Start from the rightmost element, which is always a leader.
  - Maintain a variable `max_from_right` to keep track of the maximum element seen so far.
  - If the current element is greater than or equal to `max_from_right`, it is a leader.
  - Traverse the array from right to left, adding leaders to the result list.
- **Time Complexity**: \( O(n) \), where \( n \) is the size of the array.
- **Space Complexity**: \( O(k) \), where \( k \) is the number of leaders.
- **Code**:
  ```python
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
  ```

---

## Example

### Input
- `arr = [16, 17, 4, 3, 5, 2]`

### Output
- **Naive Approach**: `[17, 5, 2]`
- **Best Approach**: `[17, 5, 2]`
```

---

Let me know if you'd like to move to **Question 12: Rearrange an Array in Alternating Positive and Negative Numbers**, or if you have any doubts! 😊