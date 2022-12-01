
from os import remove
from time import time
from typing import Dict, List

def step(polymer: List[str], pair_insertion: Dict[str, str]):
    new_list = []
    polymer = ''.join(polymer)
    i=0
    for i in range(len(polymer) - 1):
        new_list.append(polymer[i])
        poly = polymer[i:i+2]
        if poly in pair_insertion:
            new_list.append(pair_insertion[poly])
    new_list.append(polymer[i+1])
    return new_list

def number_of_occurence(polymer: List[str], pair_insertion: Dict[str, str], step_number: int, occurence: Dict[str, int]) -> Dict[str, int]:
    for _ in range(step_number):
        polymer = step(polymer, pair_insertion)
    for char in polymer:
        occurence[char] = occurence.get(char, 0) + 1
    return occurence

def memory_efficient_occurence(polymer: List[str], pair_insertion: Dict[str, str], step_count: int) -> Dict[str, int]:
    """
    dead code
    used initially to split polymer into pair and apply n step to them individually to count
    the occurence in each pair
    """
    remove_char = {}
    occurence = {}
    for index in range(1, len(polymer) - 1):
        occurence = number_of_occurence(polymer[index-1:index+1], pair_insertion, step_count, occurence)
        remove_char[polymer[index]] = remove_char.get(polymer[index], 0) + 1
    occurence = number_of_occurence(polymer[len(polymer)-2:], pair_insertion, step_count, occurence)
    for char, occu in remove_char.items():
        occurence[char] = occurence.get(char, 0) - occu
    return occurence

def dict_of_occurence(pair_insertion: Dict[str, str], step_number: int) -> Dict[str, Dict[str, int]]:
    ans = {}
    for key in pair_insertion:
        ans[key] = number_of_occurence(key, pair_insertion, step_number, {})
    return ans

if __name__ == "__main__":
    from pprint import pprint
    input = open("./14_easy_input.txt")
    input = open("./14_input.txt")
    polymer = input.readline().strip()
    polymer_list = []
    for char in polymer:
        polymer_list.append(char)
    pair_insertion = {}
    input.readline() # \n
    for line in input.readlines():
        line = line.strip().split(' -> ')
        pair_insertion[line[0]] = line[1]
    
    number_iteration = 40
    first_part = 20
    second_part = number_iteration - first_part
    for _ in range(first_part):
        polymer_list = step(polymer_list, pair_insertion)
    remove_char = {}
    occurence = {}
    dict_pair_to_occurence = dict_of_occurence(pair_insertion, second_part)
    polymer_list = ''.join(polymer_list)
    for index in range(1, len(polymer_list) - 1):
        occurence_new = dict_pair_to_occurence[polymer_list[index-1:index+1]]
        remove_char[polymer_list[index]] = remove_char.get(polymer_list[index], 0) + 1
        for char, occu in occurence_new.items():
            occurence[char] = occurence.get(char, 0) + occu
    occurence_new = dict_pair_to_occurence[polymer_list[len(polymer_list)-2:]]
    occurence = {
        char: occurence_new.get(char, 0) +
        occurence.get(char, 0) - 
        remove_char.get(char, 0)
        for char in pair_insertion.values()
    }
    mi = min(occurence.values())
    ma = max(occurence.values())
    print(ma - mi)
