
from types import FunctionType
from typing import Callable, List, Set
from dataclasses import dataclass


def from_list_to_strbin(binary_list: List[int], func: FunctionType) -> int:
    return ''.join(
                map(lambda x: str(int(func(x))),
                binary_list)
            )

def routine(bit_criteria: Callable[[List[str]], str], possible_answer: List[str]):
    inc = 0
    while len(possible_answer) != 1:
        copy = possible_answer.copy()
        bc = bit_criteria(copy)
        for string in copy:
            if string[inc] != bc[inc]:
                possible_answer.remove(string)
                if len(possible_answer) == 1:
                    return possible_answer
        inc += 1
    return possible_answer

def count_number_of_one(lines: List[str]):
    number_of_one = [0] * len(lines[0])
    for line in lines:
        for index, bit in enumerate(line):
            number_of_one[index] += bit == '1'
    return number_of_one


if __name__ == "__main__":
    with open("3_input.txt") as input:
        lines = list(map(str.strip, input.readlines()))
        number_of_one = count_number_of_one(lines)
        half_number_of_lines = len(lines) / 2
        gamma_rate = (from_list_to_strbin(number_of_one, lambda x: x >= half_number_of_lines))
        epsilon_rate = (from_list_to_strbin(number_of_one, lambda x: x <= half_number_of_lines))
        print("power consumption: ", int(gamma_rate, 2) * int(epsilon_rate, 2))


        oxygen_lines = lines.copy()
        CO2_lines = lines.copy()
        bc = lambda lines_: \
            "".join(map(lambda x: str(int(x >= (len(lines_) / 2))),
            count_number_of_one(lines_)))
        oxygen_generator_rating = (routine(bc, oxygen_lines))
        bc = lambda lines_: \
            "".join(map(lambda x: str(int(x < (len(lines_) / 2))),
            count_number_of_one(lines_)))
        CO2_rating = (routine(bc, CO2_lines))
        oxygen_generator_rating = (int(next(iter(oxygen_generator_rating)), 2))
        CO2_rating = (int(next(iter(CO2_rating)), 2))

        life_support_rating = oxygen_generator_rating * CO2_rating
        print("life support ratting: ", life_support_rating)