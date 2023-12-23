import mapping


# Check all full grids to see if green letters match
def check_good_grids(checking_grid, fn_good_grids):
    print("Checking full grids against green letters...")
    fn_complete_grids = fn_good_grids.copy()
    for fn_good_grid in fn_good_grids:
        for i in checking_grid.keys():
            # Make sure the spot is not blank
            if checking_grid[i] != "BLANK":
                # If the cell is green, check if its place on the grid matches its place in the generated solution
                if checking_grid[i]["type"] == "g":
                    if (
                        checking_grid[i]["letter"]
                        != fn_good_grid[mapping.grid_mapping[i][0]][
                            mapping.grid_mapping[i][1]
                        ][mapping.grid_mapping[i][2]]
                    ):
                        fn_complete_grids.remove(fn_good_grid)
                        break

    print(
        f"{len(fn_good_grids)} Grids checked, {len(fn_complete_grids)} grids match all green letters"
    )
    return fn_complete_grids
