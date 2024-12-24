### **Question 14: Find the Longest Subarray with a Given Sum**

---

### **Problem Statement**

Given an array of integers and a target sum \( S \), find the length of the longest subarray whose sum equals \( S \).

#### **Example**
- Input:
  - Array: `[10, 5, 2, 7, 1, 9]`
  - Target Sum: `15`
- Output: `4`  
  (Subarray: `[5, 2, 7, 1]`)

---

### **Naive Approach**

#### **Explanation**
1. Use two nested loops:
   - Outer loop starts at each index of the array.
   - Inner loop calculates the sum of the subarray starting from the outer loop's index.
2. If the sum matches the target \( S \), calculate the length of the subarray.
3. Track the maximum length found.

#### **Steps**
- Traverse each index \( i \) of the array.
- For each \( i \), calculate sums for all subarrays starting from \( i \).
- Update the maximum length if a matching subarray is found.

#### **Time Complexity**
- \( O(n^2) \), where \( n \) is the size of the array.

#### **Space Complexity**
- \( O(1) \), no additional space is used.


### **Best Approach (Using Hash Map)**

#### **Explanation**
1. Use a hash map to store the first occurrence of cumulative sums.
2. Traverse the array while maintaining the cumulative sum.
3. Check:
   - If \( \text{current_sum} == \text{target_sum} \), the subarray starts from index 0.
   - If \( \text{current_sum} - \text{target_sum} \) exists in the hash map, calculate the subarray length.
4. Track the maximum length.

#### **Steps**
- Maintain a hash map where keys are cumulative sums and values are their first occurrences.
- For each element:
  - Update the cumulative sum.
  - Check if the sum equals the target or if the difference with the target exists in the map.
  - Update the maximum length accordingly.

#### **Time Complexity**
- \( O(n) \), single traversal of the array.

#### **Space Complexity**
- \( O(n) \), space used by the hash map.

### **Example**

#### **Input**:
- Array: `[10, 5, 2, 7, 1, 9]`
- Target Sum: `15`

#### **Output**:
- **Naive Approach**: `4`
- **Best Approach**: `4`

---
