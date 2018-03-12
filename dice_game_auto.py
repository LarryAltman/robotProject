import random


def dice_game():
    min = 1
    max = 6
    roll_again = True
    print("Roll 3 even or odd numbers in a row to win!")

    # Loop until win condition is satisfied.
    while roll_again is True:
        foo_list = []
        results = []
        counter = 0

        # Randomly choose the 3 integers between 1 and 6.
        while counter < 3:
            num1 = random.randint(min, max)
            num2 = random.randint(min, max)
            total = num1 + num2
            print(num1, "+", num2, "=", str(total))
            foo_list.append(total)
            counter += 1

        # Check each integer in the list and populate a new list
        # with the string 'even' or 'odd'.
        for i in foo_list:
            if i % 2 == 0:
                win_game = "Even"
                results.append(win_game)
            elif i % 2 != 0:
                win_game = "Odd"
                results.append(win_game)

        # Checks if all values are equal.
        if len(set(results)) == 1:
            print("You win!!!")
            roll_again = False
        elif len(set(results)) != 1:
            print("Not a winner, rolling again.\n")
            roll_again = True
        else:
            print("Error.")
