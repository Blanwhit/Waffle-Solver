# Generate a grid string from a grid dictionary for visualization purposes
def generate_string_grid(raw_grid: dict):
    # Header
    grid_string = "   5  6  7  8  9"
    for i in raw_grid.keys():
        # Skip blank cells
        if raw_grid[i] == "BLANK":
            grid_string += "   "

        # First column
        elif str(i)[2] == "5":
            grid_string += f"\n{str(i)[0]}  {raw_grid[i]['letter'].upper()}"

        # All other cells
        else:
            grid_string += f"  {raw_grid[i]['letter'].upper()}"

    return grid_string
