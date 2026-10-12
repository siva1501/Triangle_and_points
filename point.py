import math


class Point:
    """Represents a 2D point with x and y coordinates."""

    def __init__(self, x, y=None):
        if y is None and isinstance(x, (tuple, list)):
            self.x = float(x[0])
            self.y = float(x[1])
        else:
            self.x = float(x)
            self.y = float(y)

    def distance_to(self, other):
        """Calculate the Euclidean distance between this point and another point."""
        if isinstance(other, (tuple, list)):
            other = Point(other[0], other[1])
        return math.hypot(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        """Check equality with another Point or a coordinate pair (tuple/list)."""
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        if isinstance(other, (tuple, list)) and len(other) == 2:
            return self.x == other[0] and self.y == other[1]
        return False

    def __getitem__(self, index):
        """Allow index access like a tuple: point[0] -> x, point[1] -> y."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        raise IndexError("Point index out of range (must be 0 or 1)")

    def __iter__(self):
        """Allow tuple unpacking: x, y = point."""
        yield self.x
        yield self.y

    def __repr__(self):
        x_display = int(self.x) if self.x.is_integer() else self.x
        y_display = int(self.y) if self.y.is_integer() else self.y
        return f"Point({x_display}, {y_display})"
