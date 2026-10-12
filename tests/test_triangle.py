import math
from pathlib import Path
import unittest

from src.data_loader import (
    load_triangles_from_csv,
    load_triangles_from_json,
)
from src.point import Point
from src.triangle import Triangle

BASE_DIR = Path(__file__).resolve().parent.parent


class TestPoint(unittest.TestCase):
    def test_point_creation_and_repr(self):
        p = Point(3, 4)
        self.assertEqual(p.x, 3.0)
        self.assertEqual(p.y, 4.0)
        self.assertEqual(repr(p), "Point(3, 4)")

    def test_point_distance(self):
        p1 = Point(0, 0)
        p2 = Point(3, 4)
        self.assertAlmostEqual(p1.distance_to(p2), 5.0)

    def test_point_equality(self):
        p1 = Point(1, 2)
        p2 = Point(1, 2)
        p3 = Point(2, 1)
        self.assertEqual(p1, p2)
        self.assertNotEqual(p1, p3)
        self.assertEqual(p1, (1, 2))

    def test_point_indexing_and_iteration(self):
        p = Point(7, 9)
        self.assertEqual(p[0], 7.0)
        self.assertEqual(p[1], 9.0)
        x, y = p
        self.assertEqual((x, y), (7.0, 9.0))


class TestTriangle(unittest.TestCase):
    def test_initial_points_empty(self):
        t = Triangle()
        self.assertEqual(t.points, [])

    def test_add_point_formats(self):
        t = Triangle()
        t.add_point(0, 0)
        t.add_point((1, 2))
        t.add_point(Point(3, 4))
        self.assertEqual(len(t.points), 3)
        self.assertEqual(t.points[0], Point(0, 0))
        self.assertEqual(t.points[1], Point(1, 2))
        self.assertEqual(t.points[2], Point(3, 4))

    def test_perimeter_t1(self):
        t1 = Triangle()
        t1.add_point(0, 0)
        t1.add_point(0, 3)
        t1.add_point(4, 0)
        self.assertAlmostEqual(t1.perimeter(), 12.0)

    def test_perimeter_t2(self):
        t2 = Triangle()
        t2.add_point(1, 2)
        t2.add_point(2, 1)
        t2.add_point(1, 5)
        expected = math.sqrt(2) + math.sqrt(17) + 3.0
        self.assertAlmostEqual(t2.perimeter(), expected)

    def test_perimeter_invalid_point_count(self):
        t = Triangle()
        t.add_point(0, 0)
        with self.assertRaises(ValueError):
            t.perimeter()

    def test_is_equal(self):
        t1 = Triangle()
        t1.add_point(0, 0)
        t1.add_point(0, 3)
        t1.add_point(4, 0)

        t2 = Triangle()
        t2.add_point(1, 2)
        t2.add_point(2, 1)
        t2.add_point(1, 5)

        t3 = Triangle()
        t3.add_point(1, 2)
        t3.add_point(2, 1)
        t3.add_point(1, 5)

        self.assertFalse(t1.is_equal(t2))
        self.assertFalse(t1.is_equal(t3))
        self.assertFalse(t3.is_equal(t1))
        self.assertTrue(t2.is_equal(t3))
        self.assertTrue(t3.is_equal(t2))
        self.assertFalse(t1.is_equal("not a triangle"))

    def test_eq_operator(self):
        t1 = Triangle()
        t1.add_point(0, 0)
        t1.add_point(0, 3)
        t1.add_point(4, 0)

        t3 = Triangle()
        t3.add_point(1, 2)
        t3.add_point(2, 1)
        t3.add_point(1, 5)

        t2 = Triangle()
        t2.add_point(1, 2)
        t2.add_point(2, 1)
        t2.add_point(1, 5)

        self.assertFalse(t1 == t3)
        self.assertTrue(t2 == t3)
        self.assertFalse(t1 == "other")


class TestDataLoader(unittest.TestCase):
    def test_load_from_json(self):
        json_file = BASE_DIR / "data" / "triangles.json"
        triangles = load_triangles_from_json(json_file)
        self.assertIn("t1", triangles)
        self.assertIn("t2", triangles)
        self.assertIn("t3", triangles)
        self.assertAlmostEqual(triangles["t1"].perimeter(), 12.0)
        self.assertEqual(triangles["t2"], triangles["t3"])

    def test_load_from_csv(self):
        csv_file = BASE_DIR / "data" / "triangles.csv"
        triangles = load_triangles_from_csv(csv_file)
        self.assertIn("t1", triangles)
        self.assertIn("t2", triangles)
        self.assertIn("t3", triangles)
        self.assertAlmostEqual(triangles["t1"].perimeter(), 12.0)
        self.assertEqual(triangles["t2"], triangles["t3"])


if __name__ == "__main__":
    unittest.main()
