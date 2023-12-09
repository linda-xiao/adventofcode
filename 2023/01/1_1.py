# DAY 1: Part 1

input = open('input.txt').read().split('\n')

# Counter for sum of calibration values
sum = 0

# For every line
for line in input:

    # Temporary empty list
    list = []

    # For every character
    for char in line:

        # If the character is a digit
        if char.isnumeric():

            # Append digit to list
            list.append(char)

    # First digit
    first = list[0]

    # Last digit
    pos_last = len(list)-1
    last = list[pos_last]

    # Combining the first and last digit
    calVal = int(first + last)

    # Adding the calibration value to the sum
    sum += calVal

# Solution
print('Sum of all of the calibration values: ' + str(sum))