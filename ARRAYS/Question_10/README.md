### Question-10:Rearrange an array such that even number comes before the odd numbers

### **Problem Statement:**

Given an array of integers, rearrange the array such that **all even numbers come before all odd numbers** while maintaining the relative order of even and odd numbers.

### **Input:**
- An array `arr[]` of integers, where the length of the array is `n`.

### **Output:**
- The array should be rearranged such that all even numbers appear before all odd numbers, while maintaining their original relative order.

### **Example 1:**

#### **Input:**
```python
arr = [12, 34, 45, 9, 8, 90, 3]
```

#### **Output:**
```python
[12, 34, 8, 90, 45, 9, 3]
```

#### **Explanation:**
The even numbers (12, 34, 8, 90) are moved to the front, maintaining their relative order, while the odd numbers (45, 9, 3) appear after them.

### **Example 2:**

#### **Input:**
```python
arr = [1, 2, 3, 4, 5, 6]
```

#### **Output:**
```python
[2, 4, 6, 1, 3, 5]
```

### **Approaches:**

#### **Naive Approach:**
In the naive approach, we could:
1. Create two separate lists: one for even numbers and one for odd numbers.
2. Iterate through the original array and separate the even and odd numbers into these lists.
3. Concatenate the even list followed by the odd list.

This approach would use extra space, which may not be optimal for large arrays.

#### **Optimal Approach (In-place solution):**
The optimal approach involves rearranging the array **in place** by iterating through the array and using the two-pointer technique. We can maintain two pointers:
- `left`: This pointer will be used to place even numbers at the beginning.
- `right`: This pointer will be used to place odd numbers at the end.

We move through the array once and swap elements as needed.

### **Explanation of Naive Approach:**

- We use two separate lists to store the even and odd numbers.
- We iterate over the original array and separate the numbers into the respective lists.
- Finally, we concatenate the two lists to form the rearranged array.

### **Time Complexity:**
- **O(n)** because we iterate over the array once to separate the even and odd numbers.

### **Space Complexity:**
- **O(n)** because we use two additional lists to store the even and odd numbers.

---

### **Optimal Approach (In-place Solution):**

In this approach, we will:
1. Use two pointers, `left` and `right`, to rearrange the array.
2. The `left` pointer will scan from the beginning of the array to place even numbers at the start.
3. The `right` pointer will scan from the end to place odd numbers at the end.
4. We swap elements when needed to achieve the desired rearrangement.



### **Explanation of Optimal Approach:**

- We maintain two pointers, `left` and `right`.
- `left` is used to find even numbers, and `right` is used to find odd numbers.
- If `arr[left]` is even, we simply increment `left`. If `arr[right]` is odd, we decrement `right`.
- If `arr[left]` is odd and `arr[right]` is even, we swap them and move both pointers inward.
- This process continues until `left` and `right` pointers meet.

### **Time Complexity:**
- **O(n)** because we only pass through the array once.

### **Space Complexity:**
- **O(1)** because the rearrangement happens in place without using any extra space.

---

