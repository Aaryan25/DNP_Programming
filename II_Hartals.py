def check(n, p, hartals):
    lost = 0
    for i in range(1, n+1):
        if i % 7 == 6 or i % 7 == 0:
            pass
        else:
            for j in range(p):
                if i % hartals[j] == 0:
                    lost += 1
                    break
    return lost

t = int(input())
t_lost = []
while t > 0:
    n = int(input())
    p = int(input())
    hartals = [int(input()) for i in range(p)]

    t_lost.append(check(n, p, hartals))
    t -= 1

for i in t_lost:
    print(i)
