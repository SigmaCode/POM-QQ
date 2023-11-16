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


#5pt specific function

def isIsolated(y0: int, x0: int) -> bool:
    """Checks if there is a bacterium nearby and returns False if it finds one. Returns True otherwise."""
    for (y,x) in nearbyCells(y0,x0):
        if petri_dish[y][x] == "#":
            return False
    return True

def countIsolated() -> int:
    """Counts the number of isolated bacteria."""
    counter = 0
    for y in range(length):
        for x in range(width):
            if (petri_dish[y][x] == "#"):
                if (isIsolated(y,x)):
                    print("Added to counter")
                    counter += 1
    return counter

if __name__ == "__main__":
    setup()
    save(str(countIsolated()))