from typing import Tuple, Dict, List, Set, Any, Callable
import sys
import matplotlib.pyplot as plt
from operator import itemgetter

def dist(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    """Calculate Manhattan distance between two points in two-dimensional space."""
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)

def initial_distances(z: Tuple[int, int], points: List[Tuple[int, int]]) -> List[int]:
    """Return an array with the distance from z to each point in points."""
    return [dist(point, z) for point in points]

def closest_point(z: Tuple[int, int], points: List[Tuple[int, int]]) -> int:
    """Return the index of the point in array points that is closest to point z.

    In case of a tie, None is returned.
    """
    distances = list(enumerate(initial_distances(z, points)))
    distances.sort(key=itemgetter(1))
    if distances[0][1] == distances[1][1]:
        return None
    else:
        return distances[0][0]

def count_nof_closest(closest_points: List[List[int]]) -> Dict[int, int]:
    """Return the number of points that each point is closest to.

    Parameters:
        closest_points: a 2-dimensional array where each entry holds the index of the point that it is closest to.
    """
    areas: Dict[int, int] = {}
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

def create_grid(points: List[Tuple[int, int]], target_func: Callable[[Tuple[int, int]], int]) -> List[List[int]]:
    min_x: int = min([z[0] for z in points])
    max_x: int = max([z[0] for z in points])
    min_y: int = min([z[1] for z in points])
    max_y: int = max([z[1] for z in points])

    return [[target_func((x,y), points) for x in range(min_x, max_x + 1)] for y in range(min_y, max_y + 1)]

def find_largest_area(points: List[Tuple[int, int]]) -> int:
    """Return the point that has the largest finite area."""
    closest_points = create_grid(points, closest_point)
    areas = count_nof_closest(closest_points)

    infinite_areas = get_infinite_areas(closest_points)
    finite_areas = {area: nof_closest for area, nof_closest in areas.items() if area not in infinite_areas}
    return finite_areas[max(finite_areas.items(), key=itemgetter(1))[0]]

def total_distance(z: Tuple[int, int], points: List[Tuple[int, int]]) -> int:
    distances = list(initial_distances(z, points))
    total = sum(distances)
    return total

def find_area_with_total_distance_below(points: List[Tuple[int, int]], threshold: int) -> int:
    distances = create_grid(points, total_distance)
    total = 0
    for row in distances:
        for col in row:
            if col < threshold:
                total += 1
    return total

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
    print(find_largest_area(points))
    print(find_area_with_total_distance_below(points, 10000))
