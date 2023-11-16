# Helper functions

def setup() -> None:
    """Reads input from input.txt and puts it in petri_dish."""
    with open("input.txt") as input_file:
        # Reads the first line and assigns value to width and length
        line = input_file.readline()
        global width, length
        width, length = line.split(" ")
        # Convert to numbers
        width, length = int(width), int(length)
        global petri_dish
        petri_dish = [input_file.readline().strip() for i in range(length)]
def save(output) -> None:
    """Saves output to output.txt."""
    with open("output.txt", "w") as output_file:
        output_file.write(output)
        
def nearbyCells(y: int, x: int) -> list[tuple[int]]:
    """Returns a list of nearby cells."""
    nearby = []
    if width == 1:
        if y == 0:
            if length != 1:
                nearby.append((y + 1,x))
        elif y == length - 1:
            nearby.append((y - 1,x))
        else:
            nearby.append((y + 1,x))
            nearby.append((y - 1,x))
    elif x == 0:
        nearby.append((y,x + 1))
        if y == 0:
            if length != 1:
                nearby.append((y + 1,x))
                nearby.append((y + 1,x + 1))
        elif y == length - 1:
            nearby.append((y - 1,x))
            nearby.append((y - 1,x + 1))
        else:
            nearby.append((y + 1,x))
            nearby.append((y + 1,x + 1))
            nearby.append((y - 1,x))
            nearby.append((y - 1,x + 1))
    elif x == width - 1:
        nearby.append((y,x - 1))
        if y == 0:
            if length != 1:
                nearby.append((y + 1,x - 1))
                nearby.append((y + 1,x))
        elif y == length - 1:
            nearby.append((y - 1,x - 1))
            nearby.append((y - 1,x))
        else:
            nearby.append((y + 1,x - 1))
            nearby.append((y + 1,x))
            nearby.append((y - 1,x - 1))
            nearby.append((y - 1,x))
    else:
        nearby.append((y,x - 1))
        nearby.append((y,x + 1))
        if y == 0:
            if length != 1:
                nearby.append((y + 1,x - 1))
                nearby.append((y + 1,x))
                nearby.append((y + 1,x + 1))
        elif y == length - 1:
            nearby.append((y - 1,x - 1))
            nearby.append((y - 1,x))
            nearby.append((y - 1,x + 1))
        else:
            nearby.append((y + 1,x - 1))
            nearby.append((y + 1,x))
            nearby.append((y + 1,x + 1))
            nearby.append((y - 1,x - 1))
            nearby.append((y - 1,x))
            nearby.append((y - 1,x + 1))
    return nearby

def nearbyCheckedCells(y: int, x: int) -> list[tuple[int]]:
    """Returns a list of nearby cells that have already been checked and have a bacterium in them."""
    nearby = []
    if x == 0:
        if y != 0:
            if petri_dish[y - 1][x] == "#": nearby.append((y - 1,x))
            if petri_dish[y - 1][x + 1] == "#": nearby.append((y - 1,x + 1))
    elif x == width - 1:
        if petri_dish[y][x - 1] == "#": nearby.append((y,x - 1))
        if y != 0:
            if petri_dish[y - 1][x - 1] == "#": nearby.append((y - 1,x - 1))
            if petri_dish[y - 1][x] == "#": nearby.append((y - 1,x))
    else:
        if petri_dish[y][x - 1] == "#": nearby.append((y,x - 1))
        if y != 0:
            if petri_dish[y - 1][x - 1] == "#": nearby.append((y - 1,x - 1))
            if petri_dish[y - 1][x] == "#": nearby.append((y - 1,x))
            if petri_dish[y - 1][x + 1] == "#": nearby.append((y - 1,x + 1))
    return nearby

def lookforNearbyColonies(y: int, x: int, nearby: list[tuple[int]], colonies: list[list[tuple[int]]]) -> list[int]:
    """Checks whether or not there are any colonies near the cell we are considering."""
    nearby_colonies = []
    # Iterate through colonies, looking for nearby bacteria
    # Iterating in reverse order stops pop from messing up the indicies later on
    for c in range(len(colonies) - 1, -1, -1):
        for n in range(len(nearby)):
            if nearby[n] in colonies[c]:
                # If you find that a colony has one of the nearby cells
                # 1) Add that colony to the list of nearby colonies
                # 2) It's now pointless to look for that cell in other colonies, so don't include in the list of things to look for anymore
                # 3) Stop looking for nearby cells in this colony -- we don't want duplicates in our list
                nearby_colonies.append(c)
                nearby.pop(n)
                break
    return nearby_colonies

def mergeColonies(y: int, x: int, colonies: list[list[tuple[int]]]) -> list[list[tuple[int]]]:
    """Combines nearby colonies together."""
    nearby_colonies = lookforNearbyColonies(y, x, nearbyCheckedCells(y,x), colonies)
    # Iterate through every colony but the last, deleting them from the list of colonies and merging them with the last (which actually has the smallest index)
    for c in nearby_colonies[:-1]:
        colonies[nearby_colonies[-1]] += colonies.pop(c)
    
    if nearby_colonies:
        # If there are nearby colonies, add this cell to that colony
        colonies[nearby_colonies[-1]].append((y,x))
    else:
        # If there aren't, start a new one
        colonies.append([(y,x)])
    return colonies

def listColonies() -> list[list[tuple[int]]]:
    """Compiles a list of all the bacterial colonies."""
    colonies = []
    for y in range(length):
        for x in range(width):
            if petri_dish[y][x] == "#":
                # Only look for nearby colonies if there is a bacterium in the cell we are considering
                # Only have to check the bacteria that we've already iterated over
                colonies = mergeColonies(y, x, colonies)
    return colonies

def sumColonyLengths(nearby_colonies: list[int], original_colonies: list[list[tuple[int]]]) -> int:
    "Sums the lengths of the nearby colonies, adding one to account for the bacterium placed in the cell."
    return 1 + sum([len(original_colonies[c]) for c in nearby_colonies])

# def biggestColony(colonies: list[list[tuple[int]]]) -> int:
#     """Finds the maximum colony size from a list of colonies."""
#     return max([len(colony) for colony in colonies])

def bestPlace() -> tuple[int]:
    original_colonies = listColonies()
    max_size = 0
    for x in range(width):
        for y in range(length):
            if petri_dish[y][x] == ".":
                size = sumColonyLengths(lookforNearbyColonies(y, x, nearbyCells(y,x), original_colonies), original_colonies)
                if size > max_size:
                    max_size = size
                    current_winner = (y,x)
    return current_winner

if __name__ == "__main__":
    setup()
    (y,x) = bestPlace()
    save(f"{x} {y}")