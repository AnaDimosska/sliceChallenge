class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Matrix:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.points = []

    @staticmethod
    def path_between_two_points(point_one, point_two):

        """
        This function represents the path between two points in the grid

        """
        step_move_x = point_two.x - point_one.x
        step_move_y = point_two.y - point_one.y
        # empty tuple that will be filled with appropriate movement on the X axis
        path_x = []
        for step in range(abs(step_move_x)):
            if step_move_x > 0:
                path_x.append("E")
            else:
                path_x.append("W")

        # empty tuple that will be filled with appropriate movement on the Y axis
        path_y = []
        for step in range(abs(step_move_y)):
            if step_move_y > 0:
                path_x.append("N")
            else:
                path_x.append("S")
        string = path_x + path_y
        new_string = ''
        if string:
            return new_string.join(string) + 'D'
        else:
            return 'D'

    def path(self):
        """
        This function returns String that represents the path between
        the start position of the delivery man and remaining points

        """
        if not self.points:
            return None

        initial = Point(0, 0)
        # successors has now path between (0,0) and first pizza_drop point
        successors = self.path_between_two_points(initial, self.points[0])
        # successors has now path between remained pizza_drop points
        for station in range(len(self.points) - 1):
            remained_successors = self.path_between_two_points(self.points[station], self.points[station + 1])
            successors += remained_successors
        return successors
