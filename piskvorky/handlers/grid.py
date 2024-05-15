class Grid:

    def __init__(self, rows: int = 5, columns: int = 5, empty_sign: str = "_"):
        """
        Vytvoří instanci herního pole - grid

        Args:
        rows (int): počet řádků hracího pole
        colums (int): počet sloupců hracího pole
        empty_sign (str): znak, reprezentující prázdnou buňku hracího pole

        Returns:
        None: pouze vytvoří hrací pole, o výpis se stará další funkce
        """
        self.rows = rows
        self.columns = columns
        self.empty_sign = empty_sign
        self.grid = []
        self.tah = 1

        for column in range(columns):
            temp_row = []  # Pomocná interní proměnná, pro použití v cyklu
            for row in range(0, rows):
                temp_row.append(empty_sign)
            self.grid.append(temp_row)

    def __str__(self) -> str:
        return "Třída reprezuntující hrací pole - grid"

    def vykresli_pole(self) -> str:
        """Vrátí herní pole"""
        # Číslování herního pole - horizontální
        result = "  "
        for row in range(self.rows):
            result += f"{str(row)} "
        result += "\n"

        # Herní pole
        i = 0
        for row in self.grid:
            result += f"{i} "        # Číslování herního pole - vertikální
            for znak in row:
                result += f"{znak} "
            result += "\n"
            i += 1
        return result

    def zapis_pole(self, y: int, x: int) -> None:
        while True:
            if self.grid[x][y] == self.empty_sign:
                if self.tah % 2 == 0:
                    self.grid[x][y] = "O"
                    self.tah += 1
                else:
                    self.grid[x][y] = "X"
                    self.tah += 1
                break
            else:
                print("Pole už je obsazené! Hraj znovu.\n")
                break