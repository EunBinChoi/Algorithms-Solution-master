from typing import List


def solution(d: List[int], budget: int) -> int:
    ds = sorted(d)

    """
    # O(n^2)
    ans = []
    
    i = 0
    while i < len(ds):
        ans.append(ds[i])
        if sum(ans) > budget:
            ans.pop()
            break
        i += 1
    """

    i = 0
    while i < len(ds):
        budget -= ds[i]
        if budget < 0: break
        i += 1
    return i


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