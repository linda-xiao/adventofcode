# DAY 1: Task 1

input = open('2019/1/input.txt').read().split('\n')
import math

# Remove the last (empty) element in the list
input.pop()

# Start at total fuel 0
fueltot = 0

# Calculate required fuel for every mass
for mass in input:

    # Convert from string to integer
    mass = int(mass)

    # Divide by three, round down and subtract 2
    fuel = int(math.floor(mass/3) - 2)

    # Add required fuel for each mass to the total fuel
    fueltot += fuel

print(int(fueltot))
