def dp(T, potions):
    
    # dp[i] will store the closest potency to i that can be achieved using the potions.
    # Initially, we set all values to infinity.
    dp = [float("inf")] * (T + 2)
    
    # Can achieve a potency of 0 by using 0 of the potions.
    dp[0] = 0
    
    # count will store the number of each potion used to achieve the closest potency.
    count = [[0,0,0,0]] * (T + 2)
    
    # Iterate through all possible potencies.
    for i in range(1, T+2):
        
        # Iterate through all potions.
        for j, potion in enumerate(potions):
            
            # Look at the closest potency to potency i. Make sure to not go below 0.
            ind = max(i-potion, 0)
            
            # First condition is to check if the current 
            # combination is closer ot the target potency than the previous one.
            # For the second condition, if it is equally close, we take the
            # lexicographically smaller combination.
            if (abs(dp[ind] + potion - i) < abs(dp[i]-i) or
                (abs(dp[ind] + potion - i) == abs(dp[i]-i) and count[ind] < count[i])):
                
                # Update the closest potency
                dp[i] = dp[ind] + potion
                
                # Copy the combination of potions, add one to the potion used.
                count[i] = count[ind][:]
                count[i][j] += 1

    # Return the combination of potions used to achieve the closest potency to T.
    return count[T]


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        line = [int(x) for x in f.readline().strip().split()]
        
        T, potions = line[0], line[1:]
        
    with open("output.txt", "w") as f:
        f.write(" ".join([str(x) for x in dp(T, potions)]))
        