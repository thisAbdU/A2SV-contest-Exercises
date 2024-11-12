def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index + n]))
        index += n
        
        # Step 1: Create a set to track unique elements and their first occurrence.
        seen = set()
        result = []
        
        for num in a:
            if num not in seen:
                seen.add(num)
                result.append(num)
        
        # Step 2: Adjust the result sequence to minimize lexicographical order
        final_result = []
        for i, num in enumerate(result):
            if i % 2 == 0:  # odd positions in 1-based index (0, 2, 4 in 0-based index)
                final_result.append(-num)
            else:
                final_result.append(num)
        
        # Append result for this test case
        results.append(f"{len(final_result)}")
        results.append(" ".join(map(str, final_result)))
    
    # Output all results
    sys.stdout.write("\n".join(results) + "\n")
