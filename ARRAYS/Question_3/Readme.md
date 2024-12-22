### **Question 3: Find the Missing Number in an Array**

---

### **Problem Statement**

You are given an array containing \( n \) distinct integers ranging from \( 1 \) to \( n+1 \). The array is missing exactly one number from this range. Find the missing number.

#### **Example**
- Input: `arr = [1, 2, 4, 6, 3, 7, 8]`
- Output: `5`  
The range is \( 1 \) to \( 8 \), and \( 5 \) is missing.

---


#### **Explanation**
1. Iterate through numbers from \( 1 \) to \( n+1 \).
2. For each number, check if it is in the array.
3. The first number that is not found is the missing number.

#### **Time Complexity**
- Iterating through \( 1 \) to \( n+1 \): \( O(n) \).
- Checking if a number exists in the array: \( O(n) \).  
**Overall Complexity**: \( O(n^2) \).

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


### **Example**

#### **Input**:
`arr = [1, 2, 4, 6, 3, 7, 8]`

#### **Output**:
- **Naive Approach**: `5`
- **Best Approach**: `5`

---
