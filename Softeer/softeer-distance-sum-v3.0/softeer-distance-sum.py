import sys
from typing import List, Tuple, Dict
from collections import defaultdict

"""
채점 결과 성공 ...
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

class Node:
    def __init__(self, num, cost):
        self.__num = num
        self.__cost = cost

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        self.__num = num

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost):
        self.__cost = cost

    def __str__(self):
        return "[{0}] num = {1}, cost = {2}".format(self.__class__.__name__, self.__num, self.__cost)


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
    for i in range(len(adj[current])):
        child = adj[current][i].num
        cost = adj[current][i].cost

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
    for i in range(len(adj[current])):
        child = adj[current][i].num
        cost = adj[current][i].cost

        if parent != child:
            subtreeDistSum[child] = subtreeDistSum[current] + cost * (N - 2*subtreeSize[child])
            dfs2(child, current) # propagate to bottom (top - down)
    return


if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 6)  # 파이썬에서 recursion의 개수를 제한해두었는데 이를 10^6까지 가능하도록 함

    ##################### input data #####################
    N = int(sys.stdin.readline().strip())
    adj = [[] for _ in range(N + 1)]
    subtreeSize = [0 for _ in range(N + 1)]
    subtreeDistSum = [0 for _ in range(N + 1)]
    
    for i in range(1, N):
        s, e, c = tuple(map(int, sys.stdin.readline().split()))
        adj[s].append(Node(e, c))
        adj[e].append(Node(s, c))

    dfs1(1, 1)
    dfs2(1, 1)
    # print(subtreeSize)
    # print(subtreeDistSum)

    for i in range(1, N+1):
        print(subtreeDistSum[i])


