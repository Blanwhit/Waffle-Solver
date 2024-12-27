import mapping
import generate_string_grid
import find_swaps


def visualize_grid(starting_grid: dict, final_grid: dict) -> None:
    print("\n")

    # Create default grid object to modify
    grid_vis = mapping.default_grid
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
