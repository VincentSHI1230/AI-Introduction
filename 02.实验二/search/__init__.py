from typing import *


class Node:
    def __init__(self, name: str, g: int = 0, h: int = 0) -> None:
        self.name = name
        self.g = g
        self.h = h

    def __repr__(self) -> str:
        '格式化输出'
        return f"{self.name}({self.g + self.h})"

    def expand(self) -> List['Node']:
        '展开节点'
        return [Node(neighbor['name'], self.g + neighbor['cost'], self.h)
                for neighbor in self.neighbors]


class Edge:
    def __init__(self, start: 'Node', end: 'Node', cost: int) -> None:
        self.start = start
        self.end = end
        self.cost = cost


class Graph:
    def __init__(self, nodes: List['Node'], edges: List['Edge']) -> None:
        self.nodes = nodes
        self.edges = edges


