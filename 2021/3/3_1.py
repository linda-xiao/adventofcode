# DAY 3: Part 1

input = open('2021/3/input.txt').read().split('\n')

# Remove the last (empty) element in the list
input.pop()

# List of gamma and epsilon rate
gammaRate = []
epsilonRate = []

for bitPosition in range(0,len(input[0])):

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

    # If 0 is the most common bit
    if zeros > ones:

        # Append 0 to the gamma rate and 1 to the epsilon rate
        gammaRate.append('0')
        epsilonRate.append('1')

    # If 1 is the most common bit
    else:

        # Append 1 to the gamma rate and 0 to the epsilon rate
        gammaRate.append('1')
        epsilonRate.append('0')

# Convert from list to strings
gammaBinary = ''.join(gammaRate)
epsilonBinary = ''.join(epsilonRate)

# Convert from binary to decimal
gammaDec = int(gammaBinary,2)
epsilonDec = int(epsilonBinary,2)

# Solution
print('Gamma rate: ' + str(gammaDec))
print('Epsilon rate: ' + str(epsilonDec))
print('Power consumption: ' + str(gammaDec * epsilonDec))
