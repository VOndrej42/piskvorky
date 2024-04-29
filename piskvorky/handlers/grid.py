def print_grid(grid, rows, columns):
    result = ""
    
    for column in range(0,columns):
        result += str(column)
        result += "\n"
        # print(column, end=" ")
    # print()
    result += "\n"
    for row in range(0, rows):
        result += "\n"
        # print(row, end=" ")
        for column in range(0, columns):
            # print(grid[row][column], end=" ")
            result += grid[row][column]
            result += "\n"
        # print()
    return result



def create_grid(rows, columns, empty_sign="_"):
    grid = []
    for row in range(0, rows):
        temp_row = []
        for column in range(0, columns):
            temp_row.append(empty_sign)
        grid.append(temp_row) 
    return grid

grid = create_grid(3,3)
print(grid)