import os

class Game:

    def ziskej_souradnice(self):
        self.x = int(input("Zadej souřadnici 'x'"))
        self.y = int(input("Zadej souřadnici 'y'"))
        os.system('cls')
        return self.x, self.y
    
    def vyhodnot_hru(self, grid: list, symbol: str, rows: int, columns: int) -> bool:
        for row in range(rows):
            for i in range(rows - 2):
                if grid[row][i] == symbol and grid[row][i+1] == symbol and grid[row][i+2] == symbol:
                    return True

        for column in range(columns):
            for j in range(columns - 2):
                if grid[j][column] == symbol and grid[j+1][column] == symbol and grid[j+2][column] == symbol:
                    return True

        



