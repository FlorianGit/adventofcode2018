import sys
import parse
from typing import Dict, List, Tuple
from operator import itemgetter

class Point():
    def __init__(self, x, y, delta_x, delta_y) -> None:
        self.x = x
        self.y = y
        self.delta_x = delta_x
        self.delta_y = delta_y

class Sky():
    def __init__(self, positions: List[Dict[str, str]]) -> None:
        self._points = [Point(int(p['x']), int(p['y']), int(p['delta_x']), int(p['delta_y'])) for p in positions]

    def at_time(self, time: int) -> List[Tuple[int, int]]:
        return [(p.x + time * p.delta_x, p.y + time * p.delta_y) for p in self._points]

    def points_to_grid(self, points: List[Tuple[int, int]]) -> List[List[str]]:
        min_x = min([p[0] for p in points])
        min_y = min([p[1] for p in points])
        max_x = max([p[0] for p in points])
        max_y = max([p[1] for p in points])
        grid = [['#' if (x,y) in points else '.' for x in range(min_x, max_x + 1)] for y in range(min_y, max_y + 1)]
        return grid

    def print_at_time(self, time:int):
        points = self.at_time(time)
        grid = self.points_to_grid(points)
        grid = "\n".join(["".join(row) for row in grid])
        print(grid)

    def find_message(self, target_function):
        for i in range(0, 100000):
            if target_function(self.at_time(i)) <= target_function(self.at_time(i-1)) and target_function(self.at_time(i)) <= target_function(self.at_time(i + 1)):
                self.print_at_time(i)
                print(i)
                break

def shortest(grid: List[Tuple[int, int]]) -> int:
    min_y = min([p[1] for p in grid])
    max_y = max([p[1] for p in grid])
    return max_y - min_y

if __name__ == "__main__":
    parser = parse.compile("position=<{x},{y}> velocity=<{delta_x},{delta_y}>\n")
    positions: List[Dict[str, str]] = [parser.parse(line) for line in sys.stdin.readlines()]
    sky = Sky(positions)
    sky.find_message(shortest)
