# Question 13: Find the Minimum Platforms Required for Trains

# Naive Approach

def find_platforms_naive(arrivals, departures):
    n = len(arrivals)
    max_platforms = 0
    
    for i in range(n):
        platforms_needed = 1  # Count the current train
        for j in range(i + 1, n):
            if arrivals[j] < departures[i]:  # Overlap condition
                platforms_needed += 1
        max_platforms = max(max_platforms, platforms_needed)
    
    return max_platforms

# Example Usage
arrivals = [900, 940, 950, 1100, 1500, 1800]
departures = [910, 1200, 1120, 1130, 1900, 2000]
result = find_platforms_naive(arrivals, departures)
print(f"Minimum Platforms Needed: {result}")


# Best Approach (Using Sorting)

def find_platforms_optimized(arrivals, departures):
    arrivals.sort()
    departures.sort()
    n = len(arrivals)
    
    platform_needed = 0
    max_platforms = 0
    i, j = 0, 0
    
    while i < n and j < n:
        if arrivals[i] < departures[j]:  # A train arrives before the previous departs
            platform_needed += 1
            max_platforms = max(max_platforms, platform_needed)
            i += 1
        else:  # A train departs
            platform_needed -= 1
            j += 1
    
    return max_platforms

# Example Usage
arrivals = [900, 940, 950, 1100, 1500, 1800]
departures = [910, 1200, 1120, 1130, 1900, 2000]
result = find_platforms_optimized(arrivals, departures)
print(f"Minimum Platforms Needed: {result}")
