if __name__ == "__main__":
    
    with open('input.txt', 'r') as f:
        
        # Read n
        first_line = f.readline()
        n = int(first_line)
        # print(n)
        
        # Read brightnesses.
        brightnesses = [int(x) for x in f.readline().strip().split()]
        # print(brightnesses)
        
        result = []
        
        for i, val in enumerate(brightnesses):
            if i == 0:
                result.append(0)
            else:
                if result[i-1] == 0:
                    result.append(0 if val >= brightnesses[i-1] else brightnesses[i-1])
                else:
                    result.append(0 if val >= result[i-1] else result[i-1])
    
    with open('output.txt', 'w') as f:
        f.write(' '.join([str(x) for x in result]))