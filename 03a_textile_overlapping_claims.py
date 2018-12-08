import sys

class Claim:
    def __init__(self, str_claim):
        self.x_start = int(str_claim[0][0])
        self.x_end = int(str_claim[0][0]) + int(str_claim[1][0])
        self.y_start = int(str_claim[0][1])
        self.y_end = int(str_claim[0][1]) + int(str_claim[1][1])

    def __repr__(self):
        return str(self.x_start) + " " + str(self.x_end) + " " + str(self.y_start) + " " + str(self.y_end)

    def rows(self):
        return xrange(self.x_start, self.x_end)

    def cols(self):
        return (self.y_start, self.y_end)

def calculate_intersections(lst):
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

splitted = [line.split('@')[1].split(':') for line in sys.stdin.readlines()]
claims = [(x[0].strip().split(','), x[1].strip().split('x')) for x in splitted]
claims.sort(key=lambda x: x[0][0])
claims = [Claim(claim) for claim in claims]
rows = dict([])
for claim in claims:
    for i in claim.rows():
        if i in rows.keys():
            rows[i].append(claim.cols())
        else:
            rows[i] = [claim.cols()]
total = 0
for row in rows.values():
    total += calculate_intersections(row)
print total

