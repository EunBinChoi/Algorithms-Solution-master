from typing import List


def solution(id_list: List[str], report: List[str], k: int) -> List[int]:
    dec_ed_cnt = {uid: 0 for uid in id_list}  # key: declared id, value: declared count
    dec_ed_id = {uid: [] for uid in id_list}  # key: declared id, value: declare id
    dec_id = {uid: [] for uid in id_list}  # key: declare id, value: declared id
    report_cnt = {uid: 0 for uid in id_list}  # key: declare id, value: report count

    for i in range(len(report)):
        report_sp = report[i].split(' ')
        if report_sp[1] not in dec_id[report_sp[0]]:
            dec_id[report_sp[0]].append(report_sp[1])
            dec_ed_id[report_sp[1]].append(report_sp[0])

    for key, values in dec_ed_id.items():
        for value in values:
            dec_ed_cnt[key] += 1

    for key, value in dec_ed_cnt.items():
        if value >= k:
            for dec_id in dec_ed_id[key]:
                report_cnt[dec_id] += 1

    answer = [0 for _ in id_list]
    for i in range(len(id_list)):
        answer[i] = report_cnt[id_list[i]]
    return answer