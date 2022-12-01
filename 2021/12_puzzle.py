
from os import add_dll_directory, name, path
from typing import List


class Cave:
    name: str
    linked_cave: List['Cave']
    number_of_visit: int = 0
    def __init__(self, name:str):
        self.name = name
        self.linked_cave = []
    def add_linked_cave(self, cave: 'Cave'):
        self.linked_cave.append(cave)
    def can_be_visited(self, visited_twice: bool):
        ...
    def visited_twice(self):
        if self.name == "start":
            return False
        return self.number_of_visit == 2
    def visit(self, visitor):
        self.number_of_visit += 1
        return visitor(self)
    def reset_visit(self):
        self.number_of_visit -= 1
    def __str__(self) -> str:
        return self.name
    def __repr__(self) -> str:
        return self.name

class BigCave(Cave):
    def can_be_visited(self, visited_twice: bool):
        return True
    def visited_twice(self):
        return False

class SmallCave(Cave):
    def can_be_visited(self, visited_twice: bool):
        if self.name == "start":
            return False
        return self.number_of_visit < (2 if not visited_twice else 1)

def save_cave(cave: Cave, file, indent=0):
    if cave.number_of_visit:
        return
    cave.number_of_visit = 1
    if cave.name == "start":
        file.write("graph graph {\n")
    for child_cave in cave.linked_cave:
        file.write('    ' * indent + cave.name + '--' + child_cave.name + '\n')
        save_cave(child_cave, file, indent + 1)

class NumberOfPath:
    visited_twice: Cave = None
    def __call__(self, cave: Cave) -> List[List[Cave]]:
        if cave.name == 'end':
            return [[cave]]
        if cave.visited_twice():
            self.visited_twice = cave
        paths = []
        for child_cave in cave.linked_cave:
            if child_cave.can_be_visited(self.visited_twice is not None):
                ending_paths = child_cave.visit(self)
                paths.extend([[cave]+ path for path in ending_paths])
                child_cave.reset_visit()
                if child_cave == self.visited_twice:
                    self.visited_twice = None
        return paths

if __name__ == "__main__":
    from pprint import pprint
    input = open("./12_input.txt")
    cave_list: List[Cave] = []
    for line in input.readlines():
        from_, to_ = line.strip().split('-')
        from_cave: Cave = None
        to_cave: Cave = None
        for cave in cave_list:
            if from_ == cave.name:
                from_cave = cave
            if to_ == cave.name:
                to_cave = cave
        if from_cave is None:
            if from_.isupper():
                from_cave = BigCave(from_)
            else:
                from_cave = SmallCave(from_)
            cave_list.append(from_cave)
        if to_cave is None:
            if to_.isupper():
                to_cave = BigCave(to_)
            else:
                to_cave = SmallCave(to_)
            cave_list.append(to_cave)
        from_cave.add_linked_cave(to_cave)
        to_cave.add_linked_cave(from_cave)
    np = NumberOfPath()
    for cave in cave_list:
        if cave.name == "start":
            paths = np(cave)
            print(len(paths))

