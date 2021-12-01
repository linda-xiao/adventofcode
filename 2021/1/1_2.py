# DAY 1: Task 2

input = open('2021/1/input.txt').read().split('\n')

# Remove the last (empty) element in the list
input.pop()

# List of sums of threes
sumThree = []

# List of increases
incr = []

# For every depth ranging from the first to the last-2
for depth in range(0,len(input)-2):

    # Append the sum of the current depth + the 2 next depths
    sumThree.append(int(input[depth]) + int(input[depth+1]) + int(input[depth+2]))

# For every sum ranging from the second to the last
for sum in range(1,len(sumThree)):

    # If the current sum is larger than the previous
    if int(sumThree[sum]) > int(sumThree[sum-1]):

        # Append to list of increases
        incr.append(sumThree[sum])

# Number of increases
print(len(incr))
