# DAY 2: Part 1

input = open('2021/2/input.txt').read().split('\n')

# Remove the last (empty) element in the list
input.pop()

# Position and depth counter
position = 0
depth = 0

# For every line
for command in input:

    # Split each line in command and digit
    command = command.split()

    # Forward
    if command[0] == 'forward':

        # Add the digit to position counter
        position += int(command[1])

    # Up
    elif command[0] == 'up':

        # Subtract the digit from depth counter
        depth -= int(command[1])

    # Down
    elif command[0] == 'down':

        # Add the digit to depth counter
        depth += int(command[1])

# Solution
print('Final horizontal position: ' + str(position))
print('Final depth: ' + str(depth))
print('Final horizontal position * final depth = ' + str(position * depth))
