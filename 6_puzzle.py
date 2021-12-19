from dataclasses import dataclass
from typing import List, Optional

@dataclass
class LanternFish:
    internal_timer: int
    def pass_day(self) -> Optional['LanternFish']:
        if self.internal_timer == 0:
            self.internal_timer = 6
            return LanternFish(8)
        self.internal_timer -= 1

def pass_day(school_fishes: List[LanternFish]):
    new_fishes = []
    for fish in school_fishes:
        new_fish = fish.pass_day()
        if new_fish:
            new_fishes.append(new_fish)
    school_fishes.extend(new_fishes)

def optimised_solution(school_fishes: List[LanternFish]):
    """
    this create a list of number that keep track of how many fishes there are at any stage of their lives
    """
    block_fishes = [0 for _ in range(9)]
    for fish in school_fishes:
        block_fishes[fish.internal_timer] += 1
    for i in range(256):
        new_block_fishes = [0 for _ in range(9)]
        new_fishes = block_fishes[0]
        block_fishes[0] = 0
        block_fishes[7] += new_fishes
        for i in range(9):
            new_block_fishes[i-1] = block_fishes[i]
            new_block_fishes[8] = 0
        new_block_fishes[8] = new_fishes
        block_fishes = new_block_fishes
    return sum(block_fishes)


if __name__ == "__main__":
    from time import time
    with open("6_input.txt") as file:
        line = file.readline()
    school_fishes = [LanternFish(int(day)) for day in line.strip().split(',')]
    begin = time()
    print(optimised_solution(school_fishes))
    print(f"optimized:{time() - begin}")
    exit()
    begin = time()
    for i in range(256):
        pass_day(school_fishes)
    print(len(school_fishes))
    print(f"not_optimized:{time() - begin}")