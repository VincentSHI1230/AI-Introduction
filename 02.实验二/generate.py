graph = {
    'Arad': {'distance': 366, 'neighbors': {
        'Zerind': 75,
        'Sibiu': 140,
        'Timisoara': 118
    }},
    'Bucharest': {'distance': 0, 'neighbors': {
        'Fagaras': 211,
        'Pitesti': 101,
        'Giurgiu': 90,
        'Urziceni': 85
    }},
    'Craiova': {'distance': 160, 'neighbors': {
        'Drobeta': 120,
        'Rimnicu Vilcea': 146,
        'Pitesti': 138
    }},
    'Drobeta': {'distance': 242, 'neighbors': {
        'Mehadia': 75,
        'Craiova': 120
    }},
    'Eforie': {'distance': 161, 'neighbors': {
        'Hirsova': 86
    }},
    'Fagaras': {'distance': 176, 'neighbors': {
        'Sibiu': 99,
        'Bucharest': 211
    }},
    'Giurgiu': {'distance': 77, 'neighbors': {
        'Bucharest': 90
    }},
    'Hirsova': {'distance': 151, 'neighbors': {
        'Eforie': 86,
        'Urziceni': 98
    }},
    'Iasi': {'distance': 226, 'neighbors': {
        'Neamt': 87,
        'Vaslui': 92
    }},
    'Lugoj': {'distance': 244, 'neighbors': {
        'Timisoara': 111,
        'Mehadia': 70
    }},
    'Mehadia': {'distance': 241, 'neighbors': {
        'Drobeta': 75,
        'Lugoj': 70
    }},
    'Neamt': {'distance': 234, 'neighbors': {
        'Iasi': 87
    }},
    'Oradea': {'distance': 380, 'neighbors': {
        'Zerind': 71,
        'Sibiu': 151
    }},
    'Pitesti': {'distance': 100, 'neighbors': {
        'Rimnicu Vilcea': 97,
        'Craiova': 138,
        'Bucharest': 101
    }},
    'Rimnicu Vilcea': {'distance': 193, 'neighbors': {
        'Sibiu': 80,
        'Pitesti': 97,
        'Craiova': 146
    }},
    'Sibiu': {'distance': 253, 'neighbors': {
        'Oradea': 151,
        'Arad': 140,
        'Rimnicu Vilcea': 80,
        'Fagaras': 99
    }},
    'Timisoara': {'distance': 329, 'neighbors': {
        'Arad': 118,
        'Lugoj': 111}},
    'Urziceni': {'distance': 80, 'neighbors': {
        'Bucharest': 85,
        'Hirsova': 98,
        'Vaslui': 142
    }},
    'Vaslui': {'distance': 199, 'neighbors': {
        'Urziceni': 142,
        'Iasi': 92
    }},
    'Zerind': {'distance': 374, 'neighbors': {
        'Arad': 75,
        'Oradea': 71
    }}
}

neighbor_map = {i: [j for j in graph[i]['neighbors']] for i in graph}
print('neighbor_map = ', neighbor_map)

neighbormapWithweight = {i: graph[i]['neighbors'] for i in graph}
print('neighbormapWithweight = ', neighbormapWithweight)

straight_to_Bucharest = {i: graph[i]['distance'] for i in graph}
print('straight_to_Bucharest = ', straight_to_Bucharest)
