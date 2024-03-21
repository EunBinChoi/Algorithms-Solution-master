from typing import List, Dict
from itertools import product


def solution(users: List, emoticons: List) -> List:
    rate_list = [10, 20, 30, 40]
    rate_case = list(product(rate_list, repeat=len(emoticons)))
    tc_list = []

    for rc in rate_case:
        total = 0
        signup = 0
        for ur, up in users:
            ut = 0
            for r, e in zip(rc, emoticons):
                sale = e * (100 - r) / 100

                if r >= ur:
                    ut += sale

            if ut >= up:
                signup += 1
            else:
                total += ut

        tc_list.append([signup,total])

    sort_tc = sorted(tc_list, key=lambda k: (k[0], k[1]), reverse=True)
    return sort_tc[0]


if __name__ == '__main__':
    users = [[40, 10000], [25, 10000]]
    emoticons = [7000, 9000]
    print(solution(users, emoticons))

    users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
    emoticons = [1300, 1500, 1600, 4900]
    print(solution(users, emoticons))