# DAY 4: Task 1

input = open('2021/4/input.txt').read().split('\n')

# Remove all empty lines in input
input = filter(None,input)

# Drawn numbers
drawnNumbersList = input[0]
drawnNumbers = drawnNumbersList.split(',')

# Boards
boards = []
for i in range(1,len(input),5):
    boards.append([input[i], input[i+1], input[i+2], input[i+3], input[i+4]])

# List of boards with each board in an array with each lines in an array
bingoBoards = []
for board in boards:
    bingoLines = []

    for line in board:

        # Filter out empty elements
        numbers = filter(None, line.split(' '))
        bingoLines.append(numbers)
    bingoBoards.append(bingoLines)

# Function that updates the board with an X for each drawn number
def checkNumber(number,board):
    newBoard = []

    for line in board:
        newLine = []

        for val in line:

            # If the current number is the drawn number, append X
            if val == number:
                newLine.append('X')

            # Else, append the current number
            else:
                newLine.append(val)

        newBoard.append(newLine)

    return newBoard

# Function for row bingo
def rowBingo(board):

    for line in board:

        # x counter in each row
        xRowCount = 0

        for n in line:

            # Add 1 to counter if there is an X
            if n == 'X':
                xRowCount += 1

            # If there are five X - bingo! Return true
            if xRowCount == 5:
                return True

    # If no bingo, return false
    return False

# Function for column bingo
def colBingo(board):

    # Transpose the board to get the columns as rows
    zipRow = zip(*board)
    transBoard = [list(row) for row in zipRow]

    # Run the rowBingo function for the transposed board
    return rowBingo(transBoard)

# Function that calculates the score of the winning board
def score(board,number):

    # Sum of all unmarked numbers
    sum = 0

    for line in board:
        for n in line:

            # If the current number is unmarked, add the number to the sum
            if n != 'X':
                sum += int(n)

    # Final score (sum of all unmarked numbers * the number that was just drawn)
    return sum * int(number)

# For each drawn number
for number in drawnNumbers:

    # Update board with X
    for i, board in enumerate(bingoBoards):
        bingoBoards[i] = checkNumber(number,board)

        # If row or column bingo, print final score and break
        if (rowBingo(bingoBoards[i]) or colBingo(bingoBoards[i])):
            print(score(bingoBoards[i],number))

            break
        else:
            continue
        break
    else:
        continue
    break
