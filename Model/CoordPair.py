## @package: Model.CoordPair
#  Data structure containing a pair of coordinates.
from Utils.CoordMath import CoordMath
import numpy as np



## Class representing a 2d coordinate pair.
class Coord2d():
    # Class variables
    ne = None
    cmath = CoordMath()

    ## The constructor.
    # @type self: Coord2d
    # @param self: The object.
    def __init__(self):
        self.ne = np.array([None, None])  # Numpy array containing two zeroes
        self.ne.flags.writeable = True # make the array writable

    ## Set the North coordinate
    # @type self: Coord2d
    # @param self: The object.
    #
    # @type n: Float
    # @param n: Distance from equator (180.0 to -180.0 Degrees North)
    #
    # @rtype: Boolean
    # @return: Whether the coordinate assignment was valid.
    def set_n(self, n):
        if(self.cmath.check_coord(n)): # If coord is valid float N degrees
            self.ne[0] = n # set N coord, return true
            return True
        return False # something is wrong.

    ## Set the East coordinate
    # @type self: Coord2d
    # @param self: The object.
    #
    # @type n: Float
    # @param n: Distance from the prime meridian (180.0 to -180.0 Degrees East)
    #
    # @rtype: Boolean
    # @return: Whether the coordinate assignment was valid.
    def set_e(self, e):
        if(self.cmath.check_coord(e)): # If coord is valid float E degrees
            self.ne[1] = e # set E coord, return true
            return True
        return False # something is wrong.

    ## Set the North and East coordinates
    # @type self: Coord2d
    # @param self: The object.
    #
    # @type n: Float
    # @param n: Distance from equator (180.0 to -180.0 Degrees North)
    #
    # @type e: Float
    # @param e: Distance from the prime meridian (180.0 to -180.0 Degrees East)
    #
    # @rtype: Boolean
    # @return: Whether the coordinate assignment was valid.
    def set_ne(self, n, e):
        if(self.cmath.check_coord(n) & self.cmath.check_coord(e)): # If both coords are floats within bounds
            self.ne[0] = n # Set both coordinates, return true
            self.ne[1] = e
            return True
        return False # something is wrong.

    ## Get the North coordinate
    # @type self: Coord2d
    # @param self: The object.
    #
    # @rtype: float
    # @return: A float containing the North coordinate, None if not set.
    def get_n(self):
        return self.ne[0]

    ## Get the East coordinate
    # @type self: Coord2d
    # @param self: The object.
    #
    # @rtype: float
    # @return: A float containing the East coordinate, None if not set.
    def get_e(self):
        return self.ne[1]

    ## Get the North and East coordinates numpy array
    # @type self: Coord2d
    # @param self: The object.
    #
    # @rtype: numpy.array([float, float])
    # @return: A numpy array of floats (or None if not set) containing the North and East coordinates.
    def get_ne(self):
        return self.ne


