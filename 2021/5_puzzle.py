from dataclasses import dataclass, field
from typing import List


@dataclass
class Point:
    x: int
    y: int
    value: str
    @classmethod
    def parse(cls, point: str, name: str):
        pts = [int(coord) for coord in point.split(",")]
        return Point(pts[0], pts[1], name)

@dataclass
class Line:
    point1: Point
    point2: Point
    name: str

    @classmethod
    def parse(cls, line: str, name: str) -> 'Line':
        pts = [Point.parse(coords, str(index)) for index, coords in enumerate(line.strip().split(" -> "))]
        return Line(pts[0], pts[1], name)


@dataclass
class Board:
    board: List[List[int]]
    def draw_point(self, point):
        if len(self.board) <= point.y:
            self.board.extend([[] for _ in range(point.y - len(self.board)+1)])
        line = self.board[point.y]
        if len(line) <= point.x:
            line.extend([0 for _ in range(point.x - len(line)+1)])
        line[point.x] += 1
    @staticmethod
    def create_range(from_:int, to_:int):
        if from_ == to_:
            return range(from_, from_ + (1 if from_ > 0 else -1))
        return range(from_, to_ + (1 if (to_ - from_) > 0 else -1), 1 if ((to_ - from_) > 0) else -1)

    def draw_line(self, line: Line):
        if line.point1.x != line.point2.x\
            and line.point1.y != line.point2.y:
            for x, y in zip(self.create_range(line.point1.x, line.point2.x), self.create_range(line.point1.y, line.point2.y)):
                board.draw_point(Point(x, y, line.name))
            return
        for x in self.create_range(line.point1.x, line.point2.x):
            for y in self.create_range(line.point1.y, line.point2.y):
                board.draw_point(Point(x, y, line.name))
    def cycle_through_element(self):
        for line in self.board:
            for elt in line:
                yield elt
    def display(self):
        print("-----board:-----")
        for list_ in self.board:
            for item in list_:
                print(item or '.', end='')
            print()

if __name__ == "__main__":
    board = Board([
        [0 for i in range(10)]
        for j in range(10)
    ])
    assert Board.create_range(1,3) == range(1, 4)
    assert Board.create_range(1,1) == range(1, 2)
    assert Board.create_range(9,3) == range(9, 2, -1)
    with open("5_input.txt") as file:
        lines = file.readlines()
        print(type(lines))
    for index, line in enumerate(lines):
        board.draw_line(Line.parse(line, str(index)))
    # board.display()
    print(len(list(filter(lambda x: x > 1, board.cycle_through_element()))))

    

