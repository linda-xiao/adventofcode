# DAY 8: Part 1

input = open('2021/8/input.txt').read().split('\n')

# Remove the last (empty) element in the list
input.pop()

# Output count (for digits 1, 4, 7, 8)
count = 0

# For every line
for line in input:

    # Extract the output values (after the delimiter) and split into separate elements
    output = line.split(' | ')[1].split(' ')

    # For every output value
    for combination in output:

        # Unique number of segments
        # 2 segments (digit 1)
        if len(combination) == 2:
            count += 1

        # 4 segments (digit 4)
        elif len(combination) == 4:
            count += 1

        # 3 segments (digit 7)
        elif len(combination) == 3:
            count += 1

        # 7 segments (digit 8)
        elif len(combination) == 7:
            count += 1

        # Non unique number of segments (other digits)
        else:
            continue

# Solution
print('Number of times digits 1, 4, 7 or 8 appear in output values: ' + str(count))
