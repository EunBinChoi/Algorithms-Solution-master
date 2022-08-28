from typing import List


def transpose(board: List[List[int]]) -> List[List[int]]:
    return [[board[j][i] for j in range(len(board[0]))][::-1] for i in range(len(board))]


def score(basket: List[int]) -> int:
    if len(basket) > 1 and basket[-1] == basket[-2]:
        del basket[-1], basket[-1]
        return 2
    else:
        return 0


def solution(board: List[List[int]], moves: List[int]) -> int:
    boardT = transpose(board)
    basket = []
    total = 0
    while moves:
        move = moves.pop(0)

        if boardT[move - 1] and boardT[move - 1][-1]:
            basket.append(boardT[move - 1][-1])
            del boardT[move - 1][-1]

        else:
            while boardT[move - 1] and boardT[move - 1][-1] == 0:
                del boardT[move - 1][-1]

            if boardT[move - 1] and boardT[move - 1][-1]:
                basket.append(boardT[move - 1][-1])
                del boardT[move - 1][-1]

        total += score(basket)
    return total


if __name__ == '__main__':
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]
    print(solution(board, moves))