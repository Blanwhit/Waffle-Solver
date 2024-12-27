# Imports
import os
import get_acceptable_triples
import check_good_grids
import get_good_grids
import generate_string_grid
import mapping
import visualize_grid

grid = mapping.default_grid.copy()  # Set default grid

IS_TESTING = False  # True to use pre-made grid from testing.py, False to ask the user to fill the grid


# Get words from words.txt
words_raw = open("words.txt", "r")
words = words_raw.readlines()
for i in range(len(words)):
    words[i] = words[i][0:5]


if IS_TESTING:  # Solve pre-made grid
    import testing

    starting_grid = testing.test_grids[2]

    # Solve
    (
        good_triples_horizontal,
        good_triples_vertical,
        good_letters,
        good_words,
    ) = get_acceptable_triples.get_acceptable_triples(starting_grid, words)

    good_grids = get_good_grids.get_good_grids(
        good_triples_horizontal, good_triples_vertical, good_letters, good_words
    )

    solution_grids = check_good_grids.check_good_grids(starting_grid, good_grids)

    # Visualise solved grids
    for solution_grid in solution_grids:
        visualize_grid.visualize_grid(starting_grid, solution_grid)


else:  # Solve grid made by user
    # Get grid from user
    for i in grid.keys():
        # Clear terminal and print grid
        if grid[i] == "BLANK":
            continue
        os.system("cls||clear")
        grid[i]["letter"] = "■"
        print(generate_string_grid.generate_string_grid(grid))

        # Ask the user for a letter
        letter = ""
        while letter not in [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]:
            letter = input(f"Please input a letter in cell {i}: ").lower()

        # Ask the user for the type of the letter
        type_letter = ""
        while type_letter != "g" and type_letter != "w" and type_letter != "y":
            type_letter = input(
                "Please enter the type of that cell (G/g for green, Y/y for yellow, W/w for white): "
            ).lower()
        grid[i]["type"] = type_letter
        grid[i]["letter"] = letter

    # Clear terminal and print final grid
    os.system("cls||clear")
    print(generate_string_grid.generate_string_grid(grid))
    print("Solving...")

    starting_grid = grid.copy()

    # Solve
    (
        good_triples_horizontal,
        good_triples_vertical,
        good_letters,
        good_words,
    ) = get_acceptable_triples.get_acceptable_triples(starting_grid, words)

    good_grids = get_good_grids.get_good_grids(
        good_triples_horizontal, good_triples_vertical, good_letters, good_words
    )

    solution_grids = check_good_grids.check_good_grids(starting_grid, good_grids)

    # Visualise solved grids
    for solution_grid in solution_grids:
        visualize_grid.visualize_grid(starting_grid, solution_grid)
