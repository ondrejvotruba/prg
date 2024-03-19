import json
with open("grid.json", "r") as file:    
    grid = json.load(file)
def print_grid(grid):    
    for row in grid:        
        print(row)
def get_value_from_grid(grid, x, y):    
    return grid[y][x]
def set_value_to_grid(grid, x, y, value):    
    grid[y][x] = value
    print_grid(grid)