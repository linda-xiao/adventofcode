# DAY 10: Part 1

input = open('2021/10/input.txt').read().split('\n')

# Remove the last (empty) element in the list
input.pop()

# List of illegal character
firstIllegalCharacter = []

# Bracket types
openBrackets = ['(', '[', '{', '<']
closeBrackets = [')', ']', '}', '>']

for line in input:

    # Temporary list for storing all checked open brackets
    tempList = []

    for i in range(0,len(line)):

        # Open brackets
        if line[i] in openBrackets:
            tempList.append(line[i])

        # Close brackets
        else:

            # ()
            if line[i] == closeBrackets[0]:

                # Check last appended element in temp list
                if tempList[-1] == openBrackets[0]:

                    # If it matches, delete the element from temp list
                    tempList.pop()

                # Corrupted if it doesn't match, append to illegal character and break
                else:
                    firstIllegalCharacter.append(line[i])
                    break

            # []
            elif line[i] == closeBrackets[1]:
                if tempList[-1] == openBrackets[1]:
                    tempList.pop()

                else:
                    firstIllegalCharacter.append(line[i])
                    break

            # {}
            elif line[i] == closeBrackets[2]:
                if tempList[-1] == openBrackets[2]:
                    tempList.pop()

                else:
                    firstIllegalCharacter.append(line[i])
                    break

            # <>
            elif line[i] == closeBrackets[3]:
                if tempList[-1] == openBrackets[3]:
                    tempList.pop()

                else:
                    firstIllegalCharacter.append(line[i])
                    break

# Score
score = 0

for i in firstIllegalCharacter:

    # ()
    if i == closeBrackets[0]:
        score += 3

    # []
    elif i == closeBrackets[1]:
        score += 57

    # {}
    elif i == closeBrackets[2]:
        score += 1197

    # <>
    elif i == closeBrackets[3]:
        score += 25137

# Solution
print('Total syntax error score: ' + str(score))
