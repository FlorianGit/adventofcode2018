import sys

ids = [x.strip() for x in sys.stdin.readlines()]
for i in xrange(len(ids[0])):
    tmp = [id[:i] + id[i + 1:] for id in ids]
    tmp.sort()
    for i in xrange(len(tmp) - 1):
        if (tmp[i] == tmp[i + 1]):
            print(tmp[i])
