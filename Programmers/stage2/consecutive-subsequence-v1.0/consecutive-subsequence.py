from typing import List

"""
1초 = 20,000,000 = 2x10^7
2초 = 40,000,000 = 4x10^7
10초 = 200,000,000 = 2x10^8

sequence: 1,000,000 == 10^6
O(n^2) = 10^12 
O(n^3) = 10^18
"""


# 시간 초과
def solution(seq: List, k: int) -> List:
    answer = []

    for i, n in enumerate(seq):

        if k == n:
            answer.append([i, i])

        s = n
        for j in range(i+1, len(seq)):
            s += seq[j]

            if s == k:
                answer.append([i, j])

    return sorted(answer, key=lambda x: (x[1]-x[0], x[0]))[0]


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
