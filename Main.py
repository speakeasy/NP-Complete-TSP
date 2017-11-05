## Author: AcolyteGeometry (KOB)
#  Description: Main class for Travelling Salesman Problem solver
#  which is famously known as an NP-Complete problem in
#  mathematics, only completely solvable in factorial time.
from TSP.TSPSolver import TSPSolver
from Utils.MathHelpers import MathHelpers
from Utils.MenuT import MenuT


class Main:
    # Class Variables
    tsps = TSPSolver()
    menut = MenuT()
    mathh = MathHelpers()

    ## The constructor.
    def __init__(self):
        pass

    ## Main method for controller flow.
    def Main(self):
        self.menu()

    ## Main menu
    def menu(self):
        mopts = [["TSP Solver", "Select an option:"], ["Solve a random TSP", 1], ["Quit program", 2]]
        sel = self.menut.showMenu(mopts)
        sel = self.mathh.stoi(sel)
        if(sel == 1):
            self.randmenu()
        elif(sel == 2):
            exit(0)

    ## Solve random TSP menu
    def randmenu(self):
        mopts = [["Solve Random TSP", "How many 2d coordinates?"]]
        sel = self.menut.showMenu(mopts)
        sel = self.mathh.stoi(sel)
        if(sel >= 2):
            solve = self.tsps.tsp_solve_rand(sel)
            self.tsps.print_tsp_solve(solve)
        else:
            mopts = [["Invalid number", "Try again?"], ["Yes", 1], ["No", 2]]
            sel = self.menut.showMenu(mopts)
            sel = self.mathh.stoi(sel)
            if(sel == 1):
                self.randmenu()
            elif(sel == 2 | sel != 1):
                self.menu()


main = Main()
main.Main()