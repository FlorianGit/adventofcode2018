from math import floor
from typing import List, Tuple

def power_level(x: int, y: int, serial_number: int) -> int:
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial_number
    power_level *= rack_id
    power_level = floor(power_level / 100) - 10 * floor(power_level / 1000)
    power_level -= 5
    return power_level

def sum_square_from(grid: List[List[int]], start_x: int, start_y: int) -> int:
    total = 0
    for y in range(start_y, start_y + 3):
        for x in range(start_x, start_x + 3):
            total += grid[y][x]
    return total

def largest_total(grid: List[List[int]]) -> Tuple[int, int]:
    current_max = ((0,0), -1000)
    n = len(grid)
    for start_x in range(0, n - 2):
        for start_y in range(0, n - 2):
            value = sum_square_from(grid, start_x, start_y)
            if value > current_max[1]:
                current_max = ((start_x + 1, start_y + 1), value)
    return current_max[0]

def max_power(serial_number: int) -> Tuple[int, int]:
    grid = [[power_level(x, y, serial_number) for x in range(1, 301)] for y in range(1, 301)]
    return largest_total(grid)

if __name__ == "__main__":
    print(max_power(6042))
