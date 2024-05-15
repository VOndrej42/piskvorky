import os

class Game:

    def ziskej_souradnice(self):
        self.x = int(input("Zadej souřadnici 'x'"))
        self.y = int(input("Zadej souřadnici 'y'"))
        os.system('cls')
        return self.x, self.y
    
    def vyhodnot_hru(self):
        pass



