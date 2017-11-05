## @package: Utils.CoordMath
# Math methods for coordinates
import math

## Methods for coordinate math.
class CoordMath():
    ## The constructor.
    # @type self: Coord2d
    # @param self: The object.
    def __init__(self):
        pass

    ## Calculates the euclidean distance between a pair of 2d coordinates
    # @type self: CoordMath
    # @param self: The object.
    #
    #  @type coords1: Coord2d
    #  @param coords1: Coordinates set 1
    #
    #  @type coords2: Coord2d
    #  @param coords2: Coordinates set 2
    #
    #  @rtype: Float
    #  @return: The distance between the set of 2d coordinates.
    def get_distance_2d(self, coords1, coords2):
        if (self.check_coord2d(coords1) & self.check_coord2d(coords2)):  # If coords1 and coords2 are valid
            # Calculate the distance using the distance formula, return the distance.
            return math.sqrt((coords2.get_n() - (coords1.get_n())) ** 2 + \
                             (coords2.get_e() - (coords1.get_e())) ** 2)

    ## Checks that a pair of coordiantes are valid.
    # @type self: CoordMath
    # @param self: The object.
    #
    # @type coordpair: Coord2d
    # @param coordpair: The coordinates to check
    #
    # @rtype: Boolean
    # @return: True if the coordinates are valid, false in all other cases.
    def check_coord2d(self, coord2d):
        from Model.CoordPair import Coord2d
        if (isinstance(coord2d, Coord2d)):  # If this is a Coord2d Object
            if (isinstance(coord2d.get_n(), float) & isinstance(coord2d.get_e(), float)):  # If array of floats
                if (self.check_coord(coord2d.get_n()) & self.check_coord(coord2d.get_e())):  # If valid NW degrees
                    return True
        return False  # Something is wrong

    ## Checks that a pair of coordiantes are valid.
    # @type self: CoordMath
    # @param self: The object.
    #
    # @type fl: float
    # @param fl: The single coordinate to check
    #
    # @rtype: Boolean
    # @return: True if the coordinate is valid, false in all other cases.
    def check_coord(self, fl):
        if (isinstance(fl, float)):  # If float
            if ((fl <= 180.0) & (fl >= -180.0)):  # If valid degrees
                return True
        return False  # Something is wrong
