# DAY 9: Part 1

input = open('2021/9/input.txt').read().split('\n')

# Remove the last (empty) element in the list
input.pop()

# List of low points (locations that are lower than any of its adjacent locations)
lowPoints = []

# Function that checks adjacent numbers for top row elements
def topAdjacent(currentRow,nextRow):

    # Temporary list of low points
    lowPointsTemp = []

    # Left corner
    if (currentRow[0] < currentRow[1] and currentRow[0] < nextRow[0]):
        lowPointsTemp.append(currentRow[0])

    # Right corner
    if (currentRow[-1] < currentRow[-2] and currentRow[-1] < nextRow[-1]):
        lowPointsTemp.append(currentRow[-1])

    # Top edge
    for i in range(1,len(currentRow)-1):
        if (currentRow[i] < currentRow[i-1] and currentRow[i] < currentRow[i+1] and currentRow[i] < nextRow[i]):
            lowPointsTemp.append(currentRow[i])

    return lowPointsTemp

# Function that checks adjacent numbers for bottom row elements
def bottomAdjacent(currentRow,previousRow):

    # Temporary list of low points
    lowPointsTemp = []

    # Left corner
    if (currentRow[0] < currentRow[1] and currentRow[0] < previousRow[0]):
        lowPointsTemp.append(currentRow[0])

    # Right corner
    if (currentRow[-1] < currentRow[-2] and currentRow[-1] < previousRow[-1]):
        lowPointsTemp.append(currentRow[-1])

    # Bottom edge
    for i in range(1,len(currentRow)-1):
        if (currentRow[i] < currentRow[i-1] and currentRow[i] < currentRow[i+1] and currentRow[i] < previousRow[i]):
            lowPointsTemp.append(currentRow[i])

    return lowPointsTemp

# Function that checks adjacent numbers for side edge elements (three adjacent) and center elements (four adjacent)
def restAdjacent(previousRow,currentRow,nextRow):

    lowPointsTemp = []

    # Check first number in every row (left edge)
    if (currentRow[0] < currentRow[1] and currentRow[0] < previousRow[0] and currentRow[0] < nextRow[0]):
        lowPointsTemp.append(currentRow[0])

    # Check last number in every row (right edge)
    if (currentRow[-1] < currentRow[-2] and currentRow[-1] < previousRow[-1] and currentRow[-1] < nextRow[-1]):
        lowPointsTemp.append(currentRow[-1])

    # Check center numbers
    for i in range(1,len(currentRow)-1):
        if(currentRow[i] < currentRow[i-1] and currentRow[i] < currentRow[i+1] and currentRow[i] < previousRow[i] and currentRow[i] < nextRow[i]):
            lowPointsTemp.append(currentRow[i])

    return lowPointsTemp

# Main
for i in range(0,len(input)):

    # First row
    if input.index(input[i]) == 0:

        lowPointsTemp = topAdjacent(input[i],input[i+1])
        if len(lowPointsTemp) > 0:
            for i in lowPointsTemp:
                lowPoints.append(i)

    # Last row
    elif input.index(input[i]) == len(input)-1:

        lowPointsTemp = bottomAdjacent(input[i],input[i-1])
        if len(lowPointsTemp) > 0:
            for i in lowPointsTemp:
                lowPoints.append(i)

    # Rest of the elements
    elif input.index(input[i]) in range(1,len(input)-1):

        lowPointsTemp = restAdjacent(input[i-1],input[i],input[i+1])
        if len(lowPointsTemp) > 0:
            for i in lowPointsTemp:
                lowPoints.append(i)

# Sum of risk levels
sum = 0

# For every low point in list
for i in lowPoints:

    # Risk level is 1 + the height of the low point
    riskLevel = 1 + int(i)

    # Add risk level to sum
    sum += riskLevel

# Solution
print('Sum of risk levels of all low points: ' + str(sum))
