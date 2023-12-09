# DAY 2: Part 2

input = open('input.txt').read().split('\n')

# Counter for sum of the power of the minimum sets of cubes
sum = 0

# For every game
for game in input:

    # Separate game ID and sets of cubes
    sets = game.split(': ')[1].split('; ')

    # Temporary list of numbers of each colour
    numRed = []
    numGreen = []
    numBlue = []

    # For every set
    for set in sets:

        # Separate each colour
        setList = set.split(', ')

        # For every colour
        for colour in setList:

            # For the colour red
            if colour.split()[1] == 'red':

                # Append number to red list
                numRed.append(int(colour.split()[0]))

            # For the colour green
            elif colour.split()[1] == 'green':

                # Append number to green list
                numGreen.append(int(colour.split()[0]))

            # For the colour blue
            elif colour.split()[1] == 'blue':

                # Append number to blue list
                numBlue.append(int(colour.split()[0]))

    # Power of the fewest number of cubes of each colour
    power = max(numRed) * max(numGreen) * max(numBlue)

    # Add to the sum of the power of the minimum sets of cubes
    sum += power

# Solution
print('Sum of the power of the minimum sets of cubes: ' + str(sum))