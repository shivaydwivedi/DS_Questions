# Question-9: Merge the Two Sorted Arrays without Using Extra Space

## Problem Statement:
Merge two sorted arrays into a single sorted array without using any extra space.

### **Solution:**

We need to merge two sorted arrays into one sorted array without using extra space. This means we cannot create an additional array to hold the merged result. We will modify the given arrays in place.

---

### **Naive Approach:**

In the naive approach, we would typically merge the two arrays by creating an extra array and using a two-pointer technique. However, since the problem requires no extra space, this approach is not applicable. The naive approach would ideally work with extra space, but we will now focus on the optimal approach.

---

### **Best Approach (Optimal):**

The optimal solution uses a technique called **in-place merging**. Here we will merge the two sorted arrays by iterating over both arrays and swapping elements as needed. This process avoids extra space by using the arrays themselves to hold the merged result.

We will use the **gap method** for in-place merging. The gap method works by:
1. Calculating the initial gap, which is roughly half the total number of elements in both arrays.
2. Iterating through the arrays and comparing elements that are a certain gap distance apart.
3. Reducing the gap by half in each iteration until it becomes 1 (similar to how we perform the final pass in bubble sort).

#### **Steps:**
1. Start by calculating the gap as the sum of lengths of both arrays divided by 2.
2. Compare and swap elements from both arrays that are `gap` distance apart.
3. Continue reducing the gap until it reaches 1.
4. At the end of the process, both arrays will be merged in place.

#### **Time Complexity:**
- **O(n log n)**, where `n` is the total number of elements in both arrays. The gap is reduced logarithmically and comparisons are made in a linear scan.

#### **Space Complexity:**
- **O(1)**: No extra space is used.

---

### **Explanation with Example:**

#### **Example:**

For the input arrays:
- `arr1 = [1, 5, 9]`
- `arr2 = [2, 3, 8, 10]`

1. Initial gap is calculated as `(3 + 4) // 2 = 3`.
2. First pass (gap = 3): We compare and swap elements that are 3 places apart.
   - Swap `arr1[0]` and `arr2[3]` (1 and 10).
   - The arrays now look like: `arr1 = [10, 5, 9]` and `arr2 = [2, 3, 8, 1]`.
3. Next, the gap is reduced to 1, and the process continues comparing adjacent elements.
4. The final merged arrays are: `arr1 = [1, 2, 3]` and `arr2 = [5, 8, 9, 10]`.

**Output**:  
`Merged Arrays: ([1, 2, 3], [5, 8, 9, 10])`

---



