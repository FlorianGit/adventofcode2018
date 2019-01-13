import sys

def calculate_twice_thrice(id):
    nof_twice = 0
    nof_thrice = 0
    count = [0] * 26
    for ch in id:
        count[ord(ch) - 97] += 1
    return count.count(2), count.count(3)

ids = [x.strip() for x in sys.stdin.readlines()]
nof_twice = 0
nof_thrice = 0
for id in ids:
    x, y = calculate_twice_thrice(id)
    if x is not 0:
        nof_twice += 1
    if y is not 0:
        nof_thrice += 1
print(nof_twice * nof_thrice)
