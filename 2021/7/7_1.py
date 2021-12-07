# DAY 7: Task 1

input = open('2021/7/input.txt').read()

# Split into separate elements
horizontalPos = input.split(',')

# Strip newline from last element
horizontalPos[-1] = horizontalPos[-1].strip('\n')

# Function that finds median value of list
def median(input):

    # List of sorted items
    sortList = []

    for i in input:

        # Append all items in input list as integers
        i = int(i)
        sortList.append(i)

    # Sort list
    sortList.sort()

    # Find median value
    # Even value
    if (len(sortList) % 2) == 0:

        # Take the average of the two values in the center
        median = (int(sortList[len(sortList)/2-1]) + int(sortList[len(sortList)/2])) / 2

    # Odd value
    else:

        # Take the center value
        median = sortList[len(sortList)/2]

    return median

# Find the position where the crabs should align
alignPos = median(horizontalPos)

# Fuel count
fuel = 0

for pos in horizontalPos:
    pos = int(pos)

    # Add the difference between the current position and the align position to fuel count
    fuel += abs(pos - alignPos)

# Solution
print('Align position: ' + str(alignPos))
print('Required fuel: ' + str(fuel))
