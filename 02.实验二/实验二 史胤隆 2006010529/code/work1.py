from typing import *

neighbor_map = {
    'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Eforie': ['Hirsova'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Giurgiu': ['Bucharest'],
    'Hirsova': ['Eforie', 'Urziceni'],
    'Iasi': ['Neamt', 'Vaslui'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Drobeta', 'Lugoj'],
    'Neamt': ['Iasi'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Rimnicu Vilcea': ['Sibiu', 'Pitesti', 'Craiova'],
    'Sibiu': ['Oradea', 'Arad', 'Rimnicu Vilcea', 'Fagaras'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Zerind': ['Arad', 'Oradea']
}


class Node:
    def __init__(self, name: str, history: List[str] = ...):
        self.name = name
        self.history = history if history is not ... else []

    def expand(self) -> List['Node']:
        return [Node(i, self.history + [self.name]) for i in neighbor_map[self.name]]


def bfs(start: 'Node', goal: 'Node'):
    queue = [start]
    while queue:
        node = queue.pop(0)
        print(*node.history, node.name, sep=' -> ')
        if node.name == goal.name:
            print('求解完成。')
            break
        queue.extend(node.expand())
    else:
        print('求解失败。')


a = Node(input('请输入起点城市名: '))   # Arad
b = Node(input('请输入目标城市名: '))   # Bucharest
bfs(a, b)
