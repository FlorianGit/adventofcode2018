import pytest
from marble_mania import sim_game

@pytest.mark.parametrize("nof_players,highest_marble,result", [
    (9, 25, 32),
    (448, 71628, 394486)
    ])
def test_sim_game(nof_players, highest_marble, result):
    assert sim_game(nof_players, highest_marble)[1] == result
