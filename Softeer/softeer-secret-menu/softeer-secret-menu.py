import sys


def input_data() -> tuple:
    M, N, K = tuple([int(s) for s in sys.stdin.readline().split()])
    secret = sys.stdin.readline().strip().replace(' ', '')
    user = sys.stdin.readline().strip().replace(' ', '')
    return M, N, K, secret, user


"""
반례
5 10 5
1 2 3 4 5
1 1 2 3 4 5 1 2 3 4 => 1, (1, 2, 3, 4, 5), 1, 2, 3, 4 => secret
"""
def solution() -> str:
    M, N, K, secret, user = input_data()
    answer = "normal"

    # if secret in user:
    #     answer = "secret"

    if M > N: return "normal"
    elif M == N: return "secret" if secret == user else "normal"

    i = 0
    while i < N - M + 1:
        cur_user = user[i:i+M]
        if cur_user == secret:
            return "secret"
        i += 1
    return answer


if __name__ == '__main__':
    print(solution())


