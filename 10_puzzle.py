

from dataclasses import dataclass, field
from typing import List


CLOSING_SYMBOL = {
    "{": "}",
    "(": ")",
    "[": "]",
    "<": ">",
}
POINTS = {
    "corrupted": {
        ")" : 3,
        "]" : 57,
        "}" : 1197,
        ">" : 25137
    },
    "incomplete": {
        ")" : 1,
        "]" : 2,
        "}" : 3,
        ">" : 4
    }
}

class Part2:
    scores: List[int] = field(default_factory=list)

    def run(self, opening_suite: List[str]):
        total = 0
        for missing_closing_char in opening_suite[::-1]:
            total *= 5
            total += POINTS["incomplete"][CLOSING_SYMBOL[missing_closing_char]]
        print("\t", total)
        self.scores.append(total)
    
    def get_score(self):
        scores = sorted(self.scores)
        return (scores[len(scores) // 2])


class Part1:
    part2: Part2
    def __init__(self, part2: Part2) -> None:
        self.part2 = part2
    score: int=0
    def run(self, line):
        opening_suite = []
        for char in line.strip():
            if char in CLOSING_SYMBOL.keys():
                opening_suite.append(char)
                continue
            last_opening_char = opening_suite.pop()
            if char == CLOSING_SYMBOL[last_opening_char]:
                continue
            self.score += POINTS["corrupted"][char]
            opening_suite = []
            break
        if opening_suite:
            self.part2.run(opening_suite)
    def get_score(self):
        return self.score


if __name__ == "__main__":
    input = open("./10_input.txt")
    part2 = Part2()
    part1 = Part1(part2)
    for line in input.readlines():
        part1.run(line)
    print(part1.get_score())
    print(part2.get_score())