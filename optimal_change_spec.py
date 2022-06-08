from optimal_change import optimal_change

print(optimal_change(75.75, 100) == "The optimal change for an item that costs $75.75 with an amount paid of $100 is 1 $20 bill, 4 $1 bills, and 1 quarter.")
print(optimal_change(56.82, 60) == "The optimal change for an item that costs $56.82 with an amount paid of $60 is 3 $1 bills, 1 dime, 1 nickel, and 3 pennies")
print(optimal_change(3.52, 10) == "The optimal change for an item that costs $3.52 with an amount paid of $10 is 1 $5 bill, 1 $1 bill, 4 dimes, 1 nickel, and 3 pennies.")
print(optimal_change(26.97, 30) == "The optimal change for an item that costs $26.97 with an amount paid of $30 is 3 $1 bills, and 3 pennies.")
print(optimal_change(.5, 3) == "The optimal change for an item that costs $0.5 with an amount paid of $3 is 2 $1 bills, and 2 quarters.")
print(optimal_change(10, 5) == "No change!")
print(optimal_change(.01, .01) == "No change!")