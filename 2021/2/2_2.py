# DAY 2: Task 2

input = open('2021/2/input.txt').read().split('\n')

# Remove the last (empty) element in the list
input.pop()

# Position, depth and aim counter
position = 0
depth = 0
aim = 0

# For every command
for command in input:

    # Forward
    if command[0] == 'f':

        # Add the digit at the last position to position counter
        position += int(command[-1])

        # Add the digit multiplied by the current aim
        depth += int(command[-1]) * aim

    # Up
    elif command[0] == 'u':

        # Subtract the digit at the last position to aim counter
        aim -= int(command[-1])

    # Down
    elif command[0] == 'd':

        # Add the digit at the last position to aim counter
        aim += int(command[-1])

# Multiply final horizontal position by final depth
print(position * depth)
