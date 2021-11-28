# DAY 1

# Task 1
input = open('1/input.txt').read().split('\n')
input.pop()
import math

fueltot = 0

for mass in input:
    mass = int(mass)
    fuel = math.floor(mass/3) - 2
    fueltot += fuel

print(int(fueltot))

# Task 2
