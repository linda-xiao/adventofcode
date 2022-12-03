# DAY 2 PART 2

input = open('2022/02/input.txt').read().split('\n')
input.pop()             # Remove the last (empty) element in the list

# Rock function (input round case and score)
def rock(i, score):

    # Rock
    if i[2] == 'X':     # For a loss, choose scissors
        score += 3      # +3 for scissors, +0 for loss

    # Paper
    elif i[2] == 'Y':   # For a draw, choose rock
        score += 4      # +1 for rock, +3 for draw

    # Scissors
    elif i[2] == 'Z':   # For a win, choose paper
        score += 8      # +2 for paper, +6 for win

    return score

# Paper function
def paper(i, score):

    # Rock
    if i[2] == 'X':     # For a loss, choose rock
        score += 1      # +1 for rock, +0 for loss

    # Paper
    elif i[2] == 'Y':   # For a draw, choose paper
        score += 5      # +2 for paper, +3 for draw

    # Scissors
    elif i[2] == 'Z':   # For a win, choose scissors
        score += 9      # +3 for scissors, +6 for win

    return score

# Scissors function
def scissors(i, score):

    # Rock
    if i[2] == 'X':     # For a loss, choose paper
        score += 2      # +2 for paper, +0 for loss

    # Paper
    elif i[2] == 'Y':   # For a draw, choose scissors
        score += 6      # +3 for scissors, +3 for draw

    # Scissors
    elif i[2] == 'Z':   # For a win, choose rock
        score += 7      # +1 for rock, +6 for win

    return score

# Counter
scoreCount = 0

# For each round
for round in input:

    # If the opponent chooses rock
    if round[0] == 'A':
        scoreCount = rock(round, scoreCount)

    # If the opponent chooses paper
    elif round[0] == 'B':
        scoreCount = paper(round, scoreCount)

    # If the opponent chooses scissors
    elif round[0] == 'C':
        scoreCount = scissors(round, scoreCount)

# Solution
print('Total score: ' + str(scoreCount))
