def visit(n, edges, i, visited: set, threshold, size):
    if i in visited or stars[i][2] <= thresholds[k]:
        return 0
    visited.add(i)
    size += 1
    for j in range(n):
        if {i, j} in edges:
            size += visit(n, edges, j, visited, threshold, size)
    return size

if __name__ == "__main__":
    
    with open('input.txt', 'r') as f:
        
        # Read n, d, m, and thresholds
        n, d, m = [int(x) for x in f.readline().strip().split()]
        thresholds = [int(x) for x in f.readline().strip().split()]
        
        stars = []
        result = []
        for i in range(n):
            x, y, b = [int(x) for x in f.readline().strip().split()]
            stars.append((x, y, b))
        
        for k in range(m):
            edges = []
            for i in range(n):
                if stars[i][2] <= thresholds[k]:
                    continue
                for j in range(i):
                    if stars[j][2] <= thresholds[k]:
                        continue
                    if (stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2 < d**2:
                        edges.append({i, j})    
            
            components = 0
            visited = set()
            for i in range(n):
                if i not in visited:
                    size = visit(n, edges, i, visited, thresholds[k], 0)
                    if size >= 2:
                        components += 1
            result.append(components)

    with open('output.txt', 'w') as f:
        f.write(' '.join([str(x) for x in result]))