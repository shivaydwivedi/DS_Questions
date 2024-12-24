### **Question 12: Rearrange an Array in Alternating Positive and Negative Numbers**

---

### **Problem Statement**

Given an array of integers, rearrange the array so that positive and negative numbers are placed alternately. If there are extra positive or negative numbers, append them at the end.

#### **Example**
- Input: `arr = [1, 2, 3, -4, -1, 4]`
- Output: `[-4, 1, -1, 2, 3, 4]`

---

### **Naive Approach**

#### **Explanation**
1. Separate the array into two subarrays: one for positive numbers and one for negative numbers.
2. Merge the two subarrays alternately to create the result array.
3. If one subarray runs out of elements, append the remaining elements of the other subarray.

#### **Steps**
- Traverse the array and add positive numbers to one list and negative numbers to another.
- Use a loop to pick elements alternately from both lists and append them to the result array.
- Append the remaining elements from the longer list if necessary.

#### **Time Complexity**
- \( O(n) \), where \( n \) is the size of the array.

#### **Space Complexity**
- \( O(n) \), for the extra space used for the result array.



### **Best Approach (In-Place Rearrangement)**

#### **Explanation**
1. Use a two-pointer approach to place positive and negative numbers alternately in the array.
2. Find the first misplaced element:
   - A positive number in a position meant for a negative number or vice versa.
3. Rotate the array to bring the next appropriate element to the current position.
4. Continue until the entire array is processed.

#### **Steps**
- Use two pointers to traverse the array.
- Identify misplaced elements and rotate the array to fix the sequence.
- Maintain the alternate pattern throughout.

#### **Time Complexity**
- \( O(n^2) \), for rotation operations.

#### **Space Complexity**
- \( O(1) \), as no extra space is used.


### **Example**

#### **Input**:
- `arr = [1, 2, 3, -4, -1, 4]`

#### **Output**:
- **Naive Approach**: `[-4, 1, -1, 2, 3, 4]`
- **Best Approach**: `[-4, 1, -1, 2, 3, 4]`

---

