from typing import Tuple, Dict, List, Set, Any
import sys
import matplotlib.pyplot as plt

def dist(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    """Calculate Manhattan distance between two points in two-dimensional space."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def initial_distances(z: Tuple[int, int], points: List[Tuple[int, int]]) -> List[int]:
    """Return an array with the distance from z to each point in points."""
    return [dist(point, z) for point in points]

def closest_point(z: Tuple[int, int], points: List[Tuple[int, int]]) -> int:
    """Return the index of the point in array points that is closest to point z.

    In case of a tie, None is returned.
    """
    distances = list(enumerate(initial_distances(z, points)))
    distances.sort(key=lambda x: x[1])
    if distances[0][1] == distances[1][1]:
        return None
    else:
        return distances[0][0]

def exclude_keys(dictionary: Dict[Any, Any], keys: Set[int]):
    """Return a copy of dictionary, with the keys from keys removed."""
    d = dict(dictionary)
    for key in keys:
        if key is not None:
            d.pop(key)
    return d

def count_nof_closest(closest_points: List[List[int]]) -> Dict[int, int]:
    """Return the number of points that each point is closest to.

    Parameters:
        closest_points: a 2-dimensional array where each entry holds the index of the point that it is closest to.
    """
    areas: Dict[int, int] = dict([])
    for row in closest_points:
        for col in row:
            if col is not None and col in areas:
                areas[col] += 1
            elif col is not None:
                areas[col] = 1
            else:
                pass
    return areas

def get_infinite_areas(closest_points: List[List[int]]) -> Set[int]:
    """Return areas that are infinite."""
    infinite_areas: Set[int] = set([])
    infinite_areas |= set(closest_points[0])
    infinite_areas |= set(closest_points[-1])
    infinite_areas |= set([row[0] for row in closest_points])
    infinite_areas |= set([row[-1] for row in closest_points])
    if None in infinite_areas:
        infinite_areas.remove(None)
    return infinite_areas

def create_grid_of_closest(points: List[Tuple[int, int]]) -> List[List[int]]:
    min_x: int = min([z[0] for z in points])
    max_x: int = max([z[0] for z in points])
    min_y: int = min([z[1] for z in points])
    max_y: int = max([z[1] for z in points])

    return [[closest_point((x,y), points) for x in range(min_x, max_x + 1)] for y in range(min_y, max_y + 1)]

def find_largest_area(points: List[Tuple[int, int]]) -> int:
    """Return the point that has the largest finite area."""
    closest_points = create_grid_of_closest(points)
    areas = count_nof_closest(closest_points)

    infinite_areas = get_infinite_areas(closest_points)
    finite_areas = exclude_keys(areas, infinite_areas)
    print(max(finite_areas))
    print(points[max(finite_areas)])
    return finite_areas[max(finite_areas)]

def without_nans(l):
    """Return a copy of l with the None's removed."""
    return [x if x is not None else -1 for x in l]

def visualize(closest_points: List[List[int]]):
    """
    Visualize a grid.
    
    Not used in the solution, only for debugging purposes.
    """
    plt.imshow([without_nans(l) for l in closest_points])
    plt.colorbar()
    plt.show()


if __name__ == "__main__":
    pnts: List[List[str]] = [x.strip().split(', ') for x in sys.stdin.readlines()]
    points: List[Tuple[int, int]] = [(int(z[0]), int(z[1])) for z in pnts]
    print(points)
    print(find_largest_area(points))
