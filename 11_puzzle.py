from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Octopus:
    energy_level: int
    has_flashed: bool = False
    total_flash = 0

    def increase_energy(self) -> bool:
        if self.has_flashed:
            return False
        self.energy_level += 1
        if self.energy_level > 9:
            self.has_flashed = True
            self.total_flash += 1
            return True
        return False

    def end_step(self):
        if self.energy_level > 9:
            self.energy_level = 0
        self.has_flashed = False

def print_grid(grid: List[List[Octopus]]):
    for line in grid:
        for octopus in line:
            print(("\033[1m" if octopus.has_flashed else "\033[0m") + str(octopus.energy_level), end='')
        print()

def get_edge_index(octopus_grid, x, y):
    for x_other in range(x-1, x+2):
        for y_other in range(y-1, y+2):
            if x_other < len(octopus_grid) \
                and x_other >= 0 \
                and y_other < len(octopus_grid[x_other]) \
                and y_other >= 0:
                yield x_other, y_other

def step(octopus_grid: List[List[Octopus]]):
    # increase energy level by 1
    flashing_octopus: List[Tuple[int, int]]= []
    for x, line in enumerate(octopus_grid):
        for y, octopus in enumerate(line):
            flash = octopus.increase_energy()
            if flash:
                flashing_octopus.append((x, y))

    # make every octopus that need to flash flash
    while len(flashing_octopus):
        x, y = flashing_octopus.pop()
        for x_other, y_other in get_edge_index(octopus_grid, x, y):
            flash = octopus_grid[x_other][y_other].increase_energy()
            if flash:
                flashing_octopus.append((x_other, y_other))

    # reset octopus flash and detect if they all flashed in this step
    synchronous_flash = True
    for line in octopus_grid:
        for octopus in line:
            if not octopus.has_flashed:
                synchronous_flash = False
            octopus.end_step()
    return synchronous_flash

if __name__ == "__main__":
    input = open("./11_input.txt")
    octopus_grid: List[List[Octopus]]= []
    for index, line in enumerate(input.readlines()):
        octopus_grid.append([])
        for char in line.strip():
            octopus_grid[index].append(Octopus(int(char)))
    print_grid(octopus_grid)
    iteration = 0
    synchronous_flash = False
    while not synchronous_flash:
        synchronous_flash = step(octopus_grid)
        iteration += 1
        if iteration == 100:
            total_flash = 0
            for line in octopus_grid:
                for octopus in line:
                    total_flash += octopus.total_flash
            print("Part1: ", total_flash)
    print("Part2: ", iteration)
    # print_grid(octopus_grid)

