import pytest
from stars_align import Sky

@pytest.mark.parametrize("positions,time,result", [
    ([{"x": '1', "y": '2', "delta_x": '1', "delta_y": '2'}], 0, [(1,2)]),
    ([{"x": '1', "y": '2', "delta_x": '1', "delta_y": '2'}], 1, [(2,4)]),
    ([{"x": '1', "y": '2', "delta_x": '1', "delta_y": '2'}, {"x": '1', "y": '2', "delta_x": '-1', "delta_y": '-2'}], 1, [(2,4), (0,0)]),
    ])
def test_sky_at_time(positions, time, result):
    sky = Sky(positions)
    assert(result == sky.at_time(time))


