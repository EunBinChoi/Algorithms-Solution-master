def solution(new_id: str) -> str:
    # step 1 ~ 2
    inc_chars = ['-', '_', '.']
    sug_id = []
    for s in new_id.lower():
        if s in inc_chars or s.isalnum():
            sug_id.append(s)
    print('step 1 ~ 2', "".join(sug_id))

    # step 3
    while '..' in "".join(sug_id):
        sug_id = list("".join(sug_id).replace('..', '.'))
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