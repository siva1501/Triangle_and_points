# Triangle and Points Project

A modular, clean Python geometry project featuring a `Point` class and a `Triangle` class with dataset loading, perimeter calculation, and operator overloading.

---

## Project Structure

```
anti/
├── data/                      # All dataset and input files
│   ├── README.md              # Data folder documentation
│   ├── triangles.json         # JSON dataset of triangle coordinates (t1, t2, t3)
│   └── triangles.csv          # CSV dataset of triangle coordinates
├── src/                       # All program source code files
│   ├── __init__.py            # Package export definitions
│   ├── point.py               # Point class (Euclidean distance, coordinates, equality)
│   ├── triangle.py            # Triangle class (add_point, perimeter, is_equal, __eq__)
│   ├── data_loader.py         # Utility to load triangles from JSON and CSV files
│   └── main.py                # Main script executing all assignment operations
├── tests/                     # Unit and integration test suite
│   ├── __init__.py
│   └── test_triangle.py       # 13 tests for Point, Triangle, and DataLoader
├── venv/                      # Python virtual environment
├── main.py                    # Root entry point launcher
├── requirements.txt           # Project dependencies and modules list
├── .gitignore                 # Git ignore rules for venv and caches
└── README.md                  # Project documentation
```

---

## Requirements & Modules

All dependencies are recorded in [`requirements.txt`](file:///home/siva/WORK/anti/requirements.txt):

- **External Packages**:
  - `pytest>=8.0.0`: Testing framework
  - `pluggy>=1.5.0`: Plugin manager for pytest
  - `iniconfig>=2.0.0`: Config parser for pytest
- **Standard Library Modules Used**:
  - `math`: For `math.hypot()` and `math.sqrt()` Euclidean distance calculations
  - `json`: Parsing dataset files in `data/triangles.json`
  - `csv`: Reading tabular coordinate records in `data/triangles.csv`
  - `pathlib`: Clean, cross-platform path handling
  - `typing`: Type annotations (`Union`, `Tuple`, `List`, `Dict`, `Iterator`)
  - `unittest`: Testing suite runner
  - `sys`: Module search path resolution

---

## Setup & Execution

### 1. Virtual Environment

Activate the included virtual environment:
```bash
source venv/bin/activate
```

To install/verify dependencies from `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 2. Run the Program

You can run the program either from the root or directly from `src/`:

```bash
# Option A: From root launcher
python main.py

# Option B: Directly from src folder
python src/main.py

# Option C: As a Python module
python -m src.main
```

### 3. Run the Tests

Execute tests using `pytest` or `unittest`:

```bash
# Using pytest
pytest

# Using standard library unittest
python -m unittest discover tests
```

---

## Overview of Operations

1. **Triangle `t1`**:
   - Points: `(0, 0)`, `(0, 3)`, `(4, 0)`
   - Perimeter: **`12.0`** ($3 + 5 + 4$)

2. **Triangle `t2`**:
   - Points: `(1, 2)`, `(2, 1)`, `(1, 5)`
   - Perimeter: **`8.5373`** ($\sqrt{2} + \sqrt{17} + 3.0$)

3. **Equality check (`t1` vs `t2`)**:
   - `t1.is_equal(t2)` $\rightarrow$ **`False`**

4. **Triangle `t3`**:
   - Points: `(1, 2)`, `(2, 1)`, `(1, 5)` (identical coordinates to `t2`)

5. **Operations before `__eq__` operator overloading**:
   - `t1 == t3` $\rightarrow$ **`False`** *(Python default object identity)*
   - `t1.is_equal(t3)` $\rightarrow$ **`False`**
   - `t3.is_equal(t1)` $\rightarrow$ **`False`**
   - `t2 == t3` $\rightarrow$ **`False`** *(Different memory objects)*
   - `t2.is_equal(t3)` $\rightarrow$ **`True`** *(Same point list)*

6. **Renaming `is_equal` to `__eq__`**:
   - `t1 == t3` $\rightarrow$ **`False`** *(Calls `__eq__`, points differ)*
   - `t2 == t3` $\rightarrow$ **`True`** *(Calls `__eq__`, points match)*

7. **Loading datasets from `data/`**:
   - Loads triangles `t1`, `t2`, `t3` directly from [`data/triangles.json`](file:///home/siva/WORK/anti/data/triangles.json) and [`data/triangles.csv`](file:///home/siva/WORK/anti/data/triangles.csv).