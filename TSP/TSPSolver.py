## @package: TSP.TSPSolver
#  Solves TSP problems in O(!n) time.
from Utils.RandomCoords import RandomCoords
from Utils.CoordMath import CoordMath
from Utils.MathHelpers import MathHelpers
import numpy as np
import itertools

## Class for solving a TSP problem.
class TSPSolver():
    # Class variables.
    arr_coords = None # Stores array of Coord2d objects.
    cmath = CoordMath()
    mathh = MathHelpers()

    ## The constructor.
    def __init__(self):
        pass

    ## Solve a TSP for n number of random coordinates.
    #  @type self: TSPSolver
    #  @param self: The object
    #
    #  @type n: int
    #  @param n: The number of coordinates
    #
    #  @rtype: np.array([Coord2d, ...], [[int, int], ...])
    #  @return: An np array containing coord2d pairs and indicies in order of the shortest route.
    def tsp_solve_rand(self, n):
        print("Generating " + str(n) + " random coordinates...")
        self.arr_coords = RandomCoords().get_rand_coords_arr(n)
        print("Done.")
        return self.solve_tsp(self.arr_coords)


    ## Solve a TSP
    #  @type self: TSPSolver
    #  @param self: The object
    #
    #  @type coords: np.array(Coord2d, ...)
    #  @param coords: np array of coordinates to solve TSP for.
    #
    #  @rtype: np.array([Coord2d, ...], [[int, int], ...])
    #  @return: An np array of arrays of coord2d pairs and indicies in order of the shortest route.
    def solve_tsp(self, coords):
        print("Calculating combinations...")
        lenc = len(coords)
        # Generate all permutations of pairs of coords by index
        permutes = np.array(list(itertools.permutations(range(lenc), lenc))) # [[0,1],[0,2],[1,0],[1,2],[2,0],[2,1]]
        # Calculate distances for every pair combination of coordinates
        print("Done.")
        print("Calculating distances...")
        dists = np.zeros(len(permutes) * (len(permutes[0]) - 1)) # [0, 1, 2, 3, 4, 5]
        di = 0
        for i in range(len(permutes)):
            for j in range(len(permutes[i])):
                if(j < len(permutes[0]) - 1):
                    print(str(di))
                    dists[di] = self.cmath.get_distance_2d(self.arr_coords[permutes[i][j]], self.arr_coords[permutes[i][(j + 1)]])
                    di += 1

        print("Done.")
        print("Restructuring array...")
        # restructure array
        #permutes = np.rot90([permutes[i:i + lenc] for i in range(0, len(permutes), lenc)], 1)
        dists = [dists[i:i + (lenc - 1)] for i in range(0, len(dists), (lenc - 1))]
        print("Done.")
        print("Finding shortest path...")

        # Calculate inital path for first permuation
        bestdist = 0
        totalpermutes = len(permutes)
        bestpermute = 1
        bestpath = np.array([None for i in range(lenc)])
        bestpath.flags.writeable = True
        for i in range(lenc - 1):
            bestdist += dists[0][i]
            bestpath[i] = permutes[i]

        #print(str(list(dists)))
        #print(str(list(permutes)))

        # Calculate the rest of the permutations and compare.
        for i in range(len(permutes)):
            distance = 0
            for j in range(lenc - 1): # permutation distance idx
                distance += dists[i][j]

            if(bestdist >= distance):
                bestdist = distance
                bestpath = np.copy(permutes[i])
                bestpermute = i + 1
            currentp = i + 1
            self.print_progress(currentp, totalpermutes, distance, bestpermute, bestdist)

        print("Done.")
        print("Structuring output.")
        ret = np.array([coords, bestpath])
        print(str(ret))
        return ret

    ## Prints output for each permutation checked.
    #  @type self: TSPSolver
    #  @param self: The object
    #
    #  @type pint: int
    #  @param pint: The current permutation
    #
    #  @type ptot: int
    #  @param ptot: Total number of permutations to check
    #
    #  @type dist: int
    #  @param dist: The current best distance
    def print_progress(self, pint, ptot, cdist, pbest, bdist):
        ptot = self.mathh.floatToInt(ptot)
        print("Current permutation set: " + str(pint) + "/" + str(ptot))
        print("Current distance: " + str(cdist))
        print("Best distance: " + str(bdist))
        print("Best Permutation: " + str(pbest) + "\n")

    ## Print TSP solve to console
    #  @type self: TSPSolver
    #  @param self: The object
    #
    #  @type solve: np.array([Coord2d, ...], [[int, int], ...])
    #  @param solve: An np array containing coord2d pairs and indicies in order of the shortest route.
    def print_tsp_solve(self, solve):
        print("\n\nTSP Index : ( Coordinate North, Coordinate East ):")
        for i in range(len(solve[0])): # Print all of the indicies and coordinates
            print(str(i) + " ( " + str(solve[0][i].get_n()) + "N, " + str(solve[0][i].get_e()) + "E )")
        print("\n\nTSP Shortest Route Step: ( Index => Index )")
        for i in range(len(solve[1]) - 1): # Print the indicies in order of shortest route.
            print(str(i+1) + " ( " + str(solve[1][i]) + " => " + str(solve[1][i+1]) + " )")



