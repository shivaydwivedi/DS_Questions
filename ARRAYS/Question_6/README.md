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
---

### **Example**

#### **Input**:
`arr = [10, 5, 3, 4, 3, 5, 6]`

#### **Output**:
- **Naive Approach**: `5`
- **Best Approach**: `5`

---

