from typing import List


def solution(n: int, left: int, right: int) -> List[int]:
    arr2d = [0] * n
    arr1d = []
    arr = [i + 1 for i in range(n)]

    for i in range(n):
        arr[:i] = [arr[i]] * len(arr[:i])
        arr2d[i] = arr.copy()

    for i in range(n):
        arr1d.extend(arr2d[i])

    print(arr2d)
    print(arr1d)
    return arr1d[left:right + 1]