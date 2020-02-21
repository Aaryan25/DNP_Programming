"""
Chapter : 2
Problem : Contest Scoreboard
Roll No   :
"""
n_case = int(input())
_ = input()
for cdx in range(n_case):
    contestants = {}
    while 1:
        try:
            record = input().split()
            if not len(record):
                break
            contestant_id = int(record[0])
            problem_id = int(record[1]) - 1
            sol_time = int(record[2])
            state = record[3]

            if contestant_id not in contestants.keys():
                contestants[contestant_id] = [None] * 9

            if contestants[contestant_id][problem_id] is None:
                if state in ('R', 'U', 'E'):
                    contestants[contestant_id][problem_id] = 0
                elif state == 'I':
                    contestants[contestant_id][problem_id] = -1
                elif state == 'C':
                    contestants[contestant_id][problem_id] = sol_time
            elif contestants[contestant_id][problem_id] > 0:
                continue
            elif contestants[contestant_id][problem_id] <= 0:
                if state == 'I':
                    contestants[contestant_id][problem_id] -= 1
                elif state == 'C':
                    contestants[contestant_id][problem_id] = (
abs(contestants[contestant_id][problem_id]) * 20 + sol_time)

        except (EOFError):
            break

    rank = []
    for k, times in contestants.items():
        cnt, score = 0, 0
        for t in times:
            if t and t > 0:
                cnt += 1
                score += t
        rank.append((k, cnt, score))

    rank.sort(key=lambda x: (-x[1], x[2], x[0]))

    if cdx:
        print()
    for uid, cnt, score in rank:
        print("{} {} {}".format(uid, cnt, score))
        
        
"""
Output :-
1

1 2 10 I
3 1 11 C
1 2 19 R
1 2 21 C
1 1 25 C

1 2 66
3 1 11

"""

