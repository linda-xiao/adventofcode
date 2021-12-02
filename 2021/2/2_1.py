# DAY 2: Task 1

input = open('2021/2/input.txt').read().split('\n')

# Remove the last (empty) element in the list
input.pop()

# Position and depth counter
position = 0
depth = 0

# For every command
for command in input:

    # Forward (if the letter at the first position is 'f')
    if command[0] == 'f':

        # Add the digit at the last position to position counter
        position += int(command[-1])

    # Up (if the letter at the first position is 'u')
    elif command[0] == 'u':

        # Subtract the digit at the last position to depth counter
        depth -= int(command[-1])

    # Down (if the letter at the first position is 'd')
    elif command[0] == 'd':

        # Add the digit at the last position to depth counter
        depth += int(command[-1])

# Multiply final horizontal position by final depth
print(position * depth)
