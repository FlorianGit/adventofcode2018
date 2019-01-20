import sys
from typing import List

class Node:
    def __init__(self, numbers: List[int]) -> None:
        self.nof_children = numbers.pop(0)
        self.nof_metadata = numbers.pop(0)

        self.children: List[Node] = []
        for _ in range(self.nof_children):
            self.children.append(Node(numbers))

        self.metadata: List[int] = []
        for _ in range(self.nof_metadata):
            self.metadata.append(numbers.pop(0))

def sum_tree(root: Node) -> int:
    total = 0
    for d in root.metadata:
        total += d
    for ch in root.children:
        total += sum_tree(ch)
    return total

def value_of_node(n: Node) -> int:
    total = 0
    if n.children:
        for m in n.metadata:
            if m >= 1 and m <= n.nof_children:
                total += value_of_node(n.children[m - 1])
    else:
        total += sum(n.metadata)
    return total


if __name__ == "__main__":
    numbers = [int(n) for n in sys.stdin.readline().strip().split()]
    tree = Node(numbers)
    print(sum_tree(tree))
    print(value_of_node(tree))
