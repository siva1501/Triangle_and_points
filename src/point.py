import math
from typing import Union, Tuple, List, Iterator


class Point:
    """Represents a 2D geometric point with x and y coordinates.

    Supports coordinate unpacking, distance calculation, tuple indexing,
    and equality comparisons.
    """

    def __init__(
        self,
        x: Union[float, int, Tuple[float, float], List[float]],
        y: Union[float, int, None] = None,
    ) -> None:
        """Initialize a Point with x and y coordinates or a coordinate pair."""
        if y is None and isinstance(x, (tuple, list)):
            self.x = float(x[0])
            self.y = float(x[1])
        elif y is not None:
            self.x = float(x)
            self.y = float(y)
        else:
            raise ValueError(
                "Point must be initialized with (x, y) or a 2-element tuple/list"
            )

    def distance_to(
        self, other: Union["Point", Tuple[float, float], List[float]]
    ) -> float:
        """Calculate the Euclidean distance to another point.

        Formula: sqrt((x2 - x1)^2 + (y2 - y1)^2)
        """
        if isinstance(other, (tuple, list)):
            other = Point(other[0], other[1])
        return math.hypot(self.x - other.x, self.y - other.y)

    def __eq__(self, other: object) -> bool:
        """Check equality with another Point or a coordinate tuple/list."""
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        if isinstance(other, (tuple, list)) and len(other) == 2:
            return self.x == other[0] and self.y == other[1]
        return False

    def __getitem__(self, index: int) -> float:
        """Allow tuple-like indexing: p[0] -> x, p[1] -> y."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        raise IndexError("Point index out of range (must be 0 or 1)")

    def __iter__(self) -> Iterator[float]:
        """Allow tuple unpacking: x, y = point."""
        yield self.x
        yield self.y

    def __repr__(self) -> str:
        """Readable representation of the Point."""
        x_str = int(self.x) if self.x.is_integer() else self.x
        y_str = int(self.y) if self.y.is_integer() else self.y
        return f"Point({x_str}, {y_str})"
