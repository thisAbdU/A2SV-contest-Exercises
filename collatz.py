

def collatz_sequence():
    memo = {}  
    max_count = 0  # Variable to store the maximum sequence count
    index = 0  # Variable to store the number with the maximum sequence count

    # Loop from 1 to 1,000,000
    for j in range(1, 10**18 + 1):
        count = 1  # Initialize the count for the current number
        i = j  # Use a temporary variable to compute the Collatz sequence
        
        # Compute the Collatz sequence
        while i > 1:
            # If the sequence is not already computed, calculate it
            if i not in memo:
                if i % 2 == 0:
                    i = i // 2
                else:
                    i = 3 * i + 1
                count += 1
            else:
                # If already computed, add the memoized value and break
                count += memo[i] - 1
                break

        # Store the sequence count for the current number
        memo[j] = count
        
        # Update the maximum count and the corresponding number
        if max_count < count:
            max_count = count
            index = j

    # Return the number with the longest Collatz sequence
    return index

collatz_sequence()

