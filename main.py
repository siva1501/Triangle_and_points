"""Demonstration script for Triangle and Point operations.

Follows the step-by-step instructions from the assignment.
"""

from point import Point
from triangle import Triangle


def run_demonstration():
    print("=" * 60)
    print("STEP 1: Create triangle t1 and add points (0,0), (0,3), (4,0)")
    print("=" * 60)
    t1 = Triangle()
    t1.add_point(0, 0)
    t1.add_point(0, 3)
    t1.add_point(4, 0)
    print(f"t1 points: {t1.points}")

    perimeter_t1 = t1.perimeter()
    print(f"Perimeter of t1: {perimeter_t1}")
    print()

    print("=" * 60)
    print("STEP 2: Create triangle t2 and add points (1,2), (2,1), (1,5)")
    print("=" * 60)
    t2 = Triangle()
    t2.add_point(1, 2)
    t2.add_point(2, 1)
    t2.add_point(1, 5)
    print(f"t2 points: {t2.points}")

    perimeter_t2 = t2.perimeter()
    print(f"Perimeter of t2: {perimeter_t2:.4f} (exact: {perimeter_t2})")
    print()

    print("=" * 60)
    print("STEP 3: Check whether t1 and t2 are equal")
    print("=" * 60)
    t1_eq_t2 = t1.is_equal(t2)
    print(f"t1.is_equal(t2) -> {t1_eq_t2}")
    print()

    print("=" * 60)
    print("STEP 4: Create triangle t3 and add points (1,2), (2,1), (1,5)")
    print("=" * 60)
    t3 = Triangle()
    t3.add_point(1, 2)
    t3.add_point(2, 1)
    t3.add_point(1, 5)
    print(f"t3 points: {t3.points}")
    print()

    print("=" * 60)
    print("STEP 5: Operations with is_equal method")
    print("=" * 60)
    # Temporarily remove __eq__ from Triangle to demonstrate behavior before renaming
    saved_eq = Triangle.__eq__
    delattr(Triangle, "__eq__")

    print("[Before adding/renaming __eq__ to Triangle]")
    print(f"t1 == t3         : {t1 == t3} (uses Python default object identity)")
    print(f"t1.is_equal(t3)  : {t1.is_equal(t3)}")
    print(f"t3.is_equal(t1)  : {t3.is_equal(t1)}")
    print(f"t2 == t3         : {t2 == t3} (False because they are different objects in memory)")
    print(f"t2.is_equal(t3)  : {t2.is_equal(t3)} (True because they have the same points)")
    print()

    print("=" * 60)
    print("STEP 6: Rename is_equal to __eq__ (Operator Overloading)")
    print("=" * 60)
    # Renaming is_equal to __eq__
    Triangle.__eq__ = Triangle.is_equal
    print("Renamed/assigned: Triangle.__eq__ = Triangle.is_equal")
    print()
    print("Now repeating operations:")
    print(f"t1 == t3         : {t1 == t3} (calls __eq__, returns False as points differ)")
    print(f"t2 == t3         : {t2 == t3} (calls __eq__, returns True as points are identical!)")
    print("=" * 60)


if __name__ == "__main__":
    run_demonstration()
