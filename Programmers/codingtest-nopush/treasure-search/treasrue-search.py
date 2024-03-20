from typing import List, Tuple
from collections import deque
from queue import PriorityQueue

"""
이게 정답인지 확실하게 모르겠지만 테케에 대해서는 잘됨
"""


def initpmap(map: List[List[int]], c: int) -> List[List[int]]:
    pmap = [[0 for _ in range(len(map[0]))] for _ in range(len(map))]
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 0:
                pmap[i][j] = 1
            elif map[i][j] == 1:
                pmap[i][j] = c
            elif map[i][j] == 2:
                pmap[i][j] = 0
            elif map[i][j] == 3:
                pmap[i][j] = 1
    return pmap


def print2darray(arr2d: List[List[int]], enter: str = '\n') -> None:
    for i in range(len(arr2d)):
        for j in range(len(arr2d[0])):
            print('%3d' % arr2d[i][j], end=' ')
        print()
    print(enter)


def location(map: List[List[int]], value: int) -> List[int]:
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == value:
                return [i, j]


def bfs(map: List[List[int]], c: int, cangowall: bool = True) -> int:
    """
        :param map: 0 denotes the place where you can go.
                    1 denotes the wall where you can't go, however, you can go using c power.
                    2 denotes the current location of robot.
                    3 denotes the location of treasure.
                    (*) when you go, you need to use 1 power.
        0 0 0 0 2 0 0 0 0 0
        0 0 0 1 1 1 1 0 0 0
        0 0 0 1 1 1 1 0 0 0
        0 0 0 1 1 1 1 0 0 0
        0 0 0 0 3 0 0 0 0 0

        :param c: the power used to break through the wall.
        :return: the minimum of total power.
    """

    # top, bottom, left, right
    H, W = len(map), len(map[0])
    visited = [[False for _ in range(W)] for _ in range(H)]
    start, goal = location(map, 2), location(map, 3)
    pmap = initpmap(map, c)
    # print2darray(pmap)

    dys = [-1, 1, 0, 0]
    dxs = [0, 0, -1, 1]

    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = True
    canpass = [0, 1] if cangowall else [0]

    while queue:
        ny, nx = queue.popleft()
        # print(f'ny={ny}, nx={nx}')
        for dy, dx in zip(dys, dxs):
            y = dy + ny
            x = dx + nx
            # print(f'y={y}, x={x}')
            if 0 <= y < H and 0 <= x < W and not visited[y][x]:
                if map[y][x] in canpass:
                    pmap[y][x] += pmap[ny][nx]
                    queue.append([y, x])
                    visited[y][x] = True
                elif map[y][x] == 3:
                    pmap[y][x] += pmap[ny][nx]
                    return pmap[y][x]


if __name__ == '__main__':
    map = [[0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
           [0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
           [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
           [0, 0, 0, 0, 3, 0, 0, 0, 0, 0]]
    answer = min(bfs(map, 2), bfs(map, 5, cangowall=False))
    print(answer)
