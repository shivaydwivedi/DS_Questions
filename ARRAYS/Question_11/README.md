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

