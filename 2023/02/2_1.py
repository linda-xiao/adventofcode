# DAY 2: Part 1

input = open('input.txt').read().split('\n')

# Counter for sum of game IDs that are valid
sum = 0

# For every game
for game in input:

    # Boolean for if the game is valid, initially set to true
    gameValid = True

    # Game ID
    gameID = input.index(game) + 1

    # Separate game ID and sets of cubes
    sets = game.split(': ')[1].split('; ')

    # For every set
    for set in sets:

        # If the game is valid
        if gameValid:

            # Separate each colour
            setList = set.split(', ')

            # For every colour in list of sets
            for colour in setList:

                # For the colour red
                if colour.split()[1] == 'red':

                    # Check if the number of cubes is less than or equal to 12
                    if int(colour.split()[0]) <= 12:

                        # If true, continue to next colour
                        continue

                    # Else, the game is invalid, break the loop and continue to the next game
                    else:
                        gameValid = False
                        break

                # For the colour green
                elif colour.split()[1] == 'green':

                    # Check if the number of cubes is less than or equal to 13
                    if int(colour.split()[0]) <= 13:
                        continue

                    # Else, the game is invalid, break the loop and continue to the next game
                    else:
                        gameValid = False
                        break

                # For the colour blue
                elif colour.split()[1] == 'blue':

                    # Check if the number of cubes is less than or equal to 14
                    if int(colour.split()[0]) <= 14:
                        continue

                    # Else, the game is invalid, break the loop and continue to the next game
                    else:
                        gameValid = False
                        break

    # Add game ID to the sum for all valid games
    if gameValid:
        sum += gameID

# Solution
print('Sum of the game IDs that are valid: ' + str(sum))