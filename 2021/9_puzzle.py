
from dataclasses import dataclass
from typing import List
from functools import reduce


def print_grid(grid: List[List[int]]):
    for line in grid:
        for digit in line:
            print(("\033[1m" if digit.marked else "\033[0m") + str(digit.number), end='')
        print()

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

def lowest(height_map, x, y):
    for x_other, y_other in get_edge_index(height_map, x, y):
        if not height_map[x][y].number < height_map[x_other][y_other].number:
            return False
    return True

@dataclass
class MarkedInt:
    number: int
    marked: bool = False

def find_bassin(height_map, x, y):
    number_of_point = 1
    if height_map[x][y].marked or height_map[x][y].number == 9:
        return 0
    height_map[x][y].marked = True
    for x_other, y_other in get_edge_index(height_map, x, y):
        number_of_point += find_bassin(height_map, x_other, y_other)
    return number_of_point


if __name__ == "__main__":
    height_map = []

    input = open("./9_input.txt")
    for line_nb, line in enumerate(input.readlines()):
        height_map.append([])
        for digit in line.strip():
            height_map[line_nb].append(MarkedInt(int(digit)))
    
    # find local minimum :
    sum_risk_level = 0
    bassins = []
    for x, line in enumerate(height_map):
        for y, digit in enumerate(line):
            if not lowest(height_map, x, y):
                continue
            bassins.append(find_bassin(height_map, x, y))
            sum_risk_level += digit.number + 1
    print(sum_risk_level)
    print(reduce(lambda x, y: x*y, sorted(bassins)[::-1][:3]))

# 601600 too low
# 1019700
    
            


