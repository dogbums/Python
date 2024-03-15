def prepare_card_grid():
    return [["J", "J", "J", "J"],
            ["Q", "Q", "Q", "Q"],
            ["K", "K", "K", "K"],
            ["A", "A", "A", "A"]]


def prepare_display_grid():
    return [["*", "*", "*", "*"],
            ["*", "*", "*", "*"],
            ["*", "*", "*", "*"],
            ["*", "*", "*", "*"]]


def print_display_grid():
    print("  1 2 3 4")
    for x in range(4):
        print(str(x + 1) + " ", end='')
        for y in range(4):
            print(display_grid[x][y] + " ", end='')
        print()


def input_card_coordinates(prompt):
    print(prompt, end='')
    x = int(input('> '))
    y = int(input('> '))
    return x, y


def invalid_coordinates(x, y):
    return x < 1 or x > 4 or y < 1 or y > 4 or display_grid[x-1][y-1] == 'X'


# prepare counters
number_of_guesses = 0
number_of_pairs_found = 0

card_grid = prepare_card_grid()
display_grid = prepare_display_grid()

print_display_grid()

# while not all pairs identified do
while number_of_pairs_found < 8:
    number_of_guesses += 1

    x1, y1 = input_card_coordinates("Enter co-ordinates of your first choice (x, y) ")

    while invalid_coordinates(x1, y1):
        x1, y1 = input_card_coordinates("Not a correct choice, please try again." +
                                        "\nEnter co-ordinates of your first choice (x, y) ")

    x1 -= 1
    y1 -= 1
    display_grid[x1][y1] = card_grid[x1][y1]

    print_display_grid()

    x2, y2 = input_card_coordinates("Enter co-ordinates of your second choice (x, y) ")

    while invalid_coordinates(x2, y2):
        x2, y2 = input_card_coordinates("Not a correct choice, please try again." +
                                        "\nEnter co-ordinates of your second choice (x, y) ")

    x2 -= 1
    y2 -= 1
    display_grid[x2][y2] = card_grid[x2][y2]

    print_display_grid()

    # check the user's selection
    if card_grid[x1][y1] == card_grid[x2][y2]:
        display_grid[x1][y1] = 'X'
        display_grid[x2][y2] = 'X'
        number_of_pairs_found += 1
        print("Congratulations, you have now found", number_of_pairs_found, "pairs")
    else:
        display_grid[x1][y1] = '*'
        display_grid[x2][y2] = '*'
        print("Hard luck! Try again")

    print_display_grid()


# display number of guesses needed to complete the grid
print("You took", number_of_guesses, "guesses to find all the pairs")
