graph = {
    'AP': {'distance': 8, 'neighbors': {}},
    'BBY': {'distance': 8, 'neighbors': {}},
    'DT': {'distance': 2, 'neighbors': {
        'SP': 2,
    }},
    'JB': {'distance': 3, 'neighbors': {
        'KB': 4,
    }},
    'KB': {'distance': 3, 'neighbors': {
        'BBY': 6,
        'DT': 3,
    }},
    'KD': {'distance': 6, 'neighbors': {
        'JB': 2,
        'MP': 4,
    }},
    'MP': {'distance': 7, 'neighbors': {
        'BBY': 5,
        'KB': 3,
    }},
    'RM': {'distance': 9, 'neighbors': {
        'SSY': 21,
    }},
    'SRY': {'distance': 29, 'neighbors': {
        'BBY': 23,
    }},
    'SP': {'distance': 0, 'neighbors': {}},
    'UAC': {'distance': 5, 'neighbors': {
        'KD': 3,
        'JB': 3,
    }},
}

neighbor_map = {i: [j for j in graph[i]['neighbors']] for i in graph}
print('neighbor_map = ', neighbor_map)

neighbormapWithweight = {i: graph[i]['neighbors'] for i in graph}
print('neighbormapWithweight = ', neighbormapWithweight)

straight_to_Bucharest = {i: graph[i]['distance'] for i in graph}
print('straight_to_Bucharest = ', straight_to_Bucharest)
