from typing import *

neighbormapWithweight = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Mchadia': {'Drobeta': 75, 'Lugoj': 70},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Neamt': {'Iasi': 87},
    'Craiova': {'Drobeta': 120, 'RimnicuVilcea': 146, 'Pitesti': 138},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Drobeta': {'Mchadia': 75, 'Craiova': 120},
    'Pitesti': {'RimnicuVilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Eforie': {'Hirsova': 86},
    'RimnicuVilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Sibiu': {'Oradea': 151, 'Arad': 140, 'RimnicuVilcea': 80, 'Fagaras': 99},
    'Giurgiu': {'Bucharest': 90},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Hirsova': {'Eforie': 86, 'Urziceni': 98},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Tasi': {'Lugoj': 111, 'Mehadia': 70},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Zerind': {'Arad': 75, 'Oradea': 71}
}
