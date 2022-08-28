def solution(dartResult: str) -> str:
    dart = {'S': 1, 'D': 2, 'T': 3}
    scores = []
    n = 0

    for i, d in enumerate(dartResult):
        if d in dart:
            scores.append(int(dartResult[n:i])**dart[d])
        if d == "*":
            scores[-2:] = [x*2 for x in scores[-2:]]
        if d == "#":
            scores[-1] = (-1)*scores[-1]
        if not (d.isnumeric()):
            n = i+1

    return sum(scores)


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