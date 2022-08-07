import sys
from typing import List, Tuple, Dict
from collections import defaultdict


"""
Test Case 01-12 오류 ... 왜 나는지 모르겠음 😭
=> 가장 아래 코드를 수정함.
=> N: 1일 때 0이 나와야하는데 아무것도 안 나와서 오류난 것임.
"""
"""
node의 개수가 N개, edge의 개수가 N-1개 (***)
O(N)
"""
"""
7  
1 2 5  
1 3 2  
1 4 8  
3 5 4  
3 6 1  
4 7 6  
"""
def input_data() -> Tuple:
    """
    This is method for user to input data with console.
    N: the number of nodes
    x, y: number of nodes
    t: time for node to communicate
    :return: N, x, y, t
    """
    N = int(sys.stdin.readline().strip())
    x = [0 for _ in range(1, N)]
    y = [0 for _ in range(1, N)]
    t = [0 for _ in range(1, N)]
    for i in range(N-1):
        x[i], y[i], t[i] = tuple(map(int, sys.stdin.readline().split()))

    return N, x, y, t


def make_graph(N: int, x: List, y: List, t: List) -> Dict[int, Dict]:
    """
    This is method for making adjacency list using x, y, t of which the number is N - 1.
    :param N: the number of nodes
    :param x: number of nodes
    :param y: number of nodes
    :param t: time for node to communicate
    :return: adjacency list
    """
    graph = defaultdict(dict)
    for i in range(N-1):
        if graph[x[i]]:
            graph[x[i]].update({y[i]: t[i]})
        else:
            graph[x[i]] = {y[i]: t[i]}

        if graph[y[i]]:
            graph[y[i]].update({x[i]: t[i]})
        else:
            graph[y[i]] = {x[i]: t[i]}

    return graph


def dfs1(current: int, parent: int) -> None:
    """
    This is method for calculating subtree size and sum of distance.
    Only able to compute the sum of distance for first node because of bottom-up approach.
    :param current: number of current node
    :param parent:  number of parent node
    :return: None
    """
    global graph, subtreeSize
    subtreeSize[current] = 1 # subtreeSize including current node
    for child, cost in graph[current].items():
        if parent != child:
            dfs1(child, current) # bottom - up
            subtreeSize[current] += subtreeSize[child]
            subtreeDistSum[current] += subtreeDistSum[child] + cost * subtreeSize[child]
    return


def dfs2(current: int, parent: int) -> None:
    """
    This is method for calculating the sum of distance with the other node using the first node.
    :param current: number of current node
    :param parent:  number of parent node
    :return: None
    """
    global graph, subtreeSize, N
    for child, cost in graph[current].items():
        if parent != child:
            subtreeDistSum[child] = subtreeDistSum[current] + cost * (N - 2*subtreeSize[child])
            dfs2(child, current) # propagate to bottom (top - down)
    return


if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 7)  # 파이썬에서 recursion의 개수를 제한해두었는데 이를 10^6까지 가능하도록 함

    N, x, y, t = input_data()
    graph = make_graph(N, x, y, t)
    nodes = sorted(graph.keys())

    subtreeSize = defaultdict(int)
    subtreeDistSum = defaultdict(int)

    dfs1(1, 1)
    dfs2(1, 1)

    """
    for node in nodes:
        print(subtreeDistSum[node])

    """
    """
    => 수정
    """
    for i in range(1, N+1):
        print(subtreeDistSum[i])