from typing import List, Dict

"""
그래프 순회
"""


def solution(edges: List) -> List:
    node_set = set()
    for edge in edges:
        for e in edge:
            node_set.add(e)

    graph_keys = list(node_set)
    graph_vals = [[] for _ in range(0, len(node_set))]
    graph_dict = dict(zip(graph_keys, graph_vals))

    for s, e in edges:
        graph_dict[s].append(e)

    # count in, out edges for each node to get first node
    in_edges = dict(zip(graph_keys, [0] * len(node_set)))
    out_edges = dict(zip(graph_keys, [0] * len(node_set)))
    for k, values in graph_dict.items():
        out_edges[k] = len(values)
        for v in values:
            in_edges[v] += 1

    first_node = 0
    donut, stick, eight = 0, 0, 0
    for k, ie, oe in zip(in_edges.keys(), in_edges.values(), out_edges.values()):
        if oe >= 2 and ie == 0: first_node = k

    queue = [first_node]
    visited = dict(zip(graph_keys, [False] * len(node_set)))

    while queue:
        node = queue.pop()

        if not visited[node]:
            visited[node] = True

            if out_edges[node] == 0: stick += 1
            elif in_edges[node] >= 2 and out_edges[node] >= 2: eight += 1;
            queue.extend(graph_dict[node])

    donut = out_edges[first_node]-stick-eight
    return [first_node, donut, stick, eight]



if __name__ == '__main__':
    edges = [[2, 3], [4, 3], [1, 1], [2, 1]] # max: 4
    print(solution(edges))

    edges = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]  # max: 11, edge: 15
    print(solution(edges))

    edges = [[1, 12], [8, 3], [12, 7], [7, 11], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8], [4, 11], [4, 8]]
    print(solution(edges))

    edges = [[4, 11], [1, 12], [8, 3], [12, 7], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]
    print(solution(edges))
