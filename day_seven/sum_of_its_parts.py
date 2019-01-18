import sys
from typing import List, Tuple, TypeVar
from collections import deque
import parse

Node = TypeVar("Node")
def topo_sort(edges: List[Tuple[Node, Node]]) -> List[Node]:
    """Sort the nodes topologically."""
    nodes = set([node for edge in edges for node in edge])
    indegree = {node: 0 for node in nodes}
    for _, to in edges:
        indegree[to] += 1

    ordered_nodes = []
    queue = [node for node, degree in indegree.items() if degree == 0]
    while queue:
        queue.sort()
        node = queue.pop(0)
        ordered_nodes.append(node)

        #TODO: store in advance
        new_nodes = []
        for frm, to in edges:
            if frm == node:
                indegree[to] -= 1
                if indegree[to] == 0:
                    new_nodes.append(to)
        new_nodes.sort()
        for nn in new_nodes:
            queue.append(nn)

    return ordered_nodes

if __name__ == "__main__":
    parser = parse.compile("Step {from} must be finished before step {to} can begin.\n")
    edges = []
    for line in sys.stdin.readlines():
        parsed = parser.parse(line)
        if parsed is not None:
            edges.append((parsed["from"], parsed["to"]))
    print("".join(topo_sort(edges)))
