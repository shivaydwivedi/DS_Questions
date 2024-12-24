### **Question 15: Maximum Product Subarray**

---

### **Problem Statement**

Given an array of integers, find the contiguous subarray (containing at least one number) that has the maximum product, and return the product.

#### **Example**
- Input: `[2, 3, -2, 4]`
- Output: `6`  
  (Subarray: `[2, 3]`)

---

### **Naive Approach**

#### **Explanation**
1. Use two nested loops:
   - Outer loop starts at each index of the array.
   - Inner loop calculates the product of the subarray starting from the outer loop's index.
2. Track the maximum product found during the traversal.

#### **Steps**
- Traverse each index \( i \) of the array.
- For each \( i \), calculate the product for all subarrays starting from \( i \).
- Update the maximum product if the current product is greater.

#### **Time Complexity**
- \( O(n^2) \), where \( n \) is the size of the array.

#### **Space Complexity**
- \( O(1) \), no additional space is used.



### **Best Approach (Dynamic Programming)**

#### **Explanation**
1. Use two variables:
   - `max_product` to store the maximum product ending at the current index.
   - `min_product` to store the minimum product ending at the current index.
2. For each element:
   - If the element is negative, swap `max_product` and `min_product` because multiplying by a negative flips the maximum and minimum.
   - Update `max_product` to be the maximum of the current element and the product of the current element with the previous `max_product`.
   - Update `min_product` similarly.
3. Track the global maximum product during the traversal.

#### **Steps**
- Traverse the array while maintaining `max_product` and `min_product`.
- Update the global maximum product at each step.

#### **Time Complexity**
- \( O(n) \), single traversal of the array.

#### **Space Complexity**
- \( O(1) \), no additional space is used.


### **Example**

#### **Input**:
- Array: `[2, 3, -2, 4]`

#### **Output**:
- **Naive Approach**: `6`
- **Best Approach**: `6`

---

