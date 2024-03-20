import sys
from typing import List, Tuple
from collections import deque


"""
[ PROBLEM LINK ]
https://www.acmicpc.net/problem/2178
"""


def data() -> Tuple:
    N, M = tuple(map(int, sys.stdin.readline().split()))
    maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    return N, M, maze, visited


def bfs(N: int, M: int, maze: List[List[int]], visited: List[List[int]]):
    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]

    queue = deque()
    queue.append([0, 0]) # starting point (0, 0)
    visited[0][0] = True
    while queue:
        a, b = queue.popleft()
        for dx, dy in zip(dxs, dys):
            x = a + dx
            y = b + dy
            if 0 <= x < N and 0 <= y < M and maze[x][y] == 1 and not visited[x][y]:
                queue.append([x, y])
                visited[x][y] = True
                maze[x][y] = maze[a][b] + 1
    return maze[N-1][M-1] # end point (N-1, M-1)


if __name__ == '__main__':
    N, M, maze, visited = data()
    print(bfs(N, M, maze, visited))