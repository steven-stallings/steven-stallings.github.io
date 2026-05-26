# Purpose: This program calculates the total income tax owed for a year.

# I started by prompting for required user input. I set income to float to accept all values. Elevation to integer
# since there would be no decimals.
annual_income = float(input("What was your total income for this year?: "))
marital_status = input("Are you married? [y/n]?: ")
marriage_length = float(input("How many years have you been married?: "))
elevation_status = int(input("What is the Sea Level of your home?: 1 - Below, 2 - At, 3 - Above : "))

# I defined my conditional statements based on the parameters in the assignment spec. I converted
# the percentages to decimals to simplify the math and reduce the amount of code needed.
# If annual income is less than 10000 than income tax = 2.3% of annual income
if annual_income < 10000:
    income_tax = annual_income * 0.023
# else if annual income is greater than or equal to 10000 but less than or equal to 50000 than income tax =
# 4.5% of annual income
elif annual_income >= 10000 and annual_income <= 50000:
    income_tax = annual_income * 0.045
# else if annual income is greater than 50000 than income tax = 6.1% of annual income
elif annual_income > 50000:
    income_tax = annual_income * 0.061

# I defined more conditional statements based on the assignment spec and user input.
# if elevation input = 1 than add 18.32 to income tax
if elevation_status == 1:
    income_tax += 18.32
# if elevation input = 2 than add 1.6% of annual income to income tax
if elevation_status == 2:
    income_tax += (0.016 * annual_income)
# if elevation status = 3, prompt user input for number of bedrooms then add (5 * number of bedrooms) to income tax.
if elevation_status == 3:
    total_bedrooms = float(input("How many bedrooms do you have?: "))
    income_tax += (5 * total_bedrooms)
# defined marital conditional statement.
# if marital status input prompt = y than subtract (1.62 * marriage length) from income tax. I did not see a reason to
# define "n" since there is no change when "n" is inputted.
if marital_status == "y":
    income_tax -= (1.62 * marriage_length)

# defined total tax as income tax so I could have a value to print in my output.
total_tax = income_tax
# printed the total tax.
print("Total Tax: ", income_tax)
