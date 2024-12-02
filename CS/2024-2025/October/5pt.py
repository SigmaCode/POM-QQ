def find_path(start_airport, end_airport, tags): 
    
    # Initialize the path with the start airport
    path = [start_airport]
    current = start_airport
    
    # Follow the path until we reach the end airport
    while current != end_airport:
        current = tags[current]
        path.append(current)
    
    return path

if __name__ == "__main__":
    
    with open('input.txt', 'r') as f:
        
        # Read the first line
        first_line = f.readline().strip().split()
        n = int(first_line[0])
        start_airport = first_line[1]
        end_airport = first_line[2]
        
        # Read airport tags
        tags = dict()
        for _ in range(n):
            source, dest = f.readline().strip().split()
            tags[source] = dest

    # Get path
    path = find_path(start_airport, end_airport, tags)
    
    with open('output.txt', 'w') as f:
        f.write(' '.join(path))