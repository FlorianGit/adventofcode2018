import pytest
from sum_of_its_parts import topo_sort

@pytest.mark.parametrize("edges,result", [
    ([(2,0), (2,5), (0,1), (0,3), (1,4), (3,4), (5,4)], [2, 0, 1, 3, 5, 4])
    ])
def test_topo_sort(edges, result):
    assert topo_sort(edges) == result

