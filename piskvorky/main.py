from handlers.grid import Grid
from handlers.game import Game
import os

grid = Grid()
game = Game()

os.system('cls')

print("Vítej ve hře piškvorky!")
print("Začíná hráč se znakem 'X', prosím zadej postupně souřadnice 'x' a 'y'\n")
print(grid.vykresli_pole())

while True:
    print(grid.grid)
    game.ziskej_souradnice()
    grid.zapis_pole(game.x, game.y)
    print(grid.vykresli_pole())
    if game.vyhodnot_hru(grid.grid, "X", grid.rows, grid.columns):
        print("Konec hry! Vyhrává hráč se symbolem 'X'")
        break
    if game.vyhodnot_hru(grid.grid, "O", grid.rows, grid.columns):
        print("Konec hry! Vyhrává hráč se symbolem 'O'")
        break