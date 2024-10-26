def solve():
    with open("input.txt") as f:
        lines = f.read().splitlines()
        
        # lines[0] corresponds to the total number of moves
        # lines[1] corresponds to the initial position
        # lines[2] corresponds to the desired position
        # lines[3] is the sequence of moves.
        
        # Get initial coordinates
        x, y = [int(z) for z in lines[1].split(" ")]
        
        # Get desired coordinates
        desired_x, desired_y = [int(z) for z in lines[2].split(" ")]
        
        # Update coordinate for each move
        for z in lines[3].split(" "):
            if z == "R":
                x += 1
            elif z == "L":
                x -= 1
            elif z == "U":
                y += 1
            elif z == "D":
                y -= 1
                
        # Return YES if the ending coordinates are the desired ones.
        return "YES" if (x == desired_x and y == desired_y) else "NO"

if __name__ == "__main__":
    with open("output.txt", "w") as f:
        f.write(solve())