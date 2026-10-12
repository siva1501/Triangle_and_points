import csv
import json
from pathlib import Path
from typing import Dict, Union

try:
    from src.triangle import Triangle
except ImportError:
    from triangle import Triangle


def load_triangles_from_json(file_path: Union[str, Path]) -> Dict[str, Triangle]:
    """Load triangles from a JSON file.

    Format expected:
    {
        "t1": [[0, 0], [0, 3], [4, 0]],
        "t2": [[1, 2], [2, 1], [1, 5]]
    }
    """
    path = Path(file_path)
    if not path.is_file():
        raise FileNotFoundError(f"Data file not found at: {path}")

    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    triangles: Dict[str, Triangle] = {}
    for name, points in data.items():
        t = Triangle()
        for pt in points:
            t.add_point(pt[0], pt[1])
        triangles[name] = t

    return triangles


def load_triangles_from_csv(file_path: Union[str, Path]) -> Dict[str, Triangle]:
    """Load triangles from a CSV file.

    Expected CSV columns: triangle_id, x, y
    """
    path = Path(file_path)
    if not path.is_file():
        raise FileNotFoundError(f"Data file not found at: {path}")

    triangles: Dict[str, Triangle] = {}
    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            t_id = row["triangle_id"]
            if t_id not in triangles:
                triangles[t_id] = Triangle()
            triangles[t_id].add_point(float(row["x"]), float(row["y"]))

    return triangles
