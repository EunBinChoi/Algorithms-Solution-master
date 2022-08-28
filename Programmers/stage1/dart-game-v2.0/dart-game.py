import re


def solution(dartResult: str) -> int:
    score = {'S': 1, 'D': 2, 'T': 3}
    bouns = {'': 1, '*': 2, '#': -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** score[dart[i][1]] * bouns[dart[i][2]]

    return sum(dart)


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