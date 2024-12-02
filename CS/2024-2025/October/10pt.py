import csv
import random

all_routes = dict()
all_airports = set()
confirmed_airports = set()
confirmed_routes = dict()
n = 1

def recurse(curr, dest, airports_left, blank_tags_left, visited):
    
    if airports_left == 1:
        if curr == dest:
            return 1
        else:
            return 0
    
    if curr == dest and airports_left > 1:
        return 0

    
    visited.add(curr)

    
    result = 0
    
    if curr in confirmed_routes:
        result = recurse(confirmed_routes[curr], dest, airports_left - 1, blank_tags_left, visited)
    else:
        # Look if there are any blank tags left that are NOT among the confirmed airports. If so, use a blank tag.
        if blank_tags_left > 0 and curr in all_routes:
            for next in all_routes[curr]:
                if next in visited or next in confirmed_airports:
                    continue
                result += recurse(next, dest, airports_left - 1, blank_tags - 1, visited)
        
        # Also look at the confirmed airports.
        for next in confirmed_airports:
            if next in visited:
                continue
            # Check that it's a valid route to go from curr to next.
            if curr not in all_routes or next not in all_routes[curr]:
                continue
            result += recurse(next, dest, airports_left - 1, blank_tags, visited)
    visited.remove(curr)
    return result
    

if __name__ == "__main__":
    
    with open("routes-10pt.csv") as file:
        csv_reader = csv.reader(file)
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                if row[0] in all_routes:
                    all_routes[row[0]].append(row[1])
                else:
                    all_routes[row[0]] = [row[1]]
                all_airports.update([row[0], row[1]])
            line_count += 1

    with open("input.txt") as input:
        line_count = 0
        start = ""
        end = ""
        
        blank_tags = 0
        
        for line in input.readlines():
            if line_count == 0:
                n, start, end = [thing.rstrip() for thing in line.split(" ")]
                n = int(n)
                confirmed_airports.update([start, end])
            else:
                split = [thing.rstrip() for thing in line.split(" ")]
                if split[0] == "A":
                    confirmed_airports.add(split[1])
                    confirmed_airports.add(split[2])
                    confirmed_routes[split[1]] = split[2]
                elif split[0] == "B":
                    confirmed_airports.add(split[1])
                else:
                    blank_tags += 1
            line_count += 1
            
        visited = set()
        
        result = recurse(start, end, n+1, blank_tags, visited)
        print(result)