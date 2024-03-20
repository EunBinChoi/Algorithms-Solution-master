from typing import List


def split_dart_result(dartResult: str) -> List[str]:
    darts = []
    s = ""
    i = 0
    while i < len(dartResult):
        if dartResult[i:i + 2].isdigit():
            if s: darts.append(s)

            s = ""
            s += dartResult[i:i + 2]
            i += 1

        elif dartResult[i].isdigit():
            if s: darts.append(s)

            s = ""
            s += dartResult[i]

        elif dartResult[i] in ["S", "D", "T", "*", "#"]:
            s += dartResult[i]

        i += 1

    else:
        if s: darts.append(s)
    return darts


def get_score_with_area(s: str) -> int:
    if s == "S":
        return 1
    elif s == "D":
        return 2
    elif s == "T":
        return 3


def solution(dartResult: str) -> int:
    darts = split_dart_result(dartResult)
    scores = [0 for _ in range(len(darts))]
    special = [1 for _ in range(len(darts))]
    for i in range(len(darts)):
        if darts[i][0:2].isdigit():
            scores[i] = int(darts[i][0:2]) ** get_score_with_area(darts[i][2])
        elif darts[i][0].isdigit():
            scores[i] = int(darts[i][0]) ** get_score_with_area(darts[i][1])

        if "*" == darts[i][-1]:
            if i >= 1:
                if "*" == darts[i - 1][-1] and "*" == darts[i][-1]:
                    special[i - 1] = 2*2
                    special[i] *= 2
                elif "*" == darts[i][-1]:
                    special[i - 1] *= 2
                    special[i] *= 2
                else:
                    special[i] *= 2
            else:
                if "*" == darts[i][-1]:
                    special[i] *= 2

        elif "#" == darts[i][-1]:
            if i >= 1 and "#" == darts[i - 1][-1] and "*" == darts[i][-1]:
                special[i - 1] *= (-2)
                special[i] *= 2
            else:
                special[i] *= (-1)

    return sum([special[i] * scores[i] for i in range(len(darts))])


if __name__ == '__main__':
    print(solution("1S2D*3T")) # 37
    print(solution("1D2S#10S")) # 9
    print(solution("1D2S0T")) # 3
    print(solution("1S*2T*3S")) # 23
    print(solution("1D#2S*3S")) # 5
    print(solution("1T2D3D#")) # -4
    print(solution("1D2S3T*")) # 59
    print(solution("1S2D*3T*")) # 72 (1^1 * 2 + 2^2 * 4 + 3^3 * 2 == 2 + 16 + 54 == 72)
    print(solution("1S2D3T*")) # 63 (1^1 + 2^2 * 2 + 3^3 * 2)