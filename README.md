<<<<<<< HEAD
# Triangle and Points Project

This project implements a 2D geometry module featuring a `Point` class and a `Triangle` class in Python.

---

## Project Structure

```
anti/
├── venv/              # Python virtual environment
├── point.py           # Point class (Euclidean distance, equality, coordinate access)
├── triangle.py        # Triangle class (add_point, perimeter, is_equal, __eq__)
├── main.py            # Step-by-step demonstration matching the requirements
├── test_triangle.py   # Comprehensive unit test suite (11 tests)
└── README.md          # Documentation and instructions
```

---

## Requirements & Implementation Overview

1. **`Point` Class** ([point.py](file:///home/siva/WORK/anti/point.py)):
   - Stores `x` and `y` coordinates.
   - Calculates Euclidean distance: `p1.distance_to(p2) = sqrt((x2 - x1)^2 + (y2 - y1)^2)`.
   - Supports coordinate unpacking `(x, y) = point`, indexing `p[0]`, `p[1]`, and coordinate tuple equality `p == (x, y)`.

2. **`Triangle` Class** ([triangle.py](file:///home/siva/WORK/anti/triangle.py)):
   - `__init__(self)`: Initializes with an empty list `self.points = []`.
   - `add_point(*args)`: Adds a point to the list (supports `(x, y)`, `Point(x, y)`, or tuple `(x, y)`).
   - `perimeter(self)`: Computes the perimeter $d(p_1, p_2) + d(p_2, p_3) + d(p_3, p_1)$.
   - `is_equal(self, other)`: Checks whether two triangle objects have the same list of points.
   - `__eq__(self, other)`: Overloads the `==` comparison operator to check whether two triangles have equal points.

---

## Quickstart

### 1. Virtual Environment

The virtual environment is created in `venv`. To activate it in your terminal:

```bash
source venv/bin/activate
```

To deactivate when finished:
```bash
deactivate
```

### 2. Run the Main Demonstration

```bash
./venv/bin/python main.py
```
Or with virtual environment activated:
```bash
python main.py
```

### 3. Run the Unit Tests

```bash
./venv/bin/python -m unittest test_triangle.py
```

---

## Walkthrough of Operations

### Step 1: Triangle `t1`
- Points: `(0, 0)`, `(0, 3)`, `(4, 0)`
- Side lengths: $3$, $5$, $4$
- **Perimeter of `t1`**: **$12.0$**

### Step 2: Triangle `t2`
- Points: `(1, 2)`, `(2, 1)`, `(1, 5)`
- Side lengths: $\sqrt{2} \approx 1.4142$, $\sqrt{17} \approx 4.1231$, $3.0$
- **Perimeter of `t2`**: **$\approx 8.5373$**

### Step 3: Check equality between `t1` and `t2`
- `t1.is_equal(t2)` $\rightarrow$ `False` (points do not match)

### Step 4: Triangle `t3`
- Points: `(1, 2)`, `(2, 1)`, `(1, 5)` (identical points to `t2`)

### Step 5: Operations with `is_equal`
- `t1 == t3` $\rightarrow$ `False` (default identity comparison)
- `t1.is_equal(t3)` $\rightarrow$ `False` (different points)
- `t3.is_equal(t1)` $\rightarrow$ `False` (different points)
- `t2.is_equal(t3)` $\rightarrow$ `True` (same points)

### Step 6: Renaming `is_equal` to `__eq__` (Operator Overloading)
- Assigning `__eq__ = is_equal` enables Python's `==` operator on `Triangle` objects.
- `t1 == t3` $\rightarrow$ `False`
- `t2 == t3` $\rightarrow$ `True`
=======
# Triangle_and_points
>>>>>>> 98f27367e7aa2938754a0bf00286cc4d7431b8b8
