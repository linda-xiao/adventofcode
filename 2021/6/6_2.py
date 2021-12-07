# DAY 6: Part 2

input = open('2021/6/input.txt').read()

# Split into separate internal timers
initialState = input.split(',')

# Strip newline from last element
initialState[-1] = initialState[-1].strip('\n')

# Function that counts the number of fish at each position (internal timer)
def fishCount(currentCount,day):

    # Save (eventual) number of fish to be born :)
    fishBabies = currentCount[0]

    # Move all counts one position down
    for i in range(1,9):
        currentCount[i-1] = currentCount[i]

    # Set temporary count on position 8 to 0
    currentCount[8] = 0

    # If there are fish with internal timer 0
    if fishBabies > 0:

        # Set count on position 8 to the previously saved number at position 0
        currentCount[8] += fishBabies

        # Set count on position 6 to the previously saved number at position 0
        currentCount[6] += fishBabies

    return currentCount

# Current fish count
# Position 0 to 8 corresponds to the internal timer digit
# The number at each position corresponds to the number of fish with each timer digit
currentCount = [0] * 9

# Initial count
for timer in initialState:
    currentCount[int(timer)] += 1

# For i days
days = 256

# Update current count for every day in range
for i in range(1,days+1):
    currentCount = fishCount(currentCount,i)

# Solution
print('Number of lanternfish after ' + str(days) + ' days: ' + str(sum(currentCount)))
