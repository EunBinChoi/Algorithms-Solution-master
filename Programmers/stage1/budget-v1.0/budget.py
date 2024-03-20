from typing import List
from itertools import combinations

"""
시간 초과
"""
def solution(d: List[int], budget: int) -> int:
    max_d = 0
    for i in range(1, len(d)+1):
        li = list(combinations(d, i))
        for e in li:
            if sum(e) == budget:
                max_d = max(max_d, len(e))
                break
    return max_d


if __name__ == '__main__':
    d = [1, 3, 2, 5, 4]
    budget = 9
    print(solution(d, budget))

    d = [2, 2, 3, 3]
    budget = 10
    print(solution(d, budget))

    d = [10]
    budget = 10
    print(solution(d, budget))