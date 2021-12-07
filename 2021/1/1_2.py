# DAY 1: Part 2

input = open('2021/1/input.txt').read().split('\n')

# Remove the last (empty) element in the list
input.pop()

# List of sums of threes
sumThree = []

# Increase counter
incr = 0

# For every depth ranging from the first to the third last
for depth in range(0,len(input)-2):

    # Append the sum of the current depth + the 2 next depths
    sumThree.append(int(input[depth]) + int(input[depth+1]) + int(input[depth+2]))

# For every sum ranging from the second to the last
for sum in range(1,len(sumThree)):

    # If the current sum is larger than the previous
    if int(sumThree[sum]) > int(sumThree[sum-1]):

        # Add one increase to the counter
        incr += 1

# Solution
print('Number of increases: ' + str(incr))
