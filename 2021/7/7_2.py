# DAY 7: Part 2

input = open('2021/7/input.txt').read()

# Split into separate elements
horizontalPos = input.split(',')

# Strip newline from last element
horizontalPos[-1] = horizontalPos[-1].strip('\n')

# Function that finds average value of list
def average(input):

    # Find sum
    sum = 0
    for i in input:
        i = int(i)
        sum += i

    # Average
    average = int(float(sum)/len(input))

    return average

# Find the position where the crabs should align
alignPos = average(horizontalPos)

# Fuel count
fuel = 0

for pos in horizontalPos:
    pos = int(pos)

    # Number of steps
    steps = abs(pos - int(alignPos))

    # For every step, add more fuel
    for i in range(1,steps+1):
        fuel += i

# Solution
print('Align position: ' + str(alignPos))
print('Required fuel: ' + str(fuel))
