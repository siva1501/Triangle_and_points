"""Main entry point for Triangle and Points project.

Demonstrates:
  1. Manual triangle creation and adding points.
  2. Perimeter calculations.
  3. Equality checks using `is_equal` and `__eq__`.
  4. Loading triangle datasets from the data/ folder.
"""

from pathlib import Path
import sys

# Ensure src and root are in sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

try:
    from src.triangle import Triangle
    from src.data_loader import (
        load_triangles_from_json,
        load_triangles_from_csv,
    )
except ImportError:
    from triangle import Triangle
    from data_loader import load_triangles_from_json, load_triangles_from_csv


def run_demonstration():
    print("=" * 70)
    print("           GEOMETRY PROJECT: TRIANGLE AND POINTS")
    print("=" * 70)

    # ---------------------------------------------------------
    # STEP 1: Triangle t1
    # ---------------------------------------------------------
    print("\n--- STEP 1: Create triangle t1 with points (0,0), (0,3), (4,0) ---")
    t1 = Triangle()
    t1.add_point(0, 0)
    t1.add_point(0, 3)
    t1.add_point(4, 0)
    print(f"t1 points: {t1.points}")
    perimeter_t1 = t1.perimeter()
    print(f"Perimeter of t1: {perimeter_t1:.4f} (exact: {perimeter_t1})")

    # ---------------------------------------------------------
    # STEP 2: Triangle t2
    # ---------------------------------------------------------
    print("\n--- STEP 2: Create triangle t2 with points (1,2), (2,1), (1,5) ---")
    t2 = Triangle()
    t2.add_point(1, 2)
    t2.add_point(2, 1)
    t2.add_point(1, 5)
    print(f"t2 points: {t2.points}")
    perimeter_t2 = t2.perimeter()
    print(f"Perimeter of t2: {perimeter_t2:.4f} (exact: {perimeter_t2})")

    # ---------------------------------------------------------
    # STEP 3: Equality check between t1 and t2
    # ---------------------------------------------------------
    print("\n--- STEP 3: Check whether t1 and t2 are equal ---")
    print(f"t1.is_equal(t2) -> {t1.is_equal(t2)}")

    # ---------------------------------------------------------
    # STEP 4: Triangle t3
    # ---------------------------------------------------------
    print("\n--- STEP 4: Create triangle t3 with points (1,2), (2,1), (1,5) ---")
    t3 = Triangle()
    t3.add_point(1, 2)
    t3.add_point(2, 1)
    t3.add_point(1, 5)
    print(f"t3 points: {t3.points}")

    # ---------------------------------------------------------
    # STEP 5: Operations with is_equal method (before __eq__ operator)
    # ---------------------------------------------------------
    print("\n--- STEP 5: Operations with is_equal method ---")
    saved_eq = Triangle.__eq__
    delattr(Triangle, "__eq__")  # Temporarily remove __eq__ to show state before

    print("[Before adding/renaming __eq__ to Triangle]")
    print(f"  t1 == t3         : {t1 == t3} (False: checks object identity by default)")
    print(f"  t1.is_equal(t3)  : {t1.is_equal(t3)} (False: points differ)")
    print(f"  t3.is_equal(t1)  : {t3.is_equal(t1)} (False: points differ)")
    print(f"  t2 == t3         : {t2 == t3} (False: different memory addresses)")
    print(f"  t2.is_equal(t3)  : {t2.is_equal(t3)} (True: identical points)")

    # ---------------------------------------------------------
    # STEP 6: Rename is_equal to __eq__
    # ---------------------------------------------------------
    print("\n--- STEP 6: Rename is_equal to __eq__ (Operator Overloading) ---")
    Triangle.__eq__ = Triangle.is_equal
    print("Action: Triangle.__eq__ = Triangle.is_equal")
    print(f"  t1 == t3         : {t1 == t3} (False: calls __eq__, points differ)")
    print(f"  t2 == t3         : {t2 == t3} (True: calls __eq__, points are identical!)")

    # ---------------------------------------------------------
    # STEP 7: Loading data from data/ folder
    # ---------------------------------------------------------
    print("\n" + "=" * 70)
    print("           LOADING DATA FROM DATA FILES (data/ FOLDER)")
    print("=" * 70)
    data_dir = BASE_DIR / "data"

    json_path = data_dir / "triangles.json"
    if json_path.exists():
        json_triangles = load_triangles_from_json(json_path)
        print(f"\nLoaded from '{json_path.name}': {list(json_triangles.keys())}")
        for name, tri in json_triangles.items():
            print(f"  {name}: perimeter = {tri.perimeter():.4f}, points = {tri.points}")

    csv_path = data_dir / "triangles.csv"
    if csv_path.exists():
        csv_triangles = load_triangles_from_csv(csv_path)
        print(f"\nLoaded from '{csv_path.name}': {list(csv_triangles.keys())}")
        for name, tri in csv_triangles.items():
            print(f"  {name}: perimeter = {tri.perimeter():.4f}, points = {tri.points}")

    print("\n" + "=" * 70)
    print("All operations executed successfully!")
    print("=" * 70)


if __name__ == "__main__":
    run_demonstration()
