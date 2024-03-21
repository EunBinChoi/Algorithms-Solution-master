from typing import List, Dict


def solution(cap: int, n: int, deliveries: List[int], pickups: List[int]) -> int:
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    cost = 0

    deliver = 0
    pickup = 0

    for i in range(n):
        deliver += deliveries[i]
        pickup += pickups[i]

        while deliver > 0 or pickup > 0:
            deliver -= cap
            pickup -= cap
            cost += (n-i) * 2

    return cost


if __name__ == '__main__':
    # cap = 4
    # n = 5
    # deliver = [1, 0, 3, 1, 2]
    # pickups = [0, 3, 0, 4, 0]
    # print(solution(cap, n, deliver, pickups)) # 16

    cap = 2
    n = 7
    deliver = [1, 0, 2, 0, 1, 0, 2]
    pickups = [0, 2, 0, 1, 0, 2, 0]
    print(solution(cap, n, deliver, pickups)) # 30

    cap = 1
    n = 5
    deliver = [0, 0, 1, 0, 0]
    pickups = [0, 0, 0, 0, 0]
    print(solution(cap, n, deliver, pickups)) # 6

    cap = 2
    n = 2
    deliver = [0, 0]
    pickups = [0, 4]
    print(solution(cap, n, deliver, pickups)) # 8

    cap = 3
    n = 2
    deliver = [2, 4]
    pickups = [4, 2]
    print(solution(cap, n, deliver, pickups)) # 8

