# DAY 5: Part 1 (super ineffective and time consuming)

input = open('2021/5/input.txt').read().split('\n')

# Remove all empty lines in input
input.pop()

# List of coordinates
coord = []

for line in input:

    # Split first and second entry
    entries = line.split(' -> ')

    # Split first entry into x- and y-coordinates
    firstEntry = entries[0]
    firstEntrySplit = firstEntry.split(',')
    x1 = int(firstEntrySplit[0])
    y1 = int(firstEntrySplit[1])

    # Split second entry into x- and y-coordinates
    secondEntry = entries[1]
    secondEntrySplit = secondEntry.split(',')
    x2 = int(secondEntrySplit[0])
    y2 = int(secondEntrySplit[1])

    # Skip diagonal lines
    if (x2 != x1 and y2 != y1):
        continue

    else:

        # Horizontal line (increase)
        if x2 > x1:

            # Increase x1 to x2, keep y
            for i in range(x1,x2+1):
                coord.append((i,y1))

        # Horizontal line (decrease)
        elif x2 < x1:

            # Decrease x1 to x2, keep y
            for i in range(x1,x2-1,-1):
                coord.append((i,y1))

        # No change in horizontal direction
        else:

            # Vertical line (increase)
            if y2 > y1:

                # Increase y1 to y2, keep x
                for i in range(y1,y2+1):
                    coord.append((x1,i))

            elif y2 < y1:

                # Decrease y1 to y2, keep x
                for i in range(y1,y2-1,-1):
                    coord.append((x1,i))

# List of overlaps
overlap = []

# For every coordinate (ineffective loop)
for i in coord:

    # If there are more than one of the same coordinate, append to list
    if coord.count(i) > 1:
        overlap.append(i)

# Delete duplicates in list of only overlaps
overlap = list(set(overlap))

# Solution
print('Number of overlaps: ' + str(len(overlap)))
