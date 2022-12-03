# DAY 1: Part 1

input = open('2022/01/input.txt').read().split('\n')

# Temporary list for storing calories of one elf
temp = []

# List storing the calories of each elf
listElves = []

# For every item
for i in input:

    # If the item is not empty
    if i != '':
        i = int(i)               # Convert string to integer
        temp.append(i)           # Add to temporary list

    # When an empty item '' is reached
    else:
        listElves.append(temp)   # Add the temporary list to the list of elves
        temp = []                # Reset temporary list

# List storing the total calories of each elf
totalCalories = []

# For every elf
for elf in listElves:
    calorieCount = 0                        # Set the counter to 0

    # For every food
    for i in elf:
        calorieCount = calorieCount + i     # Add the calories to the counter

    totalCalories.append(calorieCount)      # Add the total of calories to the list

# Solution
print('Total calories: ' + str(max(totalCalories)))
