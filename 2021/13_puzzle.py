
from typing import List
from dataclasses import dataclass

@dataclass
class FoldInstruction:
    axis: str
    value: int

def count_dot(grid: List[List[str]]):
    return sum(
        sum(map(lambda x: x == '#', line))
        for line in grid)

def fold_y(grid: List[List[str]], arround: int) -> List[List[str]]:
    top_sub_list = grid[:arround]
    bottom_sub_list = grid[arround+1:]
    for y, line in enumerate(bottom_sub_list):
        for x, char in enumerate(line):
            if char == '#':
                top_sub_list[-1-y][x] = '#'
    return top_sub_list

def fold_x(grid: List[List[str]], arround: int) -> List[List[str]]:
    left_sub_list = [line[:arround] for line in grid]
    right_sub_list = [line[arround+1:] for line in grid]
    for y, line in enumerate(right_sub_list):
        for x, char in enumerate(line):
            if char == '#':
                left_sub_list[y][-1-x] = '#'
    return left_sub_list



if __name__ == "__main__":
    from pprint import pprint
    input = open("./13_easy_input.txt")
    input = open("./13_input.txt")
    grid: List[List[str]] = []
    max_line: int = 0
    while line := input.readline():
        if line == '\n':
            break
        dot = line.strip().split(",")
        assert len(dot) == 2
        y, x = int(dot[0]), int(dot[1])
        while len(grid) < x+1:
            grid.append([])
        while len(grid[x]) < y+1:
            grid[x].append(' ')
        grid[x][y] = '#'
        if len(grid[x]) >= max_line:
            max_line = len(grid[x])
    for line in grid:
        while len(line) < max_line:
            line.append(' ')

    fold_instructions: List[FoldInstruction] = []
    for line in input.readlines():
        line = line.strip()
        line = line.split(' ')[-1]
        line = line.split('=')
        fold_instructions.append(FoldInstruction(line[0], int(line[1])))
    """
    grid = [[char for char in "#......."],
            [char for char in ".#......"],
            [char for char in "..#....."],
            [char for char in "...#...."],
            [char for char in "....#..."],
            ]
    fold_instructions = [
        FoldInstruction('y', 2)
    ]
    """
    part1 = True
    for intstruction in fold_instructions:
        if intstruction.axis == 'x':
            grid = fold_x(grid, intstruction.value)
        else:
            grid = fold_y(grid, intstruction.value)
        if part1:
            part1 = False
            print(count_dot(grid))
    for line in grid:
        print(''.join(line))