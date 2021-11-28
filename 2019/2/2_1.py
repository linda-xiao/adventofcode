# DAY 2: Task 1

input = open('2/input.txt').read().split(',')

# Start at position 0 in list
pos = 0

# Check opcode for every fourth element
for i in input[0:len(input):4]:

    # Convert from string to integer
    i = int(i)

    # Position of inputs to opcode
    pos1 = int(input[pos+1])
    pos2 = int(input[pos+2])
    pos3 = int(input[pos+3])

    # Opcode 1 (addition)
    if i == 1:

        # Add the values at the positions of pos1 and pos2
        newVal = int(input[pos1]) + int(input[pos2])

        # Replace the value at the position of pos3 with the added values
        input[int(pos3)] = newVal

    # Opcode 2 (multiplication)
    elif i == 2:

        # Multiply the values at the positions of pos1 and pos2
        newVal = int(input[pos1]) * int(input[pos2])

        # Replace the value at the position of pos3 with the multiplied values
        input[int(pos3)] = newVal

    # Opcode 99 (finish the program)
    elif i == 99:
        continue

    # Step 4 positions
    pos += 4

print(input[0])
