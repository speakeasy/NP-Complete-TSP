from Model.CoordPair import Coord2d
from numpy.random import uniform as randu
import numpy as np


## Class that generates random coordinates for creating
#  and testing TSP problems.
class RandomCoords():

    ## The constructor.
    def __init__(self):
        pass # Nothing to do.

    ## Get a number of random coordinates
    #  @type self: RandomCoords
    #  @param self: The object
    #
    #  @type n: int
    #  @param n: Number of coordinates to generate
    #
    #  @rtype: np.array(Coord2d...)
    #  @return: an array of Coord2d objects.
    def get_rand_coords_arr(self, n=2):
        arr = np.array([None for i in range(n)]) # Empty array to hold Coord2d objects.
        arr.flags.writeable = True
        for i in range(len(arr)): # Generate random Coord2d for each space in array.
            arr[i] = self.get_rand_coord2d()
        return arr


    ## Get a pair of random coordinates
    #  @type self: RandomCoords
    #  @param self: The object
    #
    #  @rtype: np.array(Float, Float)
    #  @return: A random pair of coordinates N and E (+/- 180 degrees)
    def get_rand_ne(self):
        return randu(-180.0, 180.0, 2)

    ## Get a pair of random coordinates
    #  @type self: RandomCoords
    #  @param self: The object
    #
    #  @rtype: Coord2d
    #  @return: A random pair of coordinates N and E (+/- 180 degrees)
    def get_rand_coord2d(self):
        c2d = Coord2d()
        npcoord = self.get_rand_ne()
        c2d.set_ne(npcoord[0], npcoord[1])
        return c2d

