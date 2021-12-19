from dataclasses import dataclass
from typing import Tuple
@dataclass
class Probe:
    vel_x: int
    vel_y: int
    x: int = 0
    y: int = 0
    def __repr__(self) -> str:
        return f"Probe(x={self.x}, y={self.y})"

def step(probe: Probe):
    probe.x += probe.vel_x
    probe.y += probe.vel_y
    if probe.vel_x:
        probe.vel_x -= 1 if probe.vel_x > 0 else -1
    probe.vel_y -= 1

def probe_in(area: Tuple[int, int, int, int], probe:Probe):
    return probe.x >= area[0] \
        and probe.x <= area[1] \
        and probe.y >= area[2] \
        and probe.y <= area[3]

def probe_past(area: Tuple[int, int, int, int], probe:Probe):
    return probe.x > area[1] \
        or probe.y < area[2]

if __name__ == "__main__":
    from pprint import pprint
    input = open("./17_easy_input.txt")
    input = open("./17_input.txt")
    line = input.readline().strip().split(": ")[-1]
    x_range, y_range = line.split(', ')
    x_min, x_max = x_range[2:].split("..")
    y_min, y_max = y_range[2:].split("..")

    area = int(x_min), int(x_max), int(y_min), int(y_max)
    print(area)
    max_high = (0, (0,0))
    all_trajectory = set({})
    range_ = 1000
    for x_vel in range(area[1]+1):
        for y_vel in range(area[2], range_):
            probe = Probe(x_vel, y_vel)
            high = 0
            while not probe_past(area, probe) and not probe_in(area, probe):
                step(probe)
                if high < probe.y:
                    high = probe.y
            if probe_in(area, probe):
                all_trajectory.add((x_vel, y_vel))
                if max_high[0] < high:
                    max_high = (high, (x_vel, y_vel))
    print(max_high)
    print(len(all_trajectory))
