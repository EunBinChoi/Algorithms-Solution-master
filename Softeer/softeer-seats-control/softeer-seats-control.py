import sys
from typing import Tuple, List, Dict


def input_data() -> Tuple:
    N, M, Q = [int(s) for s in sys.stdin.readline().split()]

    work_li = []
    for i in range(Q):
        In, ID = input().split()
        ID = int(ID)
        work_li.append([In, ID])
    return N, M, Q, work_li


def print_2d_array(arr2d: List[List]):
    for i in range(len(arr2d)):
        for j in range(len(arr2d[0])):
            print(arr2d[i][j], end=" ")
        print()


def get_index_of_possible_location(N: int, M: int, seat_li: List[List], current_index: Dict) -> List:
    # print_2d_array(seat_li)
    in_list = list(current_index.values())
    # print(in_list)
    if not in_list:
        return [1, 1]
    else:
        seat_max = 0
        seat_loc = [-1, -1]
        for i in range(1, N+1):
            for j in range(1, M+1):
                safty_min = 100
                safty_loc = [-1, -1]

                # print(f"{i}, {j}")
                if seat_li[i][j] == 0 and seat_li[i-1][j] == 0 and seat_li[i+1][j] == 0 \
                        and seat_li[i][j-1] == 0 and seat_li[i][j+1] == 0:
                    checker = False
                    for k in range(len(in_list)):  # current state index
                        d = ((in_list[k][0] - i) ** 2 + (in_list[k][1] - j) ** 2) ** 0.5
                        # print(f"{i}, {j} => {d}")
                        if d == 1:
                            checker = False
                            break  # 상하좌우

                        if safty_min > d:
                            safty_min = d
                            safty_loc = [i, j]
                            checker = True

                    if checker and seat_max < safty_min:
                        seat_max = safty_min
                        seat_loc = [safty_loc[0], safty_loc[1]]
                    # print(f"{seat_max}, {seat_loc}")
        return seat_loc


def solution():
    N, M, Q, work_li = input_data()
    seat_li = [[0] * (M+2) for _ in range(N+2)]
    current_state = {}  # key: id, value: in (1), in-out (2)
    current_index = {}  # key: id, value: location (list)
    for i in range(len(work_li)):
        status, pid = work_li[i]
        if status == "In":
            if pid in current_state.keys():
                if current_state[pid] == 1:
                    print(f"{pid} already seated.")
                elif current_state[pid] == 2:
                    print(f"{pid} already ate lunch.")

            else:
                idx = get_index_of_possible_location(N, M, seat_li, current_index)
                if idx == [-1, -1]:
                    print(f"There are no more seats.")

                else:
                    seat_li[idx[0]][idx[1]] = pid
                    current_state[pid] = 1
                    current_index[pid] = [idx[0], idx[1]]
                    print(f"{pid} gets the seat ({idx[0]}, {idx[1]}).")

        else:  # "Out"
            if pid not in current_state.keys():
                print(f"{pid} didn't eat lunch.")
            elif current_state[pid] == 2:
                print(f"{pid} already left seat.")
            else:
                current_state[pid] = 2
                x, y = current_index[pid]
                seat_li[x][y] = 0
                del current_index[pid]
                print(f"{pid} leaves from the seat ({x}, {y}).")


if __name__ == '__main__':
    solution()