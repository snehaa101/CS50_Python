# ------------------------------------------------------------------------------------------
# CS50 Python
# Week 0
# Problem set 0
# ---------------------------------------------------
# Problem 5 : TIP CALCULATOR
# Description: This program calculates the tip amount and total bill for a restaurant meal
#              based on user input for meal cost and desired tip percentage.
#---------------------------------------------------------------------------------------------

def main():

    # Prompt the user to enter the cost of the meal
    # input() returns a string, so we convert it to a float to allow decimal values
    dollars = dollars_to_float(input("How much was the meal? "))

    # Prompt the user to enter the tip percentage they want to leave
    # Convert it to a float so we can perform calculations
    percent = percent_to_float(input("What percentage would you like to tip? "))

    # Calculating the tip amount
    tip = dollars * percent

    # Display the tip amount formatted to 2 decimal places
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
                        # Convert a string representing dollars to a float.
                        # Example: "$50" -> 50.0

    d = d.replace('$','') # Removes the dollor sign
    return float(d)



def percent_to_float(p):
                        # Convert a string representing a percentage to a float.
                        # Example: "15%" -> 0.15

    p = p.replace('%','') # Removes the percentage sign
    p = float(p)/100 # Converts in percentage to decimal
    return (p)


# Calls the main function
main()
