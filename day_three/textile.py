import sys
from typing import Tuple, List, Dict

class Claim:
    def __init__(self, claim_id: int, x_start: int, x_end: int, y_start: int, y_end: int) -> None:
        self.claim_id = claim_id
        self.x_start = x_start
        self.x_end = x_end
        self.y_start = y_start
        self.y_end = y_end

    @classmethod
    def from_string(cls, line):
        claim_id, line = line.split('@')
        claim_id = claim_id.strip('# ')
        starts, deltas = line.strip().split(':')
        x_start, y_start = starts.split(',')
        x_delta, y_delta = deltas.strip().split('x')
        x_end = int(x_start) + int(x_delta)
        y_end = int(y_start) + int(y_delta)
        return cls(int(claim_id), int(x_start), int(x_end), int(y_start), int(y_end))

    def __repr__(self):
        return str(self.x_start) + " " + str(self.x_end) + " " + str(self.y_start) + " " + str(self.y_end)

    def rows(self):
        return range(self.x_start, self.x_end)

    def cols(self):
        return (self.y_start, self.y_end)

def calculate_intersections(lst: List[Tuple]):
    changes = []
    for l in lst:
        changes.append((l[0], 1))
        changes.append((l[1], -1))
    changes.sort(key = lambda x: x[0])
    nof_claims = 0
    col = 0
    total = 0
    for ch in changes:
        if nof_claims > 1:
            total += ch[0] - col
        col = ch[0]
        nof_claims += ch[1]
    return total

def nof_claim_intersections(lst: List[Claim]) -> int:
    claims.sort(key=lambda c: c.x_start)
    rows: Dict[int, List[Tuple]] = dict([])
    for claim in claims:
        for i in claim.rows():
            if i in rows.keys():
                rows[i].append(claim.cols())
            else:
                rows[i] = [claim.cols()]
    total = 0
    for row in rows.values():
        total += calculate_intersections(row)
    return total

def intersect(cl1: Claim, cl2: Claim) -> bool:
    if cl1.x_start <= cl2.x_end and cl2.x_start <= cl1.x_end and cl1.y_start <= cl2.y_end and cl2.y_start <= cl1.y_end:
        return True
    else:
        return False

def claim_without_intersection(lst: List[Claim]) -> int:
    for cl in lst:
        count = 0
        for cl2 in lst:
            if intersect(cl, cl2):
                count += 1
        if count == 1:
            return cl.claim_id
    return None

claims = [Claim.from_string(line) for line in sys.stdin.readlines()]
total = nof_claim_intersections(claims)
print("Total number of intersections: " + str(total))

print("Claim without intersection: " + str(claim_without_intersection(claims)))

