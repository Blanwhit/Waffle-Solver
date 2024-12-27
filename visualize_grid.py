import mapping
import generate_string_grid
import find_swaps


def visualize_grid(starting_grid: dict, final_grid: tuple[tuple[str]]) -> None:
    print("\n")

    # Create default grid object to modify
    grid_vis = {
        "0-5": {"type": "", "letter": "."},
        "0-6": {"type": "", "letter": "."},
        "0-7": {"type": "", "letter": "."},
        "0-8": {"type": "", "letter": "."},
        "0-9": {"type": "", "letter": "."},
        "1-5": {"type": "", "letter": "."},
        "1-6": "BLANK",
        "1-7": {"type": "", "letter": "."},
        "1-8": "BLANK",
        "1-9": {"type": "", "letter": "."},
        "2-5": {"type": "", "letter": "."},
        "2-6": {"type": "", "letter": "."},
        "2-7": {"type": "", "letter": "."},
        "2-8": {"type": "", "letter": "."},
        "2-9": {"type": "", "letter": "."},
        "3-5": {"type": "", "letter": "."},
        "3-6": "BLANK",
        "3-7": {"type": "", "letter": "."},
        "3-8": "BLANK",
        "3-9": {"type": "", "letter": "."},
        "4-5": {"type": "", "letter": "."},
        "4-6": {"type": "", "letter": "."},
        "4-7": {"type": "", "letter": "."},
        "4-8": {"type": "", "letter": "."},
        "4-9": {"type": "", "letter": "."},
    }

    for i in grid_vis.keys():
        # Avoid blank letters
        if grid_vis[i] != "BLANK":
            # Update grid dictionary to match grid solution tuple
            grid_vis[i]["letter"] = final_grid[mapping.grid_mapping[i][0]][
                mapping.grid_mapping[i][1]
            ][mapping.grid_mapping[i][2]]

    # Visualise solved grid
    print(generate_string_grid.generate_string_grid(grid_vis))
    print("\n")
    swaps = find_swaps.find_min_grid_swaps(starting_grid, grid_vis)
    print(f"Total swaps: {len(swaps)}\n{swaps}")
    print("\n-------------------")
