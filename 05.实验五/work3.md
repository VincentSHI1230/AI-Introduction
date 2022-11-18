```python
import networkx as nx

List = [(0, 1, 1), (0, 2, 2), (0, 4, 7), (0, 6, 4), (0, 7, 8), (1, 2, 2), (1, 3, 3), (1, 7, 7),
        (2, 3, 1), (2, 4, 5), (3, 4, 3), (3, 5, 6), (4, 5, 4), (4, 6, 3), (5, 6, 6), (5, 7, 4), (6, 7, 2)]
G = nx.Graph()
G.add_weighted_edges_from(List)
print('最短路径', nx.shortest_path(G, source=3, target=7, weight='weight'))
print('最短距离', nx.shortest_path_length(G, source=3, target=7, weight='weight'))

```

    最短路径 [3, 4, 6, 7]
    最短距离 8
    
