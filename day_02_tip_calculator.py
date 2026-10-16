"""
Day 2 Project: Tip Calculator

Background:
    You are out for dinner with friends and want to split the bill fairly,
    tip included. The program asks for the total bill, the tip percentage
    (10, 12 or 15) and the number of people, then prints what each person
    should pay, rounded to 2 decimal places.

Concepts practised:
    Data types and type conversion (int/float/str), arithmetic operators,
    round(), f-strings.
"""

print("Welcome to the tip calculator.")
total_bill = input("What was the total bill?\n$")
tip = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
bill_split = input("How many people to split the bill?\n")
total_pay = round(float(total_bill) * float(1 + tip / 100) / float(bill_split), 2)
print(f"Each person should pay: ${total_pay}")
