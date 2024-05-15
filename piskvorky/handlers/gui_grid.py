import tkinter as tk

class Grid:
    def __init__(self, rows: int = 3, columns: int = 3):
        self.mark = "X"
        self.rows = rows
        self.columns = columns
        self.grid = [[tk.Button(width=6, height=3) for _ in range(columns)] for _ in range(rows)]

        # Vytvoření hracího pole
        for row in range(rows):
            for column in range(columns):
                self.grid[row][column].grid(row = row, column = column)

    def draw_grid(self):
        # Zobrazení hracího pole
        for row in self.grid:
            for button in row:
                button.config(text = " ")  # Inicializace tlačítek prázdnými znaky

    def handle_click(self, event):
        # Získání řádku a sloupce kliknutého tlačítka
        row = event.widget.grid_info()["row"]
        column = event.widget.grid_info()["column"]

        # Označení tlačítka znakem hráče
        self.grid[row][column].config(text = self.mark)

# Vytvoření instance herního pole a zobrazení
grid = Grid()
grid.draw_grid()

# Nastavení obsluhy událostí pro kliknutí myší na tlačítka
for row in grid.grid:
    for button in row:
        button.bind("<Button-1>", grid.handle_click)

# Spuštění hlavní smyčky Tkinter
tk.mainloop()