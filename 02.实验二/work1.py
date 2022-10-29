from typing import *

neighbor_map = {
    'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
    'Mchadia': ['Drobeta', 'Lugoj'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Neamt': ['Iasi'],
    'Craiova': ['Drobeta', 'RimnicuVilcea', 'Pitesti'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Drobeta': ['Mchadia', 'Craiova'],
    'Pitesti': ['RimnicuVilcea', 'Craiova', 'Bucharest'],
    'Eforie': ['Hirsova'],
    'RimnicuVilcea': ['Sibiu', 'Pitesti', 'Craiova'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Sibiu': ['Oradea', 'Arad', 'RimnicuVilcea', 'Fagaras'],
    'Giurgiu': ['Bucharest'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Hirsova': ['Eforie', 'Urziceni'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Tasi': ['Lugoj', 'Mehadia'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Zerind': ['Arad', 'Oradea']
}


class Node:
    def __init__(self, name: str, history: List[str] = []):
        self.name = name
        self.history = history

    def expand(self) -> List['Node']:
        return [Node(i, self.history + [self.name]) for i in neighbor_map[self.name]]


def bfs(start: 'Node', goal: 'Node'):
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node.name == goal.name:
            return node.history + [node.name]
        queue.extend(node.expand())
    raise Exception('无解')


a = Node(input('请输入起点城市名: '))   # Arad
b = Node(input('请输入目标城市名: '))   # Bucharest
print(bfs(a, b))
