import sys
from typing import List

"""
메모리 1024MB == 8.192e+9 초과
3000 + 3000 + (1 + 2 + 3 + 3000) * 3000 
= 6000 + (2999 * 3000 / 2) * 3000 
"""
def input_data() -> tuple:
    M, N, K = tuple([int(s) for s in sys.stdin.readline().split()])
    secr = list(map(int, sys.stdin.readline().strip().split()))
    user = list(map(int, sys.stdin.readline().strip().split()))
    return M, N, K, secr, user


def get_partial_combination(li: List):
    li_comb = []
    for i in range(len(li)):
        for j in range(1, len(li)-i+1):
            li_comb.append(li[i:i+j])
    return li_comb

"""
반례
5 10 5
1 2 3 4 5
1 1 2 3 4 5 1 2 3 4 => 1, (1, 2, 3, 4, 5), 1, 2, 3, 4 => secret
"""
def solution() -> int:
    M, N, K, secr, user = input_data()
    secr_comb = get_partial_combination(secr)
    user_comb = get_partial_combination(user)
    # print(secr_comb)
    # print(user_comb)

    max_len = 0
    for i in range(len(user_comb)):
        for j in range(len(secr_comb)):
            if user_comb[i] == secr_comb[j]:
                max_len = max(max_len, len(secr_comb[j]))
    return max_len


if __name__ == '__main__':
    print(solution())


