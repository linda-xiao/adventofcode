# DAY 4: Part 1

input = open('input.txt').read().split('\n')

# Function that checks if my numbers are winning numbers
def checkWinningNumber(winningNumber, myNumbers, counter):

    # For every number of my numbers
    for i in myNumbers:

        # If the number is the same as the current winning number
        if i == winningNumber:

            # Add one to the counter of matching numbers
            counter += 1

    return counter

# Sum of the total points
sum = 0

# For every card
for card in input:

    # Separate the card number and the numbers with the vertical bar
    numbers = card.split(': ').pop(1).split(' | ')

    winningNumbers = numbers[0].split()
    myNumbers = numbers[1].split()

    # Counter of matching numbers
    counter = 0

    # For every winning number
    for num in winningNumbers:

        # Call the function that checks if the current winning number is in my numbers
        counter = checkWinningNumber(num, myNumbers, counter)

    # Calculation of points for all cards that have winning numbers
    if counter > 0:
        sum += pow(2,counter-1)

# Solution
print('Total sum of points:', sum)