def solution(dartResult: str) -> str:
    point = []
    answer = []
    dartResult = dartResult.replace('10','k')
    point = ['10' if i == 'k' else i for i in dartResult]
    print(point)

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
    return sum(answer)


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