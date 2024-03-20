from typing import List

def solution(board: List, h: int, w: int) -> int:
    n = len(board)
    count = 0
    dh, dw = [0, 1, -1, 0], [1, 0, 0, -1] # top, right, left, bottom
    for i in range(0, 4):
        h_check = h + dh[i]
        w_check = w + dw[i]
        if (0 <= h_check < n) and (0 <= w_check < n) and (board[h][w] == board[h_check][w_check]):
            count += 1
    return count


if __name__ == '__main__':
    #board = [["blue", "red", "orange", "red"],
    #         ["red", "red", "blue", "orange"],
    #         ["blue", "orange", "red", "red"],
    #         ["orange", "orange", "red", "blue"]]
    #h = 1
    #w = 1

    board = [["yellow", "green", "blue"], ["blue", "green", "yellow"], ["yellow", "blue", "blue"]]
    h = 0
    w = 1
    print(solution(board, h, w))