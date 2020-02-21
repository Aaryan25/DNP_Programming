"""
Chapter : 6
Problem : How Many Pieces Of Land?
Roll No : 10
"""

test = int(input())
no = [int(input()) for i in range(test)]
lst = []
for i in no:
    line = (i*(i-1)) // 2
    piece = (i*(i-1)*(i-2)*(i-3))//24 + line + 1
    lst.append(piece)
for i in lst:
    print(i)

"""
Output :-
4
1
2
3
4

1
2
4
8
"""
