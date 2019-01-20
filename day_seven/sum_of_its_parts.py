import sys
from typing import List, Tuple, TypeVar, Dict, Set, NamedTuple
from collections import deque
from heapq import heappush, heappop
import parse

Node = TypeVar("Node")

class Graph:
    """Store a graph and precompute neighbours per node"""
    def __init__(self, edges: List[Tuple[Node, Node]]) -> None:
        self.edges = edges
        self.nodes = set([node for edge in edges for node in edge])
        self.neighbours : Dict[Node, List[Node]]= {node: [] for node in self.nodes}
        for frm, to in self.edges:
            self.neighbours[frm].append(to)

class Simulator:
    """Simulate passage of time"""
    def __init__(self) -> None:
        self._current_time = 0
        self._timeline: List[Tuple[int, Node]] = []

    def enqueue(self, delta_t: int, evt: Node):
        heappush(self._timeline, (self._current_time + delta_t, evt))

    def step(self) -> Tuple[int, Node]:
        t, e = heappop(self._timeline)
        self._current_time = t
        return t, e

    def number_enqueued(self) -> int:
        return len(self._timeline)

def time_needed(c: str) -> int:
    return ord(c) - 4

def available_steps(indegree: Dict[Node, int]) -> List[Node]:
    steps = [node for node, degree in indegree.items() if degree == 0]
    for node in steps:
        indegree.pop(node)
    return steps

def get_indegree(g: Graph) -> Dict[Node, int]:
    """Get a dict with an indegree per node"""
    indegree = {node: 0 for node in g.nodes}
    for _, to in g.edges:
        indegree[to] += 1
    return indegree

def topo_sort(edges: List[Tuple[Node, Node]]) -> List[Node]:
    """Sort the nodes topologically."""
    g = Graph(edges)
    indegree = get_indegree(g)

    ordered_nodes = []
    available = available_steps(indegree)
    while available:
        available.sort()
        node = available.pop(0)
        ordered_nodes.append(node)

        for to in g.neighbours[node]:
            indegree[to] -= 1

        available += available_steps(indegree)

    return ordered_nodes

def topo_sort_with_time(edges: List[Tuple[Node, Node]], nof_workers: int) -> int:
    g = Graph(edges)
    indegree = get_indegree(g)

    sim = Simulator()
    nof_free_workers = nof_workers
    available = available_steps(indegree)
    while sim.number_enqueued() > 0 or available:
        available.sort()
        if available and nof_free_workers > 0:
            node = available.pop(0)
            sim.enqueue(time_needed(node), node)
            nof_free_workers -= 1
        elif sim.number_enqueued() > 0:
            t, n = sim.step()
            nof_free_workers += 1
            for to in g.neighbours[n]:
                indegree[to] -= 1
            available += available_steps(indegree)

    return t

if __name__ == "__main__":
    parser = parse.compile("Step {from} must be finished before step {to} can begin.\n")
    edges = []
    for line in sys.stdin.readlines():
        parsed = parser.parse(line)
        if parsed is not None:
            edges.append((parsed["from"], parsed["to"]))
    print("".join(topo_sort(edges)))
    print(topo_sort_with_time(edges, 5))
