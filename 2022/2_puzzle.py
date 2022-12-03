

from enum import Enum

class NeedTo(Enum):
    WIN = 'Z'
    DRAW = 'Y'
    LOSE = 'X'

class RPZ(Enum):
    ROCK = 'A'
    PAPER = 'B'
    SCISSOR = 'C'
    @staticmethod
    def from_str(str: str) -> 'RPZ':
        for rpz in RPZ:
            if str in rpz.value:
                return rpz
        raise ValueError('No RPZ found for {}'.format(str))


SCORES_FOR_PLAY = {
    RPZ.ROCK : 1,
    RPZ.PAPER : 2,
    RPZ.SCISSOR: 3,
}
WIN_LOSE_DRAW = {
    RPZ.ROCK: {
        NeedTo.WIN: RPZ.PAPER,
        NeedTo.LOSE: RPZ.SCISSOR,
        NeedTo.DRAW: RPZ.ROCK,
    },
    RPZ.PAPER: {
        NeedTo.WIN: RPZ.SCISSOR,
        NeedTo.LOSE: RPZ.ROCK,
        NeedTo.DRAW: RPZ.PAPER,
    },
    RPZ.SCISSOR: {
        NeedTo.WIN: RPZ.ROCK,
        NeedTo.LOSE: RPZ.PAPER,
        NeedTo.DRAW: RPZ.SCISSOR,
    },
}
POINTS_FOR = {
    NeedTo.WIN: 6,
    NeedTo.DRAW: 3,
    NeedTo.LOSE: 0,
}
def get_points_for_play(play: RPZ) -> int:
    return SCORES_FOR_PLAY[play]

def to_be_played(elves_play: RPZ, myself: NeedTo) -> RPZ:
    return WIN_LOSE_DRAW[elves_play][myself]

def get_points(myself: NeedTo, elves_play: RPZ) -> int:
    print(POINTS_FOR[myself], get_points_for_play(to_be_played(elves_play, myself)))
    return POINTS_FOR[myself] + get_points_for_play(to_be_played(elves_play, myself))

def main(puzzle_input: str):
    # Part 1
    aggregator = 0
    for line in puzzle_input.splitlines():
        elves_play, myself = line.split()
        aggregator += get_points(NeedTo(myself), RPZ(elves_play))
    print(aggregator)


if __name__ == "__main__":
    puzzle_input = open("2_input.txt").read()
    # puzzle_input = open("2_easy_input.txt").read()
    main(puzzle_input)