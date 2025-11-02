# ------------------------------------------------------------------------------------------
# CS50 Python
# Week 0
# Problem set 0
# ---------------------------------------------------
# Problem 4 : EINSTEIN
# Description: This program prompts the user to enter a mass (in kilograms)
#              and calculates the equivalent energy (in Joules) using
#              Einstein's formula:
#                             E = m * c^2
#              where:
#              E = energy in Joules
#              m = mass in kilograms (user input)
#              c = speed of light, approximately 300,000,000 m/s
#             The program assumes the user inputs an integer value for mass
#             and outputs the resulting energy as an integer.
#---------------------------------------------------------------------------------------------

# Prompt the input from user for mass (in Kg)
mass = int(input("m : "))
c = 300000000 # Define constant for speed of light (in meter per second)
# Calculate energy using the formula E = m * c^2
energy = mass * (c**2)
# Print the results
print("E :",energy)


