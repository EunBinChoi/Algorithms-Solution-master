def solution(new_id: str) -> str:
    # step 1 ~ 2
    inc_chars = ['-', '_', '.']
    sug_id = []
    for s in new_id.lower():
        if s in inc_chars or s.isalnum():
            sug_id.append(s)
    print('step 1 ~ 2', "".join(sug_id))

    # step 3
    """
    오류 생긴 이유: '...' -> '.'로 바꾸면 그만큼 sug_id 길이가 달라지기 때문에 인덱스가 정확하지 않음
    """
    dot_cnt = 0
    dot_index = []  # [start, end]
    tmp = [-1, -1]
    sug_id_copy = sug_id.copy()
    i = 0
    while sug_id_copy:
        s = sug_id_copy.pop(0)
        if s == '.':
            dot_cnt += 1
            if dot_cnt == 1:
                tmp[0] = i # start
            elif dot_cnt >= 2:
                tmp[1] = i # end
        else:
            if tmp[0] != -1 and tmp[1] != -1:
                dot_index.append(tmp)
            dot_cnt = 0
            tmp = [-1, -1]  # [start, end]
        i += 1
    if tmp[0] != -1 and tmp[1] != -1:
        dot_index.append(tmp)

    """
    삭제된 만큼 인덱스도 줄이기 위해 아래와 같은 코드를 작성
    """
    remove = 0
    for s, e in dot_index:
        print(s,e)
        sug_id[s-remove:e+1-remove] = '.'
        remove += e-s
    print('step 3', "".join(sug_id))

    # step 4
    if sug_id and sug_id[0] == '.':
        sug_id = sug_id[1:]
    if sug_id and sug_id[-1] == '.':
        sug_id = sug_id[:-1]
    print('step 4', "".join(sug_id))

    # step 5
    if not sug_id:
        sug_id = ['a']
    print('step 5', "".join(sug_id))

    # step 6
    if len(sug_id) >= 16:
        sug_id = sug_id[:15]
        if sug_id[-1] == '.':
            sug_id = sug_id[:-1]
    print('step 6', "".join(sug_id))

    # step 7
    if sug_id and len(sug_id) <= 2:
        sug_id += sug_id[-1] * (3 - len(sug_id))
    print('step 7', "".join(sug_id))

    return "".join(sug_id)


if __name__ == '__main__':
    new_id = "...!@BaT#*..y.abcdefghijklm"
    # new_id = "z-+.^."
    # new_id = "=.="
    # new_id = "123_.def"
    # new_id = "abcdefghijklmn.p"
    # new_id = "a...............a........."
    print(solution(new_id))