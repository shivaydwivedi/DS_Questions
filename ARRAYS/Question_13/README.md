### **Question 13: Find the Minimum Platforms Required for Trains**

---

### **Problem Statement**

Given the arrival and departure times of trains, find the minimum number of platforms required at the station so that no train has to wait.

#### **Example**
- Input:
  - Arrival Times: `[900, 940, 950, 1100, 1500, 1800]`
  - Departure Times: `[910, 1200, 1120, 1130, 1900, 2000]`
- Output: `3`

---

### **Naive Approach**

#### **Explanation**
1. Iterate through the arrival and departure times for each train.
2. For each train, check how many other trains are present at the platform at the same time.
3. Update the maximum count of platforms needed.

#### **Steps**
- Traverse each train's arrival time.
- Count overlapping trains by checking if their arrival is before the departure of others.
- Keep track of the maximum count.

#### **Time Complexity**
- \( O(n^2) \), where \( n \) is the number of trains.

#### **Space Complexity**
- \( O(1) \), no extra space is used.



### **Best Approach (Using Sorting)**

#### **Explanation**
1. Sort the arrival and departure times.
2. Use two pointers to traverse the sorted times:
   - Increment the platform count for an arrival.
   - Decrement it for a departure.
3. Track the maximum platform count during traversal.

#### **Steps**
- Sort the arrival and departure arrays.
- Use two pointers, one for arrivals and another for departures.
- Traverse through the arrays, comparing current arrival and departure times.
- Update the platform count and keep track of the maximum.

#### **Time Complexity**
- \( O(n \log n) \), for sorting the arrival and departure times.

#### **Space Complexity**
- \( O(1) \), as no additional space is used.

### **Example**

#### **Input**:
- Arrival Times: `[900, 940, 950, 1100, 1500, 1800]`
- Departure Times: `[910, 1200, 1120, 1130, 1900, 2000]`

#### **Output**:
- **Naive Approach**: `3`
- **Best Approach**: `3`

---

