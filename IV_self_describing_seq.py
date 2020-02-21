"""
Chapter : 6
Problem : Self-describing Sequence
Roll No : 10
"""

def findGolomb(n):
    if n == 1:
        return 1
    return 1 + findGolomb(n - findGolomb(findGolomb(n - 1)))
def generator():
    gen = (findGolomb(i) for i in range(1, 20))
    return gen
no = []
while True:
    n = int(input())
    if n == 0:
        break
    no.append(n)

for i in no:
    count = 0
    gen = generator()
    for j in gen:
        count += 1
        if count == i:
            print(j)
            break

"""
Output :-
100
9999
123456
1000000000
0

21
356
1684
438744
"""