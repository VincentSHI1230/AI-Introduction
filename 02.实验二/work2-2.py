from typing import *

neighbormapWithweight = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Eforie': {'Hirsova': 86},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Giurgiu': {'Bucharest': 90},
    'Hirsova': {'Eforie': 86, 'Urziceni': 98},
    'Iasi': {'Neamt': 87, 'Vaslui': 92},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Drobeta': 75, 'Lugoj': 70},
    'Neamt': {'Iasi': 87},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Sibiu': {'Oradea': 151, 'Arad': 140, 'Rimnicu Vilcea': 80, 'Fagaras': 99},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Zerind': {'Arad': 75, 'Oradea': 71}
}

straight_to_Bucharest = {
    'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242,
    'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151,
    'Iasi': 226,  'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234,
    'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193, 'Sibiu': 253,
    'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
}


class Node:
    def __init__(self, name: str, history: List[str] = [], cost: int = 0):
        self.name = name
        self.history = history
        self.cost = cost

    def expand(self) -> List['Node']:
        return [Node(i, self.history + [self.name], self.cost + neighbormapWithweight[self.name][i]) for i in neighbormapWithweight[self.name]]


def astar(start: 'Node', goal: 'Node'):
    queue = [start]
    while queue:
        node = queue.pop(0)
        print(*node.history, node.name, sep=' -> ')
        if node.name == goal.name:
            print('求解完成。')
            break
        queue.extend(node.expand())
        queue.sort(key=lambda x: x.cost + straight_to_Bucharest[x.name])
    else:
        print('求解失败。')


a = Node(input('请输入起点城市名: '))   # Arad
b = Node(input('请输入目标城市名: '))   # Bucharest
astar(a, b)
