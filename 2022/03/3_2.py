# DAY 3 PART 1

input = open('2022/03/input.txt').read().split('\n')
input.pop()     # Remove the last (empty) element in the list

# Find the common item in the three rucksacks
def findCommonItem(first, second, third):

    # For each item in the first rucksack
    for item in first:

        # If the item is in the second and the third rucksack
        if item in second and item in third:
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

# For every third rucksack
for rucksack in input[0:len(input):3]:
    first = rucksack
    second = input[input.index(rucksack)+1]     # Index of the current rucksack + 1 (1 after the current one)
    third = input[input.index(rucksack)+2]      # Index of the current rucksack + 2 (2 after the current one)

    # Find the common item in the three rucksacks
    commonItem = findCommonItem(first, second, third)

    # Find the priority of the common item
    priority = findPriority(commonItem)

    # Add the priority to the sum of priorities
    prioritySum = prioritySum + priority

# Solution
print('Sum of priorities: ' + str(prioritySum))
