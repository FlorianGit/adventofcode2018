import sys

numbers = [int(x.strip()) for x in sys.stdin.readlines()]
print(sum(numbers))
freq = 0
s = set([])
found = False
while not found:
    for n in numbers:
        s.add(freq)
        freq += n
        if freq in s:
            found = True
            print (freq)
