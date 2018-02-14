import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Rolling the dice...")
    print("The values are....")
    num1 = random.randint(min, max)
    num2 = random.randint(min, max)
    total = num1 + num2

    print(num1, "&", num2, "=", str(total))
    roll_again = input("Roll again?: ")
    print()
