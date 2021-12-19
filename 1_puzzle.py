
from typing import List


def difference_between(mylist: List[int], sum_item: int=0) -> List[int]:
    return [
        (sum(mylist[a+1:a+1+(sum_item or 1)])) - (sum(mylist[a:a+(sum_item or 1)]))
        for a in range(len(mylist)-(sum_item or 1))
    ]

if __name__ == "__main__":
    input = open("input.txt", "r")
    list_scan = list(map(int, input.readlines()))
    # 1st
    print(len(list(filter(lambda x: x > 0, difference_between(
        list_scan)))))
    # 2nd
    print(len(list(filter(lambda x: x > 0, difference_between(
        list_scan,
        3)))))