def naive(T, S1, S2, S3, S4):
    
    # Track the closest combination of potions.
    closest_combination = [0, 0, 0, 0]
    
    # Closest distance to the target potency.
    closest_distance = float("inf")
    
    # Iterate through all possible combinations of potions.
    for a in range(T//S1+2):
        for b in range(T//S2+2):
            for c in range(T//S3+2):
                for d in range(T//S4+2):
                    
                    # If the combination is better than the current best, update it.
                    distance = abs(T - (a*S1 + b*S2 + c*S3 + d*S4))
                    if distance < closest_distance:
                        closest_combination = [a, b, c, d]
                        closest_distance = distance
    
    return closest_combination


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        line = [int(x) for x in f.readline().strip().split()]
        
        T, S1, S2, S3, S4 = line
        
    with open("output.txt", "w") as f:
        f.write(" ".join([str(x) for x in naive(T, S1, S2, S3, S4)]))
        