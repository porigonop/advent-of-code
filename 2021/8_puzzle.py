
from typing import Set


POSSIBLE_SEGMENT = {
    0: {'a', 'b', 'c', 'e', 'f', 'g'},
    1: {'c', 'f'},
    2: {'a', 'c', 'd', 'e', 'g'},
    3: {'a', 'c', 'd', 'f', 'g'},
    4: {'b', 'c', 'd', 'f'},
    5: {'a', 'b', 'd', 'f', 'g'},
    6: {'a', 'b', 'd', 'e', 'f', 'g'},
    7: {'a', 'c', 'f'},
    8: {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
    9: {'a', 'b', 'c', 'd', 'f', 'g'},
}
POSSIBLE_SEGMENT_BY_LEN = {
    2: {'c', 'f'}, # only 1
    3: {'a', 'c', 'f'}, # only 7
    4: {'b', 'c', 'd', 'f'}, # only 4
}

def remove_found(combinaison: dict[str, Set[str]]) -> dict[str, Set[str]]:
    found_set = list(map(lambda x: combinaison[x],
        filter(lambda x: len(combinaison[x]) == 1, combinaison)))
    for set_ in found_set:
        remove_set(set_, combinaison)
    return combinaison

def remove_pair(combinaison: dict[str, Set[str]]):
    pairs = []
    seen = set()
    for set_ in combinaison.values():
        if len(set_) == 2:
            if ''.join(set_) in seen:
                pairs.append(set_)
            seen.add(''.join(set_))
    for pair in pairs:
        remove_set(pair, combinaison)
    
def remove_set(to_remove: set, combinaison: dict[str, Set[str]]):
    for comb in combinaison.values():
        if len(comb) == len(to_remove):
            continue
        for value in to_remove:
            comb.discard(value)

if __name__ == "__main__":
    input = open("./8_input.txt")
    sum_final = 0
    for line in input.readlines():
        # line = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
        combinaison = {
            'a': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
            'b': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
            'c': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
            'd': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
            'e': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
            'f': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
            'g': {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
        }
        input, output = line.split('|')
        input = input.strip().split(' ')
        output = output.strip().split(' ')
        # input = ["ab", "eafb", "dab", "acedgf"]
        #            1   4       7       8
        # input = ["cdfbe", "gcdfa"]
        # 2,3,5
        for digit in input:
            if POSSIBLE_SEGMENT_BY_LEN.get(len(digit)):
                for key in digit:
                    combinaison[key] = combinaison[key].intersection(POSSIBLE_SEGMENT_BY_LEN.get(len(digit)))
        remove_pair(combinaison)
        remove_pair(combinaison)
        remove_found(combinaison)
        # 2 - 3 - 5
        ttf = list(filter(lambda x: len(x) == 5, input))
        for i in range(3):
            found = True
            for digit in ttf[i]:
                if digit not in ttf[i-1] and digit not in ttf[i-2]:
                    found = False
            if found:
                break
        three = ttf[i]
        for key in three:
            combinaison[key] = combinaison[key].intersection(POSSIBLE_SEGMENT[3])
        remove_found(combinaison)
        # 2
        for digit in input:
            if len(digit) != 5:
                continue
            found = True
            passed = 0
            for key in digit:
                if len(combinaison[key]) != 1:
                    passed += 1
                    if passed == 2:
                        found = False
                    continue
                if next(iter(combinaison[key])) not in POSSIBLE_SEGMENT[2]:
                    found = False
            if  found:
                break
        two = digit
        for value in two:
            if 'f' in combinaison[value]:
                combinaison[value].remove('f')
        remove_found(combinaison)
        for set_ in combinaison.values():
            assert len(set_) == 1
        values = []
        for digit in output:
            true_digit = ''.join(map(lambda key: next(iter(combinaison[key])), digit))
            for value, set_ in POSSIBLE_SEGMENT.items():
                if len(set_) != len(true_digit):
                    continue
                found_value = True
                for d in true_digit:
                    if d not in set_:
                        found_value = False
                        break
                if found_value:
                    values.append(value)
        sum_final += int(''.join(map(str, values)))
    print(sum_final)