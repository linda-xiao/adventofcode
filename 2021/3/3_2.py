# DAY 3: Part 2

input = open('2021/3/input.txt').read().split('\n')

# Remove the last (empty) element in the list
input.pop()

# Creates an updated list for oxygen generator rating
# with only the numbers containing the most common bit for each position
def newListOxygen(input,bitPosition):

    # List of new numbers
    newNumbersOxygen = []

    # Start counter for zeros and ones
    zeros = 0
    ones = 0

    for number in input:

        # If the digit at the current position is 0, add to the zeros counter
        if number[bitPosition] == '0':
            zeros += 1

        # If the digit at the current position is 1, add to the ones counter
        else:
            ones += 1

    for number in input:

        # If 0 is the most common bit
        if zeros > ones:

            # Append all numbers with 0 at the current position
            if number[bitPosition] == '0':
                newNumbersOxygen.append(number)

        # If 1 is the most common bit
        else:

            # Append all numbers with 1 at the current position
            if number[bitPosition] == '1':
                newNumbersOxygen.append(number)

    # Return the updated list of numbers
    return newNumbersOxygen

# Creates an updated list for CO2 scrubber rating
# with only the numbers containing the most common bit for each position
def newListCO2(input,bitPosition):

    newNumbersCO2 = []

    zeros = 0
    ones = 0

    for number in input:

        if number[bitPosition] == '0':
            zeros += 1
        else:
            ones += 1

    for number in input:
        if zeros > ones:

            if number[bitPosition] == '1':
                newNumbersCO2.append(number)

        else:
            if number[bitPosition] == '0':
                newNumbersCO2.append(number)

    return newNumbersCO2

# Initial input for oxygen generator rating and CO2 scrubber rating
oxygen = input
CO2 = input

for bitPosition in range(0,len(input[0])):

    # If the list contains more than one number
    if len(oxygen) > 1:

        # Update the list of numbers for oxygen generator rating
        oxygen = newListOxygen(oxygen,bitPosition)

    # If the list contains more than one number
    if len(CO2) > 1:

        # Update the list of numbers for CO2 scrubber rating
        CO2 = newListCO2(CO2,bitPosition)

# Convert from list to strings
oxygenBinary = ''.join(oxygen)
CO2Binary = ''.join(CO2)

# Convert from binary to decimal
oxygenDec = int(oxygenBinary,2)
CO2Dec = int(CO2Binary,2)

# Solution
print('Oxygen generator rating: ' + str(oxygenDec))
print('CO2 scrubber rating: ' + str(CO2Dec))
print('Life support rating: ' + str(oxygenDec * CO2Dec))
