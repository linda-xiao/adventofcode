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

    # Split each line in command and digit
    command = command.split()

    # Forward
    if command[0] == 'forward':

        # Add the digit to position counter
        position += int(command[1])

        # Add the digit multiplied by the current aim
        depth += int(command[1]) * aim

    # Up
    elif command[0] == 'up':

        # Subtract the digit from aim counter
        aim -= int(command[1])

    # Down
    elif command[0] == 'down':

        # Add the digit to aim counter
        aim += int(command[1])

# Multiply final horizontal position by final depth
print(position * depth)
