from typing import IO, Generator, Iterable, List
from dataclasses import dataclass

@dataclass
class BingoInt:
    number: int
    marked: bool = False

@dataclass
class BingoBoard:
    board: List[List[BingoInt]]
    def is_win(self) -> bool:
        for list_ in self.board:
            if len(list(filter(lambda bingoint: bingoint.marked, list_))) == len(list_):
                return True
        for i in range(len(self.board[0])):
            list_ = [
                self.board[j][i] for j in range(len(self.board[0]))
            ]
            if len(list(filter(lambda bingoint: bingoint.marked, list_))) == len(list_):
                return True
        return False
    
    def cycle_through_numbers(self) -> Iterable[BingoInt]:
        for list_ in self.board:
            for bingoint in list_:
                yield bingoint
    def mark_number(self, number: int) -> None:
        for bingoint in self.cycle_through_numbers():
            if bingoint.number == number:
                bingoint.marked = True
    
    def sum_unmarked(self) -> int:
        return sum([
                bingoint.number for bingoint in self.cycle_through_numbers()
                if not bingoint.marked
            ])

    def calculate_score(self, last_called_number: int) -> int:
        return self.sum_unmarked() * last_called_number

    def __str__(self) -> str:
        return '<BingoBoard:\n' + '\n'.join([' '.join(
            [str(bingoint.number) for bingoint in line])
            for line in self.board
        ]) + '>'
    def __repr__(self) -> str:
        return str(self)


def parse_input(input: IO):
    numbers = map(int, input.readline().strip().split(','))
    boards = [
        list(map(int, line.strip().split()))
        for line in input.readlines() if line != '\n'
    ]
    if len(boards) % 5:
        raise AssertionError("board must be 5 line long")
    bingo_boards: List[BingoBoard] = []
    for i in range(int(len(boards) / 5)):
        bingo_boards.append(BingoBoard(
            [
                [BingoInt(number) for number in line]
                for line in boards[i*5:(i+1)*5]
            ]
        ))
    return numbers, bingo_boards
if __name__ == "__main__":
    numbers, bingo_boards = parse_input(open("4_input.txt"))
    for number in numbers:
        for bingo_board in bingo_boards.copy():
            bingo_board.mark_number(number)
            if bingo_board.is_win():
                if len(bingo_boards) == 1:
                    print(bingo_board.calculate_score(number))
                    exit()
                bingo_boards.remove(bingo_board)



