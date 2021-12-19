from dataclasses import dataclass
from typing import List, Tuple, get_origin
from functools import reduce
import time


def print_grid(grid: List[List[int]], marked):
    for x, line in enumerate(grid):
        if not x % 10:
            print()
        for y, digit in enumerate(line):
            if not y % 10:
                print(end=' ')
            print(("\033[1m" if (x, y) in marked else "\033[0m") + str(digit.cost), end='')
        print("\033[0m")

def get_edge_index(height_map, x, y):
    ans = [
    ]
    if x + 1 < len(height_map):
        ans.append((x+1, y))
    if x >= 1:
        ans.append((x-1, y))
    if y + 1 < len(height_map[x]):
        ans.append((x, y+1))
    if y >= 1:
        ans.append((x, y-1))
    return ans

def d(grid, node_tuple):
    return ((len(grid) - node_tuple[0])**2 + (len(grid[0]) - node_tuple[1])**2)**0.5
@dataclass
class Node:
    x: int
    y: int
    cost: int

def dijkstra(risk_level: List[List[Node]], node: Node):
    P: set[Node] = set({})
    distance = {(node.x, node.y) : 0}
    node_not_p = {(node.x, node.y)}
    predecesseur = {}
    while len(P) < len(risk_level) * len(risk_level[0]):
        node = min(node_not_p, key=distance.__getitem__)
        node = risk_level[node[0]][node[1]]
        node_not_p.remove((node.x, node.y))
        P.add((node.x, node.y))
        for x_other, y_other in get_edge_index(risk_level, node.x, node.y):
            if (x_other, y_other) in P:
                continue
            neighbour_distance = distance.get((x_other, y_other), 10**10)
            new_distance_possible = distance[(node.x, node.y)] + risk_level[x_other][y_other].cost 
            if neighbour_distance > new_distance_possible:
                distance[(x_other, y_other)] = new_distance_possible
                node_not_p.add((x_other, y_other))
                predecesseur[(x_other, y_other)] = (node.x, node.y)
        if (len(risk_level), len(risk_level[0])) in predecesseur:
            return predecesseur
    return predecesseur


if __name__ == "__main__":
    risk_level = []

    input = open("./15_easy_input.txt")
    input = open("./15_input.txt")
    for line_nb, line in enumerate(input.readlines()):
        risk_level.append([])
        for digit_index, digit in enumerate(line.strip()):
            risk_level[line_nb].append(Node(line_nb, digit_index, int(digit)))
    initial_len_x = len(risk_level)
    initial_len_y = len(risk_level[0])
    full_size = [
        [value for value in line]
        for line in risk_level
    ]
    full_size.extend([[] for _ in range(initial_len_x * 4)])
    for line in full_size:
        line.extend([0 for _ in range(initial_len_y * 5 - len(line))])
    for x_base, line in enumerate(risk_level):
        for y_base, value in enumerate(line):
            for x in range(5):
                for y in range(5):
                    if x == 0 and y == 0:
                        continue
                    current_x = x_base + x*initial_len_x
                    current_y = y_base + y*initial_len_y
                    if x == 0:
                        value = (full_size[current_x][current_y-initial_len_y].cost % 9) + 1
                    else:
                        value = (full_size[current_x - initial_len_x][current_y].cost % 9) + 1
                    full_size[current_x][current_y] = Node(current_x, current_y, value)
    risk_level = full_size
    predecesseur = dijkstra(risk_level, risk_level[0][0])
    path = (len(risk_level)-1, len(risk_level[0])-1)
    risk_sum = 0
    marked = [path]
    while path != (0, 0):
        risk_sum += risk_level[path[0]][path[1]].cost
        path = predecesseur[path]
        marked.append(path)
    print(risk_sum)


