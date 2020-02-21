"""
Chapter : 4
Problem : Stacks Of Flapjacks
Roll No : 10
"""
while True:
    line = str(input())
    if line == "":
        break
    count = num = flip = 0
    flips = []
    cake = [int(i) for i in line if i != " "]
    rev_cake = cake[-1::-1]
    for i in range(len(cake)):
        max = rev_cake[i]
        pos = 0
        for j in range(i+1,len(cake)):
            if max < rev_cake[j]:
                max = rev_cake[j]
                pos = j
        if pos:
            if pos != (len(cake)-1):
                temp = [i for i in rev_cake]
                x = pos
                j = len(cake)
                while x < len(cake):
                    rev_cake[x] = temp[j]
                    x += 1
                    j -= 1
                    flip += 1
                    flips.append(pos+1)
            temp = [i for i in rev_cake]
            x = i
            j = len(cake)-1
            while x < len(cake):
                rev_cake[x] = temp[j]
                x += 1
                j -= 1
                flip += 1
                flips.append (i + 1)
    for i in cake:
        print(i, end=" ")
    print("")
    for i in list(set(flips)):
        print(i, end=" ")
    print("0")

"""
Output :-
1 2 3 4 5
1 2 3 4 5 
0

5 4 3 2 1
5 4 3 2 1 
1 0

5 1 2 3 4
5 1 2 3 4 
1 2 0
"""