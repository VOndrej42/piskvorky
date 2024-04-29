from handlers.grid import create_grid, print_grid
from handlers.input import get_input

rows = 3
colums = 3
grid = create_grid(rows, colums)
empty_place = rows*colums

player_dict = {
    0: "x",
    1: "o"
}

for round_id in range(0, 6):
    print(f"Round number is {round_id}")

    for player in range(0, 2):
        print(f"Player {player} turn")
        print_grid(grid, rows, colums)

        print("Enter the X cordinate")
        x = get_input()
        
        print("Enter the Y cordinate")
        y = get_input()
        
        grid[x][y] = player_dict[player]