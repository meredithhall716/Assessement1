from optimal_change import optimal_change

print(optimal_change(75.75, 100) == "The optimal change for an item that costs $75.75 with an amount paid of $100 is 1 $20 bill, 4 $1 bills and 1 quarter.")
print(optimal_change(56.82, 60) == "The optimal change for an item that costs $56.82 with an amount paid of $60 is 2 $20 bills, 1 $10 bill, 1 $5 bill, 1 $1 bill, 3 quarters, 1 nickel and 2 pennies.")
print(optimal_change(3.50, 10) == "The optimal change for an item that costs $3.50 with an amount paid of $10 is 1 $5 bill, 1 $1 bill, and 2 quarters.")
print(optimal_change(26.90, 30) == "The optimal change for an item that costs $26.90 with an amount paid of $30 is 3 $1 bills and 1 dime.")
print(optimal_change(.5), 3) == "The optimal change for an item that costs $.5 with an amount paid of $3 is 2 $1 bills and 2 quarters."
print(optimal_change(10, 5) == "No change!")
print(optimal_change(.01, .01) == "The optimal change for an item that costs $.01 with an amount paid of $.01 is none.")
