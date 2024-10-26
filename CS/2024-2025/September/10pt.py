with open("input.txt") as input_file:
    n = int(input_file.readline())
    dirs = input_file.readline().split()

# relative offset doesn't matter in this problem, just start at (0,0)
(x, y) = (0, 0)

# this will store every past position
visited = set()
# True unless a shortcut is discovered
shortest = True

for dir in dirs:
    match dir:
        case "R":
            (nextx, nexty) = (x + 1, y)
        case "L":
            (nextx, nexty) = (x - 1, y)
        case "U":
            (nextx, nexty) = (x, y + 1)
        case "D":
            (nextx, nexty) = (x, y - 1)

    # if an adjacent cell from more than 1 step ago was visited, path cannot be the shortest
    if (
        (nextx, nexty) in visited
        or (nextx + 1, nexty) in visited
        or (nextx - 1, nexty) in visited
        or (nextx, nexty + 1) in visited
        or (nextx, nexty - 1) in visited
    ):
        shortest = False
        break

    visited.add((x, y))
    (x, y) = (nextx, nexty)

with open("output.txt", "w") as output_file:
    output_file.write("YES" if shortest else "NO")
