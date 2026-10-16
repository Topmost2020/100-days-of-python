"""
Day 1 Project: Band Name Generator

Background:
    A first taste of Python input and output. The program greets the user,
    asks for the city they grew up in and the name of their first pet, then
    combines the two into a band name (e.g. "Lagos Bella").

Concepts practised:
    print(), input(), variables, string formatting (str.format).
"""

print("Welcome to the Band Name Generator.")
city = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be {} {}".format(city, pet))
