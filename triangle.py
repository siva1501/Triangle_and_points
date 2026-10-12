from point import Point


class Triangle:
    """Represents a triangle defined by a list of points."""

    def __init__(self):
        # Initially this class has an empty list of points
        self.points = []

    def add_point(self, *args):
        """Add a point to the list of points.

        Can be called with:
            add_point(x, y)
            add_point(Point(x, y))
            add_point((x, y))
        """
        if len(args) == 2:
            self.points.append(Point(args[0], args[1]))
        elif len(args) == 1:
            arg = args[0]
            if isinstance(arg, Point):
                self.points.append(arg)
            elif isinstance(arg, (tuple, list)) and len(arg) == 2:
                self.points.append(Point(arg[0], arg[1]))
            else:
                raise TypeError(
                    f"Expected Point or 2-element tuple/list; got {type(arg).__name__}"
                )
        else:
            raise TypeError(f"add_point expects 1 or 2 arguments, got {len(args)}")

    def perimeter(self):
        """Calculate and return the perimeter of the triangle."""
        if len(self.points) != 3:
            raise ValueError(
                f"Triangle must have exactly 3 points to compute perimeter (has {len(self.points)})"
            )

        p1, p2, p3 = self.points
        side1 = p1.distance_to(p2)
        side2 = p2.distance_to(p3)
        side3 = p3.distance_to(p1)

        return side1 + side2 + side3

    def is_equal(self, other):
        """Accept another triangle object as an argument and check whether

        the two triangles have the same list of points.
        """
        if not isinstance(other, Triangle):
            return False
        return self.points == other.points

    def __eq__(self, other):
        """Rename is_equal to __eq__ to support the == operator."""
        return self.is_equal(other)

    def __repr__(self):
        return f"Triangle(points={self.points})"
