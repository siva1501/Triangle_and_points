# Triangle and Points Project

This project implements a 2D geometry module in Python featuring a `Point` class and a `Triangle` class.

## Project Structure

```text
anti/
├── point.py           # Point class for coordinates and distance calculations
├── triangle.py        # Triangle class for points, perimeter, and equality
├── main.py            # Demonstration of project functionality
├── test_triangle.py   # Unit tests for the project
└── README.md          # Project documentation
```

## Requirements and Implementation

### 1. Point Class

The `Point` class is implemented in `point.py`.

Features:
- Stores `x` and `y` coordinates.
- Calculates the Euclidean distance between two points.
- Supports coordinate unpacking, such as `(x, y) = point`.
- Supports indexing, such as `point[0]` and `point[1]`.
- Supports equality comparisons with coordinate tuples, such as `point == (x, y)`.

The Euclidean distance between two points is calculated using:

\[
d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}
\]

### 2. Triangle Class

The `Triangle` class is implemented in `triangle.py`.

Features:
- `__init__(self)`: Initializes an empty list of points.
- `add_point(*args)`: Adds points to the triangle.
- `perimeter(self)`: Calculates the perimeter using the distances between the three vertices.
- `is_equal(self, other)`: Checks whether two triangles contain the same points.
- `__eq__(self, other)`: Implements equality comparison using the `==` operator.

The perimeter is calculated as:

\[
P = d(p_1,p_2) + d(p_2,p_3) + d(p_3,p_1)
\]

## Quickstart

### 1. Activate the Virtual Environment

Activate the existing virtual environment:

```bash
source venv/bin/activate
```

To deactivate it when finished:

```bash
deactivate
```

### 2. Run the Main Program

With the virtual environment activated:

```bash
python main.py
```

Alternatively, run the program directly:

```bash
./venv/bin/python main.py
```

### 3. Run Unit Tests

Run the test suite using:

```bash
python -m unittest test_triangle.py
```

Alternatively:

```bash
./venv/bin/python -m unittest test_triangle.py
```

## Example Operations

### 1. Create Triangle `t1`

Vertices:

- `(0, 0)`
- `(0, 3)`
- `(4, 0)`

Side lengths: `3`, `4`, and `5`.

Expected perimeter:

```text
12.0
```

### 2. Create Triangle `t2`

Vertices:

- `(1, 2)`
- `(2, 1)`
- `(1, 5)`

Side lengths:

- `sqrt(2)`
- `sqrt(17)`
- `3`

Expected perimeter:

```text
8.5373
```

### 3. Compare Triangles

The `is_equal()` method checks whether two triangles have the same points.

Example:

```python
t2.is_equal(t3)
```

Expected result when `t2` and `t3` contain the same points in the same order:

```text
True
```

### 4. Operator Overloading

Implementing the `__eq__()` method allows triangle objects to be compared using `==`.

Example:

```python
t2 == t3
```

Expected result when both triangles contain the same points in the same order:

```text
True
```

## Testing

The `test_triangle.py` file contains unit tests for the project's functionality.

Run the tests with:

```bash
python -m unittest test_triangle.py
```

## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- Unit Testing
- Git and GitHub