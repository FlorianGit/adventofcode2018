import pytest
from chronal_charge import power_level, largest_total, max_power

@pytest.mark.parametrize("x,y,serial_number,result", [
    (3, 5, 8, 4),
    (122, 79, 57, -5),
    (217, 196, 39, 0),
    (101, 153, 71, 4),
    ])
def test_power_level(x, y, serial_number, result):
    assert power_level(x, y, serial_number) == result

@pytest.mark.parametrize("grid,result", [
    ([[-2, -4, 4, 4, 4],
      [-4, 4, 4, 4, -5],
      [4, 3, 3, 4, -4],
      [1, 1, 2, 4, -3],
      [-1, 0, 2, -5, -2]], (2,2))
    ])
def test_largest_total(grid, result):
    assert largest_total(grid) == result

@pytest.mark.parametrize("serial_number,result", [
    (18, (33,45)),
    (42, (21,61)),
    (6042, (21,61)),
    ])
def test_max_power(serial_number, result):
    assert max_power(serial_number) == result
