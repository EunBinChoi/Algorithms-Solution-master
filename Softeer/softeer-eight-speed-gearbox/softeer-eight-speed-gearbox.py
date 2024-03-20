import sys
from typing import List


def input_data() -> List[int]:
    gear = [int(s) for s in sys.stdin.readline().split()]
    return gear


def solution() -> str:
    gear = input_data()
    checker = "ascending" if gear[1] - gear[0] > 0 else "descending"

    for i in range(2, len(gear)):
        if checker == "ascending" and gear[i] - gear[i - 1] > 0:
            checker = "ascending"
        elif checker == "descending" and gear[i] - gear[i - 1] < 0:
            checker = "descending"
        else:
            checker = "mixed"
    return checker


if __name__ == '__main__':
    print(solution())


