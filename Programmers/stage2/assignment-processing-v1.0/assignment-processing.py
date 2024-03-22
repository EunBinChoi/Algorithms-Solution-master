from typing import List
from datetime import timedelta


def solution(plans: List) -> List:
    plans.sort(key=lambda x: x[1], reverse=True)

    done = []
    pause = []

    """
    1) 현재 계획한 과목이 있는 경우
        1) 현재 과목을 끝내지 못하고 다음 과목을 시작하는 경우
        2) 현재 과목을 끝내고 다음 과목을 시작하는 경우
        - 현재 과목을 끝내고도 시간이 남아 중지된 과제를 하는 경우

    2) 현재 계획한 과목이 없는 경우 중지된 과제를 모두 수행함
    """

    while plans:
        ni, si, pi = plans.pop()
        hi, mi = si.split(':')
        si_td = timedelta(hours=int(hi), minutes=int(mi))
        pi_td = timedelta(minutes=int(pi))
        ei_td = si_td + pi_td

        # 1)
        if plans:
            nj, sj, pj = plans[-1]
            hj, mj = sj.split(':')
            sj_td = timedelta(hours=int(hj), minutes=int(mj))
            diff = (sj_td-ei_td).total_seconds().__int__()

            # 1) - 1)
            if diff < 0:
                pause.append([ni, -diff])

            # 1) - 2)
            else:
                done.append(ni)

                while pause and diff:
                    pn, pt = pause.pop()

                    if pt >= diff:
                        pt -= diff
                        diff = 0

                        if pt == 0: done.append(pn)
                        else: pause.append([pn, pt])

                    else:
                        diff -= pt
                        done.append(pn)

        # 2)
        else:
            done.append(ni)

            if pause:
                name = [n for n, p in pause][::-1]
                done.extend(name)

    return done


if __name__ == '__main__':
    plans = [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]
    print(solution(plans))

    plans = [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
    print(solution(plans))