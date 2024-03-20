import sys
from typing import List

"""
메모리 초과 해결을 위해 dp 사용
"""
def input_data() -> tuple:
    M, N, K = tuple([int(s) for s in sys.stdin.readline().split()])
    secr = list(map(int, sys.stdin.readline().strip().split()))
    user = list(map(int, sys.stdin.readline().strip().split()))
    return M, N, K, secr, user


def dfs(s: int, u: int, secr: List, user: List, dp: List) -> int:
    if s < 0 or u < 0: return 0
    if dp[s][u] != 0: return dp[s][u]
    if secr[s] == user[u]:
        dp[s][u] = 1 + dfs(s - 1, u - 1, secr, user, dp)
        return dp[s][u]
    return dp[s][u]

"""
반례
5 10 5
1 2 3 4 5
1 1 2 3 4 5 1 2 3 4 => 1, (1, 2, 3, 4, 5), 1, 2, 3, 4 => secret
"""
def solution() -> int:
    M, N, K, secr, user = input_data()
    dp = [[0 for _ in range(N)] for _ in range(M)] # M * N

    max_len = 0
    for s in range(len(secr)):
        for u in range(len(user)):
            max_len = max(dfs(s, u, secr, user, dp), max_len)
    return max_len


if __name__ == '__main__':
    print(solution())


