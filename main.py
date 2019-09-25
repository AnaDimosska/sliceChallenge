import sys
import re
from matrix import Matrix
from matrix import Point


def splitMatrixCoordinates(input_matrix):
    pattern = re.compile('^[0-9]*x[0-9]*$')
    if not pattern.match(input_matrix):
        raise ValueError("Address coordinates must be declared matching format 1,3")
    # This function will split string in parts in regex 'x'
    input_parts = input_matrix.split('x')
    width = int(input_parts[0])
    height = int(input_parts[1])

    # Check if parts between x are positive integers
    if width < 1 or height < 1:
        raise ValueError("Please enter valid grid representation like 5x5")

    return Matrix(width, height)


def splitPointsCoordinates(points, grid):
    pattern = re.compile('^[0-9]*,[0-9]*$')
    if not pattern.match(points):
        raise ValueError("Address coordinates must be declared matching format 1,3")
    # This function will split string in parts in regex ','
    points_array = points.split(',')
    x = int(points_array[0])
    y = int(points_array[1])

    # Coordinates must fit on grid
    if x > grid.width or y > grid.height:
        raise ValueError("Please enter coordinates that will fit into the grid according to your grid input coordinates")

    stations = Point(x, y)
    grid.points.append(stations)

if __name__ == "__main__":
    # Get command line
    args = sys.argv
    len_args = len(args)
    # Separate integers between x and form grid
    grid = splitMatrixCoordinates(args[1])
    stations = []
    stations.append(args[4:])
    len_points = len(stations)
    # Separate integers between , and form stations
    for station in stations:
        splitPointsCoordinates(station, grid)

    print(grid.path())
