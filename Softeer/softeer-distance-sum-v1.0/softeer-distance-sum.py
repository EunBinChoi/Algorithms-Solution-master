import sys
from typing import List, Tuple, Dict
from collections import defaultdict
import heapq


"""
시간 제한 초과
문제를 제대로 읽지 않음
해당 문제에서는 node의 개수가 N개, edge의 개수가 N-1개라고 말함
하지만 dijkstra는 그래프의 최단경로를 구하는 것으로 edge의 개수가 N-1개 아닐 수 있음
dijkstra with adjacency list's time complexity: O(|E|log|V|) == O(|E|log|E|) 
dijkstra with adjacency array's time complexity: O(|V|^2)
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


def dijkstra(graph: Dict, start: int) -> Dict[int, float]:
    """
    This is dijkstra algorithm using adjacency list.
    :param graph: graph using adjacency list
    :param start: starting node to search
    :return: distance between starting node and node (starting node ---- distance ---- node)
            returns dictionary which consist of distance for number of node {node: distance}
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작 하기 위함.

    while queue:  # queue에 남아 있는 노드가 없으면 끝
        current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.

        if distances[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음.
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
            if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신함.
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입함.

    return distances


def solution() -> None:
    """
    This is solution which calls each method according to algorithms.
    :return: print the sum of the shortest distances between starting node and node
    """
    N, x, y, t = input_data()
    graph = make_graph(N, x, y, t)
    print(graph)
    nodes = sorted(graph.keys())
    for node in nodes:
        print(int(sum(dijkstra(graph, node).values())))


if __name__ == '__main__':
    solution()
