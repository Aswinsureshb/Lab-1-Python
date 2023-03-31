PENNY_VALUE = 1
NICKEL_VALUE = 5
DIME_VALUE = 10
QUARTER_VALUE = 25
PENNIES_IN_DOLLAR = 100

penny = int(input("Enter the number of pennies: " ))
nickel = int(input("Enter the number of nickel: "))
dime = int(input("Enter the number of dimes: "))
quarter = int(input("Enter the number of quarters: "))

totalCent=(PENNY_VALUE * penny)+(NICKEL_VALUE * nickel)+(DIME_VALUE * dime)+(QUARTER_VALUE * quarter)

totalDollars = totalCent/PENNIES_IN_DOLLAR


if totalDollars > 1.0:
    print("Sorry, the amount you entered was more than one dollar.")
elif totalDollars < 1.0:
    print("Sorry, the amount you entered was less than one dollar.")
else:
    print("Congratulations!The amount you entered was exactly one dollar!You win the game!!")
