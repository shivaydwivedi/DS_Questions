**Question 2: Rotate an Array by K Positions**.

---

### **Problem Statement**

You are given an array and a number \( K \). Rotate the array to the right by \( K \) positions. Rotation means elements at the end of the array move to the beginning, while other elements are shifted right.

For example:
- Input: `arr = [1, 2, 3, 4, 5], K = 2`
- Output: `[4, 5, 1, 2, 3]`

---

### **Naive Approach**

#### **Explanation**
1. Rotate the array \( K \) times by moving the last element to the front of the array repeatedly.
2. Each rotation involves removing the last element and inserting it at the beginning.

#### **Time Complexity**
- Rotating once: \(O(n)\) (remove and insert operations).
- Rotating \( K \) times: \(O(n \times K)\).

#### **Code**
```python
def rotate_array_naive(arr, k):
    n = len(arr)
    k %= n  # Handle cases where k > n
    for _ in range(k):
        last_element = arr.pop()  # Remove the last element
        arr.insert(0, last_element)  # Insert it at the beginning
    return arr

# Example Usage
arr = [1, 2, 3, 4, 5]
k = 2
print("Rotated Array (Naive):", rotate_array_naive(arr, k))
```

---

### **Best Approach (Using Slicing)**

#### **Explanation**
1. Use array slicing to avoid repeated rotations.
2. Steps:
   - Find \( K \mod N \) to handle cases where \( K > N \).
   - Divide the array into two parts: the last \( K \) elements and the first \( N-K \) elements.
   - Concatenate these two parts in reverse order.

#### **Time Complexity**
- Slicing and concatenation: \(O(n)\).

#### **Code**
```python
def rotate_array_best(arr, k):
    n = len(arr)
    k %= n  # Handle cases where k > n
    return arr[-k:] + arr[:-k]

# Example Usage
arr = [1, 2, 3, 4, 5]
k = 2
print("Rotated Array (Best):", rotate_array_best(arr, k))
```

---

### **Example**

#### **Input**:
`arr = [1, 2, 3, 4, 5], K = 2`

#### **Output**:
- **Naive Approach**: `[4, 5, 1, 2, 3]`
- **Best Approach**: `[4, 5, 1, 2, 3]`

---
