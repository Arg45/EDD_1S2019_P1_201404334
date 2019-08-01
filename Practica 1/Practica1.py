class Menu:
    def __init__ (self):
        print("corrio el constructor")
    def menuP(self):
        print("\n 1.Play (Jugar)\n 2.Scoreboard (Puntuaciones)\n 3.User selection (Usuarios)\n 4.Reports (Reportes)\n 5.Bulk loading (Carga masiva)\n")
        
#Metodo main
if __name__ == "__main__":
    m = Menu()
    m.menuP()
