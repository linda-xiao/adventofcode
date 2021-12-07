# DAY 5: Part 2

input = open('2021/5/input.txt').read().split('\n')

# Remove all empty lines in input
input.pop()

# Matrix of numbers of times each coordinate occurs (starting with zeros)
matrix = []
for i in range(0,1000):
    matrix.append([0] * 1000)

# Function for diagonal lines
def diagLines(matrix,x1,x2,y1,y2):

    # Increase in x and y
    if (x2 > x1 and y2 > y1):
        xRange = range(x1,x2+1)
        yRange = range(y1,y2+1)
        for i in range(0,(x2-x1)+1):
            matrix[xRange[i]][yRange[i]] += 1

    # Increase in x, decrease in y
    elif (x2 > x1 and y2 < y1):
        xRange = range(x1,x2+1)
        yRange = range(y1,y2-1,-1)
        for i in range(0,(x2-x1)+1):
            matrix[xRange[i]][yRange[i]] += 1

    # Decrease in x and y
    elif (x2 < x1 and y2 < y1):
        xRange = range(x1,x2-1,-1)
        yRange = range(y1,y2-1,-1)
        for i in range(0,abs(x2-x1)+1):
            matrix[xRange[i]][yRange[i]] += 1

    # Decrease in x, increase in y
    elif (x2 < x1 and y2 > y1):
        xRange = range(x1,x2-1,-1)
        yRange = range(y1,y2+1)
        for i in range(0,abs(x2-x1)+1):
            matrix[xRange[i]][yRange[i]] += 1

    return matrix

# Function for horizontal lines
def horLines(matrix,x1,x2,y):

    # Increase in x
    if x2 > x1:
        for i in range(x1,x2+1):
            matrix[i][y] += 1

    # Decrease in x
    elif x2 < x1:
        for i in range(x1,x2-1,-1):
            matrix[i][y] += 1

    return matrix

# Function for vertical lines
def vertLines(matrix,y1,y2,x):

    # Increase in y
    if y2 > y1:
        for i in range(y1,y2+1):
            matrix[x][i] += 1

    # Decrease in y
    elif y2 < y1:
        for i in range(y1,y2-1,-1):
            matrix[x][i] += 1

    return matrix

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

    # Diagonal line
    if (x2 != x1 and y2 != y1):
        matrix = diagLines(matrix,x1,x2,y1,y2)

    # Horizontal line
    elif y1 == y2:
        matrix = horLines(matrix,x1,x2,y1)

    # Vertical line
    elif x1 == x2:
        matrix = vertLines(matrix,y1,y2,x1)

# Counter of overlaps
overlap = 0

# Check for overlaps in matrix
for line in matrix:
    for i in line:
        if i > 1:
            overlap += 1

# Solution
print('Number of overlaps: ' + str(overlap))
