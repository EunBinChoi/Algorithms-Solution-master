from typing import List

def solution (data: List[List[int]], ext: str, val_ext: int, sort_by: str) -> List[List[int]]:
    m = {"code": 0, "date": 1, "maximum": 2, "remain": 3}

    ext_lst = [d for d in data if d[m[ext]] < val_ext]
    ext_lst.sort(key=lambda x: x[m[sort_by]])
    #print(ext_lst)
    return ext_lst


if __name__ == '__main__':
    data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]] # [code, date, maximum, remain]
    ext = "date" # "code", "date", "maximum", "remain"
    val_ext = 20300501
    sort_by = "remain" # "code", "date", "maximum", "remain"

    print(solution(data, ext, val_ext, sort_by))