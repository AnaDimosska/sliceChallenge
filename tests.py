import unittest
from matrix import Matrix
from matrix import Point
from main import (splitPointsCoordinates, splitMatrixCoordinates)

test_matrix = Matrix(5, 5)
point1 = Point(1, 3)
point2 = Point(4, 4)


class SplitValuesMatrix(unittest.TestCase):

    def test_split_matrix_values(self):
        # Test if given argument matrix equals test matrix coordinates
        matrix_to_compare = splitMatrixCoordinates('5x5')
        self.assertEqual(test_matrix.height, matrix_to_compare.height)
        self.assertEqual(test_matrix.width, matrix_to_compare.width)

        # Incorrect input format
        with self.assertRaises(ValueError):
            splitMatrixCoordinates('5x')

        # Incorrect matrix size
        with self.assertRaises(ValueError):
            splitMatrixCoordinates('0x0')


class SplitValuesPoints(unittest.TestCase):
    def test_split_list_points_values(self):
        # Base test objects
        points = Point(1, 3)

        # Test argument address equals matching base test object
        splitPointsCoordinates('1,3', test_matrix)
        self.assertEqual(points.x, test_matrix.points[0].x)
        self.assertEqual(points.y, test_matrix.points[0].y)

        # Test failure for incorrect formatting
        with self.assertRaises(ValueError):
            splitPointsCoordinates('3, 4', test_matrix)

        # Test failure for negative coordinates
        with self.assertRaises(ValueError):
            splitPointsCoordinates('-3,-1', test_matrix)

        # Test for failure of coordinates larger than grid
        with self.assertRaises(ValueError):
            splitPointsCoordinates('7,8', test_matrix)


class ManhattanTest(unittest.TestCase):
    def test_route_between_two_points(self):
        # Test matrix
        test_matrix.points.append(point1)
        test_matrix.points.append(point2)
        # Calculate path between the two points

        path = test_matrix.path_between_two_points(point1, point2)
        self.assertEqual(path, "EEEND")

    def test_full_route(self):
        # Base test objects

        test_matrix.points.append(point1)
        test_matrix.points.append(point2)

        route = test_matrix.path()
        self.assertEqual(route, 'ENNNDEEEND')


if __name__ == '__main__':
    unittest.main()
