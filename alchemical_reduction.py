import sys
from typing import List

def can_react(a: int, b: int) -> bool:
    if abs(a - b) is 32:
        return True
    return False

def reduce_polymer(polymer: str) -> str:
    intlist = [ord(x) for x in polymer]
    index = 0
    while index < len(intlist) - 1:
        if can_react(intlist[index], intlist[index + 1]):
            del intlist[index]
            del intlist[index]
            index -= 1
        else:
            index += 1
    ret = "".join([chr(x) for x in intlist])
    return ret

def remove_type(polymer: str, char: int) -> str:
    intlist = [ord(x) for x in polymer]
    index = 0
    while index < len(intlist):
        if intlist[index] is char or abs(intlist[index] - char) == 32:
            del intlist[index]
        else:
            index += 1
    return "".join([chr(x) for x in intlist])

if __name__ == "__name__":
    polymer = sys.stdin.readline().strip()
    print(len(reduce_polymer(polymer)))

    lengths = [len(reduce_polymer(remove_type(polymer, x))) for x in range(ord('a'), ord('z') + 1)]
    print(min(lengths))
