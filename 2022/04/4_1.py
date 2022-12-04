# DAY 4: Part 1

input = open('2022/04/input.txt').read().split('\n')
input.pop()     # Remove the last (empty) element in the list

# Counter of full overlaps
fullOverlaps = 0

# For each pair of elves
for pair in input:

    # Split the pair into individual elves
    elves = pair.split(',')

    # Split the elves into their respective sections
    sectionsFirstElf = elves[0].split('-')
    sectionsSecondElf = elves[1].split('-')

    # If the first elf's start section is smaller than the second elf's
    # and if the first elf's end section is smaller than the second elf's
    if (int(sectionsFirstElf[0]) < int(sectionsSecondElf[0]) and int(sectionsFirstElf[1]) < int(sectionsSecondElf[1])):
        continue

    # If the second elf's start section is smaller than the first elf's
    # and if the second elf's end section is smaller than the first elf's
    elif (int(sectionsSecondElf[0]) < int(sectionsFirstElf[0]) and int(sectionsSecondElf[1]) < int(sectionsFirstElf[1])):
        continue

    # Else full overlap occurs, add to the counter
    else:
        fullOverlaps += 1

# Solution
print('Number of full overlaps: ' + str(fullOverlaps))
