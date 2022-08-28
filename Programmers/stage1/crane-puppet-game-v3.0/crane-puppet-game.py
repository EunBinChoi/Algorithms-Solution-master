from typing import List


def solution(board: List[List[int]], moves: List[int]) -> int:
    cols = list(map(lambda x: list(filter(lambda y: y > 0, x[::-1])), zip(*board)))
    stack = [0]
    answer = 0
    s = 0
    b = 0

    for m in moves:
        if cols[m - 1]:
            if (b := cols[m - 1].pop()) == (s := stack.pop()):
                answer += 2
            else:
                stack.extend([s, b])
    return answer


if __name__ == '__main__':
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]
    print(solution(board, moves))