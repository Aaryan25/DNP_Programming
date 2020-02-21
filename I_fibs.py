"""
Chapter : 6
Problem : How Many Fibs?
Roll No : 10
"""

nos = []
while True:
    line = str(input())
    if line == "0 0":
        break
    nos.append(line.split(" "))
lines = [[int(nos[i][j]) for j in range(len(nos[i]))] for i in range(len(nos))]
tcount = []
for i in range(len(lines)):
    fibs = [0, 1]
    count = 0
    while fibs[-1] <= lines[i][1]:
        fibs.append(fibs[-1] + fibs[len(fibs)-2])
    for j in fibs:
        if j >= lines[i][0] and j <= lines[i][1]:
            count += 1
    tcount.append(count)
for i in tcount:
    print(i)

"""
Output :-
10 100
1234567890 9876543210
0 0

5
4
"""