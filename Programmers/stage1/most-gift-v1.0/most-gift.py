from typing import List, Dict

def solution(friends: List[str], gifts: List[str]) -> int:
    tbl = {(A, B): 0 for A in friends for B in friends if A != B}
    idx = {friend: 0 for friend in friends}
    ans = {friend: 0 for friend in friends}

    # init
    for gift in gifts:
        A, B = gift.split()
        tbl[A,B]+=1
        idx[A]+=1
        idx[B]-=1

    print(tbl)
    print(idx)
    # solution
    for A, B in tbl.keys():
        v1 = tbl[(A,B)]
        v2 = tbl[(B,A)]

        if v1 != 0 and v1 > v2:
            ans[A]+=1

        elif v1 == v2 and idx[A] > idx[B]:
            ans[A]+=1

    return max(ans.values())


if __name__ == '__main__':
    #friends = ["muzi", "ryan", "frodo", "neo"]
    #gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

    #friends = ["joy", "brad", "alessandro", "conan", "david"]
    #gifts = ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]

    friends = ["a", "b", "c"]
    gifts = ["a b", "b a", "c a", "a c", "a c", "c a"]
    print(solution(friends, gifts))