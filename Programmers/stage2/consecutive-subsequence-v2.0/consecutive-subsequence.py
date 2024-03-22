from typing import List

"""
1초 = 20,000,000 = 2x10^7
2초 = 40,000,000 = 4x10^7
10초 = 200,000,000 = 2x10^8

sequence: 1,000,000 == 10^6
O(n^2) = 10^12 
O(n^3) = 10^18
"""


# 다시 풀기
def solution(sequence: List, k: int) -> List:
    answer = [0, len(sequence)]
    s = sequence[0]

    l, r = 0, 0
    while True:
        if s >= k:
            if s == k and r-l < answer[1]-answer[0]:
                answer = [l, r]
            s -= sequence[l]
            l += 1

        else:
            r += 1
            if r == len(sequence): break
            s += sequence[r]

    return answer


if __name__ == '__main__':
    sequence = [1, 2, 3, 4, 5]
    k = 7
    print(solution(sequence, k))

    sequence = [1, 1, 1, 2, 3, 4, 5]
    k = 5
    print(solution(sequence, k))

    sequence = [2, 2, 2, 2, 2]
    k = 6
    print(solution(sequence, k))
