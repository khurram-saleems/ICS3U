# 03 Practice Programs 1
# Multiplication Practice
#
# Khurram Shaikh
# Saturday, September 14, 2022
#
# This program serves as practice with the multiplication
# arithmetic operator in Python.

import math

# Displays the area of a circle with a radius of 10 meters
radius=10
area=math.pi*10**2
print("Circumference of Circle with a Radius of {} is {} Meters Squared.\n".format(radius,area))

# Displays annual interest payable on a loan of $5365.25 at 12.5% 
loan,interest_rte=5365.25,0.125
annualInterest_payable= interest_rte*loan
print("Annual Interest Payable on a loan of ${} at {:.1%} is ${:.2f}.\n".format(loan,interest_rte,annualInterest_payable))

# Displays the sales tax payable at 7% on a purchase of $12.50
purchase_amnt,tax_rte=12.5,0.07
salesTax_payable=tax_rte*purchase_amnt
print("Sales Tax Payable at {:.1%} on a Purchase of {} is ${:.2f}.".format(tax_rte,purchase_amnt,salesTax_payable))
total=purchase_amnt+salesTax_payable
print("Total is: ${:.2f}.".format(total))

