from typing import *

graph = {
    'AP': {'distance': 8, 'neighbors': {}},
    'BBY': {'distance': 8, 'neighbors': {}},
    'DT': {'distance': 2, 'neighbors': {
        'SP': 2
    }},
    'JB': {'distance': 3, 'neighbors': {
        'KB': 4
    }},
    'KB': {'distance': 3, 'neighbors': {
        'BBY': 6,
        'DT': 3
    }},
    'KD': {'distance': 6, 'neighbors': {
        'JB': 2,
        'MP': 4
    }},
    'MP': {'distance': 7, 'neighbors': {
        'BBY': 5,
        'KB': 3
    }},
    'RM': {'distance': 9, 'neighbors': {
        'SSY': 21
    }},
    'SP': {'distance': 0, 'neighbors': {}},
    'SRY': {'distance': 29, 'neighbors': {
        'BBY': 23
    }},
    'UBC': {'distance': 5, 'neighbors': {
        'JB': 3,
        'KD': 3
    }}
}

neighbor_map = {i: [j for j in graph[i]['neighbors']] for i in graph}
neighbormapWithweight = {i: graph[i]['neighbors'] for i in graph}
distance_to_SP = {i: graph[i]['distance'] for i in graph}


class Node:
    def __init__(self, name: str, history: List[str] = ..., cost: int = 0):
        self.name = name
        self.history = history if history is not ... else []
        self.cost = cost

    def expand(self) -> List['Node']:
        return [Node(
            i,
            self.history + [self.name],
            self.cost + neighbormapWithweight[self.name][i]
        ) for i in neighbormapWithweight[self.name]]


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


def ucs(start: 'Node', goal: 'Node'):
    queue = [start]
    while queue:
        node = queue.pop(0)
        print(*node.history, node.name, sep=' -> ')
        if node.name == goal.name:
            print('求解完成。')
            break
        queue.extend(node.expand())
        queue.sort(key=lambda x: x.cost)
    else:
        print('求解失败。')


def astar(start: 'Node', goal: 'Node'):
    queue = [start]
    while queue:
        node = queue.pop(0)
        print(*node.history, node.name, sep=' -> ')
        if node.name == goal.name:
            print('求解完成。')
            break
        queue.extend(node.expand())
        queue.sort(key=lambda x: x.cost + distance_to_SP[x.name])
    else:
        print('求解失败。')


print('\n广度优先搜索: ')
bfs(Node('UBC'), Node('SP'))
print('\n一致代价搜索: ')
ucs(Node('UBC'), Node('SP'))
print('\nA*搜索: ')
astar(Node('UBC'), Node('SP'))
