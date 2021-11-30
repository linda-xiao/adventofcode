# DAY 3: Task 1

input = open('2019/3/input.txt').read().split('\n')

# Remove the last (empty) element in the list
input.pop()

# Function for saving all the passed coordinates in a list as tuples (x,y)
def wireCoord(path):

    # Define x- and y-position of central port (start position)
    x = 0
    y = 0

    # List of coordinates
    coord = []

    # Split the path into steps
    step = path.split(',')

    # For every step
    for i in step:

        # Right
        if i[0] == 'R':

            # Create list with all the passed x-coordinates
            xlistR = range(x+1, x + int(i[1:])+1)

            # Update the x-position of the wire
            x += int(i[1:])

            # Store the coordinates in a list
            for pos in xlistR:
                coord.append((pos,y))

        # Up
        elif i[0] == 'U':

            # Create list with all the passed y-coordinates
            ylistU = range(y+1, y + int(i[1:])+1)

            # Update the y-position of the wire
            y += int(i[1:])

            # Store the coordinates in a list
            for pos in ylistU:
                coord.append((x,pos))

        # Left
        elif i[0] == 'L':

            # Create list with all the passed x-coordinates
            xlistL = range(x-1, x - int(i[1:])-1, -1)

            # Update the x-position of the wire
            x += -int(i[1:])

            # Store the coordinates in a list
            for pos in xlistL:
                coord.append((pos,y))

        # Down
        elif i[0] == 'D':

            # Create list with all the passed y-coordinates
            ylistD = range(y-1, y - int(i[1:])-1, -1)

            # Update the y-position of the wire
            y += -int(i[1:])

            # Store the coordinates in a list
            for pos in ylistD:
                coord.append((x, pos))

    # Output is the coordinates
    return coord

# Coordinates of the wires
firstWire = wireCoord(input[0])
secondWire = wireCoord(input[1])

# Convert one of the two lists to a set
firstWireSet = set(firstWire)

# Find the intersections between the first and second wire
intersectionSet = firstWireSet.intersection(secondWire)

# List of intersections and Manhattan distances to intersections
ints = []
dist = []

for intersection in intersectionSet:
    ints.append(intersection)
    dist.append(abs(intersection[0]) + abs(intersection[1]))

# Manhattan distance to closest intersection
print(min(dist))
