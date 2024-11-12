def findMinimumVariance(height):
    n = len(height)
    min_variance = float('inf')
    
    last_seen = {}
    
    for i in range(n):
        if height[i] in last_seen:
            left = last_seen[height[i]]
            group = height[left:i + 1]
            group_size = len(group)
            first_element_count = group.count(height[i]) 
            variance = group_size - first_element_count
            min_variance = min(min_variance, variance)
        
        last_seen[height[i]] = i
    
    return min_variance


height = list(map(int, input().split()))
print(findMinimumVariance(height))
