import pytest
from chronal_coordinates import dist, closest_point, initial_distances, count_nof_closest, find_largest_area, get_infinite_areas, create_grid_of_closest

@pytest.mark.parametrize("a,b,d", [
    ((1,1), (1,1), 0),
    ((1,1), (2,1), 1),
    ((2,1), (1,1), 1),
    ((3,6), (2,7), 2),
    ((2,7), (3,6), 2),
    ((353,177), (91,236), 321),
    ((91,236), (353,177), 321)
    ])
def test_dist(a, b, d):
    assert dist(a,b) == d

TEST_POINTS = [(1,1),(1,6),(8,3),(3,4),(5,5),(8,9)]
TEST_GRID = [[0, 0, 0, 0, 0, None,2, 2, 2, 2], 
     [0, 0, 0, 0, 0, None,2, 2, 2, 2], 
     [0, 0, 0, 3, 3, 4, 2, 2, 2, 2], 
     [0, 0, 3, 3, 3, 4, 2, 2, 2, 2], 
     [None,None,3, 3, 3, 4, 4, 2, 2, 2], 
     [1, 1, None,3, 4, 4, 4, 4, 2, 2], 
     [1, 1, 1, None,4, 4, 4, 4, None,None],
     [1, 1, 1, None,4, 4, 4, 5, 5, 5], 
     [1, 1, 1, None,4, 4, 5, 5, 5, 5], 
     [1, 1, 1, None,5, 5, 5, 5, 5, 5]]
MINIMAL_TEST_GRID = [[0, 0, 0, 0, None,2, 2, 2], 
     [0, 0, 3, 3, 4, 2, 2, 2], 
     [0, 3, 3, 3, 4, 2, 2, 2], 
     [None,3, 3, 3, 4, 4, 2, 2], 
     [1, None,3, 4, 4, 4, 4, 2], 
     [1, 1, None,4, 4, 4, 4, None],
     [1, 1, None,4, 4, 4, 5, 5], 
     [1, 1, None,4, 4, 5, 5, 5], 
     [1, 1, None,5, 5, 5, 5, 5]]


@pytest.mark.parametrize("z,points,results", [
        ((0,0), TEST_POINTS, [2, 7, 11, 7, 10, 17]),
        ((1,1), TEST_POINTS, [0, 5, 9, 5, 8, 15])
    ])
def test_initial_distances(z, points, results):
    assert initial_distances(z, points) == results

@pytest.mark.parametrize("z,points,closest", [
    ((0,0), TEST_POINTS, 0),
    ((1,0), TEST_POINTS, 0),
    ((0,1), TEST_POINTS, 0),
    ((8,0), TEST_POINTS, 2),
    ((4,5), TEST_POINTS, 4),
    ((0,4), TEST_POINTS, None)
    ])
def test_closest_point(z, points, closest):
    assert closest_point(z, points) == closest

@pytest.mark.parametrize("closest_points,result", [
    (TEST_GRID, {0: 15, 1: 14, 2: 21, 3: 9, 4: 17, 5: 13}),
    (MINIMAL_TEST_GRID, {0: 7, 1: 9, 2: 12, 3: 9, 4: 17, 5: 10})
    ])
def test_count_nof_closest(closest_points, result):
    assert count_nof_closest(closest_points) == result

@pytest.mark.parametrize("closest_points,result", [
    (TEST_GRID, {0, 1, 2, 5}),
    (MINIMAL_TEST_GRID, {0, 1, 2, 5})
    ])
def test_infinite_areas(closest_points, result):
    assert get_infinite_areas(closest_points) == result

@pytest.mark.parametrize("points,result", [
    (TEST_POINTS, MINIMAL_TEST_GRID)
    ])
def test_create_grid_of_closest(points, result):
    assert create_grid_of_closest(points) == result

@pytest.mark.parametrize("points,result", [
    (TEST_POINTS, 17),
    ([(300,300), (300,302), (302,300), (302,302), (301,301)], 1),
    ([(1,1), (1,101), (48,51), (51,48), (51,51), (51,54), (54,51), (101,1), (101,101)], 9),
    ([(0,0), (0,100), (1,50), (80,20), (80,50), (80,80), (100,0), (100,50), (100,100)], 1876),
    ([(45, 315), (258, 261), (336, 208), (160, 322), (347, 151), (321, 243), (232, 148), (48, 202), (78, 161), (307, 230), (170, 73), (43, 73), (74, 248), (177, 296), (330, 266), (314, 272), (175, 291), (75, 142), (278, 193), (279, 337), (228, 46), (211, 164), (131, 100), (110, 338), (336, 338), (231, 353), (184, 213), (300, 56), (99, 231), (119, 159), (180, 349), (130, 193), (308, 107), (140, 40), (222, 188), (356, 44), (73, 107), (304, 313), (199, 238), (344, 158), (49, 225), (64, 117), (145, 178), (188, 265), (270, 215), (48, 181), (213, 159), (174, 311), (114, 231), (325, 162)], 3894)
    ])
def test_find_largest_area(points, result):
    assert find_largest_area(points) == result
