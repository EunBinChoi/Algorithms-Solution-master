import sys
import copy
from typing import List


def input_data():
    _N, _M = map(int, sys.stdin.readline().split())

    _lst_stand = [[0, 0] for _ in range(_N)]
    _acc_sec = 0
    for _i in range(_N):
        _sec, _speed = map(int, input().split())

        _acc_sec += _sec
        _lst_stand[_i][0] = _acc_sec
        _lst_stand[_i][1] = _speed

    _lst_inspect = [[0, 0] for _ in range(_M)]
    _acc_sec_inspect = 0
    for _i in range(_M):
        _sec, _speed = map(int, input().split())

        _acc_sec_inspect += _sec
        _lst_inspect[_i][0] = _acc_sec_inspect
        _lst_inspect[_i][1] = _speed

    return _lst_stand, _lst_inspect


def solution_with_two_pointers(_lst_stand, _lst_inspect) -> int:
    """
    This is algorithm with two pointers where one is used for lst_section and the other is for lst_section_inspect
    :param _lst_stand: element -> [section length, limited speed for each section]
    :param _lst_inspect: element -> [section length to inspect, real operating speed for each section]
    :return: max difference between limited speed and real operating speed
            when real operating speed exceed the limited speed
    """
    _max_sub = 0
    i = 0
    j = 0
    while i < len(_lst_stand) and j < len(_lst_inspect):
        if _lst_stand[i][0] < _lst_inspect[j][0]:
            _max_sub = max(_max_sub, _lst_inspect[j][1] - _lst_stand[i][1])
            i += 1
        elif _lst_stand[i][0] > _lst_inspect[j][0]:
            _max_sub = max(_max_sub, _lst_inspect[j][1] - _lst_stand[i][1])
            j += 1
        else:
            _max_sub = max(_max_sub, _lst_inspect[j][1] - _lst_stand[i][1])
            i += 1
            j += 1
    return _max_sub


"""
:exception 생각해보기
2 3
50 90
50 100
20 30
29 30
51 99
"""
def solution_section_extension(_lst_stand, _lst_inspect) -> int:
    """
    This is algorithm with section extension when there are difference
                        between split section length and real operating section length
    :param _lst_stand: element -> [section length, limited speed for each section]
    :param _lst_inspect: element -> [section length to inspect, real operating speed for each section]
    :return: max difference between limited speed and real operating speed
            when real operating speed exceed the limited speed
    """
    i = 0
    j = 0
    _new_lst_stand_section = []
    _new_lst_stand_speed = []
    _new_lst_operating_speed = []
    while i < len(_lst_stand) and j < len(_lst_inspect):
        if _lst_stand[i][0] < _lst_inspect[j][0]:
            _new_lst_stand_section.append(_lst_stand[i][0])
            _new_lst_stand_speed.append(_lst_stand[i][1])
            _new_lst_operating_speed.append(_lst_inspect[j][1])
            i += 1

        elif _lst_stand[i][0] > _lst_inspect[j][0]:
            _new_lst_stand_section.append(_lst_inspect[j][0])
            _new_lst_stand_speed.append(_lst_stand[i][1])
            _new_lst_operating_speed.append(_lst_inspect[j][1])
            j += 1

        else:
            _new_lst_stand_section.append(_lst_stand[i][0])
            _new_lst_stand_speed.append(_lst_stand[i][1])
            _new_lst_operating_speed.append(_lst_inspect[j][1])
            i += 1
            j += 1

    # print(_new_lst_stand_section)
    # print(_new_lst_stand_speed)
    # print(_new_lst_operating_speed)

    max_differ = 0
    if len(_new_lst_stand_speed) == len(_new_lst_operating_speed):
        for s in range(len(_new_lst_stand_speed)):
            max_differ = max(max_differ, _new_lst_operating_speed[s] - _new_lst_stand_speed[s])
    return max_differ


if __name__ == '__main__':
    lst_stand, lst_inspect = input_data()
    # print(lst_section, lst_speed_lim)
    # print(lst_section_inspect, lst_speed_lim_inspect)

    max_sub = solution_with_two_pointers(lst_stand, lst_inspect)
    print(max_sub)

    max_sub = solution_section_extension(lst_stand, lst_inspect)
    print(max_sub)

