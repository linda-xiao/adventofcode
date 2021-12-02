# DAY 1: Task 1

input = open('2021/1/input.txt').read().split('\n')

# Remove the last (empty) element in the list
input.pop()

# Increase counter
incr = 0

# For every depth ranging from the second to the last
for depth in range(1,len(input)):

    # If the current depth is larger than the previous
    if int(input[depth]) > int(input[depth-1]):

        # Add one increase to the counter
        incr += 1

# Number of increases
print(incr)
