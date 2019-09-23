from address import Address


class Matrix:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.addresses = []

    def full_route_successor(self):
        """
        Calculates the route to visit all of the addresses on the grid.
        The delivery man itself is represented as Address(0,0)

        :return: String
        """
        if not self.addresses:
            return None

        # Get directions from starting coordinates (0, 0) to first address
        succ = self.one_to_one_route_successor(
            Address(0, 0),
            self.addresses[0]
        )

        # Get directions for remaining addresses
        for i in range(len(self.addresses) - 1):
            remained_addresses = self.one_to_one_route_successor(
                self.addresses[i],
                self.addresses[i + 1]
            )
            succ += remained_addresses

        return succ

    @staticmethod
    def one_to_one_route_successor(address1, address2):
        """
        Generates a string representation of the route to take between
        two points in the matrix using capital letters to represent cardinal direction

        Calculation in made with simple coordinate subtraction and according to positive or negative
        result of the subtraction different x and y tuples are made.

        :return: String
        """
        x_difference = address2.x - address1.x
        y_difference = address2.y - address1.y

        x_steps = [
            'E' if x_difference > 0 else 'W' for _ in range(abs(x_difference))
        ]
        y_steps = [
            'N' if y_difference > 0 else 'S' for _ in range(abs(y_difference))
        ]

        directions = x_steps + y_steps
        if directions:
            return ''.join(directions) + 'D'
        else:
            return 'D'
