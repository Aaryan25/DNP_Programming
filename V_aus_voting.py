case = int(input())
tname = []
while case>0:
    n = int(input())
    names = [str(input()) for i in range(n)]
    voting = []
    calc = [0 for i in range(n)]

    while True:
        v = []
        vote = str(input())
        if vote == "":
            break
        else:
            v = vote.split(" ")
            voting.append(v)

    count = 0
    for i in range(len(voting)):
        for j in range(n):
            if voting[i][count] == str(j+1):
                calc[j] += 1
    avg = max(calc) / len(voting)

    if avg > 0.5:
        break
    else:
        for i in range (len (voting)):
            if voting[i][count] == str (calc.index (min (calc)) + 1):
                count += 1
                for j in range (n):
                    if voting[i][count] == str (j + 1):
                        calc[j] += 1
                        break
                break
    win = calc.index(max(calc))
    tname.append(names[win])
    case -= 1
for i in tname:
    print(i)
    
"""
Output :-

1
3 
John Doe
Jane Smith
Jane Austen
1 2 3
2 1 3
2 3 1
1 2 3
3 1 2

John Doe

"""
