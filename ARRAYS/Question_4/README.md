### **Question 4: Sort an Array of 0s, 1s, and 2s (Dutch National Flag Problem)**

---

### **Problem Statement**

You are given an array consisting of only 0s, 1s, and 2s. Your task is to sort the array in ascending order without using any sorting algorithm like quicksort or mergesort. 

#### **Example**
- Input: `arr = [0, 2, 1, 2, 0, 1, 1, 0]`
- Output: `[0, 0, 0, 1, 1, 1, 2, 2]`

---

### **Naive Approach (Counting Elements)**

#### **Explanation**
1. Count the number of 0s, 1s, and 2s in the array.
2. Reconstruct the array by appending 0s, 1s, and 2s in order.

#### **Steps**
- Iterate through the array to count occurrences of each element.
- Use the counts to overwrite the array.

#### **Time Complexity**
- Counting: \( O(n) \).
- Reconstructing the array: \( O(n) \).  
**Overall Complexity**: \( O(n) \).

#### **Space Complexity**
- Requires \( O(1) \) additional space.

---

### **Best Approach (Dutch National Flag Algorithm)**

#### **Explanation**
1. Use three pointers: 
   - `low`: Keeps track of where 0s should go.
   - `mid`: Iterates through the array.
   - `high`: Keeps track of where 2s should go.
2. Steps:
   - If `arr[mid] == 0`, swap it with `arr[low]` and move both `low` and `mid` forward.
   - If `arr[mid] == 1`, just move `mid` forward.
   - If `arr[mid] == 2`, swap it with `arr[high]` and move `high` backward.

#### **Time Complexity**
- Single traversal of the array: \( O(n) \).

#### **Space Complexity**
- \( O(1) \), as no extra space is used.

---

### **Example**

#### **Input**:
`arr = [0, 2, 1, 2, 0, 1, 1, 0]`

#### **Output**:
- **Naive Approach**: `[0, 0, 0, 1, 1, 1, 2, 2]`
- **Best Approach**: `[0, 0, 0, 1, 1, 1, 2, 2]`

---

