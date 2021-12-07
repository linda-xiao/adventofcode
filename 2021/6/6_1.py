# DAY 6: Part 1

input = open('2021/6/input.txt').read()

# Split into separate internal timers
initialState = input.split(',')

# Strip newline from last element
initialState[-1] = initialState[-1].strip('\n')

# Function that updates the current state
def internalTimer(currentState,i):

    # Temporary list
    listTemp = []

    for timer in currentState:
        timer = int(timer)

        # If timer is between 1 and 8, subtract 1 and append to list
        if 1 <= timer <= 8:
            timer -= 1
            listTemp.append(timer)

        # If timer is 0
        elif timer == 0:

            # Reset internal timer (set to 6)
            listTemp.append(6)

            # Add new fish starting with internal timer 8
            listTemp.append(8)

    # Update current state by setting as temporary list
    currentState = listTemp

    return currentState

# Initial state
currentState = initialState

# For i days
days = 80

# Update current state for every day in range
for i in range(1,days+1):
    currentState = internalTimer(currentState,i)

# Solution
print('Number of lanternfish after ' + str(days) + ' days: ' + str(len(currentState)))
