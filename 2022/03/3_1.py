# DAY 3: Part 1

input = open('2022/03/input.txt').read().split('\n')
input.pop()     # Remove the last (empty) element in the list

# Find the common item in the two compartments
def findCommonItem(firstCompartment, secondCompartment):

    # For each item in the first compartment
    for item in firstCompartment:

        # If the item is in the second compartment
        if item in secondCompartment:
            return item

# Find the priority of the common item
def findPriority(item):

    # A-Z (ord 65-90)
    if ord(item) in range(65,90+1):     # End value not included
        priority = ord(item) - 38       # A-Z -> 27-52

    # a-z (ord 97-122)
    else:
        priority = ord(item) - 96       # a-z -> 1-26

    return priority

# Sum of priorities
prioritySum = 0

# For each rucksack
for rucksack in input:

    # Divide the rucksack into two equally large compartments
    divideCompartment = int(len(rucksack)/2)
    firstCompartment = rucksack[0:divideCompartment]
    secondCompartment = rucksack[divideCompartment:len(rucksack)]

    # Find the common item in the compartments
    commonItem = findCommonItem(firstCompartment, secondCompartment)

    # Find the priority of the common item
    priority = findPriority(commonItem)

    # Add the priority to the sum of priorities
    prioritySum = prioritySum + priority

# Solution
print('Sum of priorities: ' + str(prioritySum))
