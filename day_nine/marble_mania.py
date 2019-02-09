import parse
import sys
from operator import itemgetter
from typing import List, Tuple

class Circle():
    def __init__(self):
        self._marbles = [0]
        self._nof_marbles = 1
        self._current_marble_index = 0

    def add(self, marble_value: int) -> int:
        score = 0
        if marble_value % 23 == 0:
            score += marble_value
            remove_index = (self._current_marble_index - 7) % self._nof_marbles
            self._current_marble_index = remove_index
            score += self._marbles.pop(remove_index)
            self._nof_marbles -= 1
        else:
            insert_at_index = (self._current_marble_index + 2) % self._nof_marbles
            self._marbles.insert(insert_at_index, marble_value)
            self._current_marble_index = insert_at_index
            self._nof_marbles += 1
        return score

def sim_game(nof_players: int, last_marble: int) -> Tuple[int, int]:
    """Simulate a game with nof_players players until last_marble. Return tuple of winning player index, highest score."""
    circle = Circle()
    scores = [0] * nof_players
    marble = 1
    current_player = 0
    while marble <= last_marble:
        scores[current_player] += circle.add(marble)
        current_player = (current_player + 1) % nof_players
        marble += 1
    return max(enumerate(scores), key=itemgetter(1))

if __name__ == "__main__":
    parser = parse.compile("{nof_players} players; last marble is worth {last_marble} points")
    info = parser.parse(sys.stdin.readline().strip())
    print(sim_game(int(info["nof_players"]), int(info["last_marble"])))
    print(sim_game(int(info["nof_players"]), 100 * int(info["last_marble"])))

