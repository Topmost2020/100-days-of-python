"""
Day 3 Project: Escape the Alien Spaceship (text adventure)

Background:
    The course project is "Treasure Island"; this is my own version with a
    sci-fi theme. You are trapped on an alien spaceship and must make the
    right choices (corridor, laser room, escape pod, destination) to get home
    safely. One wrong answer and it's game over.

Concepts practised:
    Conditional statements (if / elif / else), nested conditions,
    comparison operators, string methods (.lower()).
"""

print("Mission: Escape the Alien Spaceship 👽 🚀")
print("Welcome aboard the Alien Spaceship! Your mission is to escape before the aliens discover you.\nFind the escape pod and return safely to Earth!\n")
direction = input("Which corridor would you like to take? Left or Right?\n").lower()
if direction == 'left':
    print("\nYou are safe! No Alien is here! Continue\n")
    choice = int(input("How will you cross the laser room?\nOption 1: Jump over the lasers.\nOption 2: Crawl under the lasers.\nType 1 or 2.\n"))
    if choice == 1:
        print("\nYou triggered the alarm. Game Over!")
    elif choice == 2:
        print("\nYou are almost home!")
        escape = input("Which escape pod will you like to open? Red or Blue or Green?\n").lower()
        if escape == "green":
            print("\nThank Goodness! The engines started successfully. Continue\n")
            location = input("Where will you go from here?\nMars or Earth?\n").lower()
            if location == "earth":
                print("\nYayyy! You returned home safely.\nYou Win!🎉")
            elif location == "mars":
                print("\nYou get lost in space. Game Over!")
            else:
                print("\nPlease choose the right option. Game Over")
        elif escape == "blue":
            print("\nThe navigation system malfunctioned. Game Over!")
        elif escape == "red":
            print("\nThe engine failed. Game Over!")
        else:
            print("\nPlease choose the right option. Game Over")
elif direction == 'right':
    print("\nYou encountered an alien guard.\nGame Over!")
else:
    print("\nPlease choose the right option. Game Over")
