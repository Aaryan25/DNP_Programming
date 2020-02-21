"""
Chapter : 6
Problem : Counting
Roll No : 10
"""

no = []
while True:
    n = str(input())
    if n == "":
        break
    no.append(int(n))
lst = [2, 5, 13]
for i in range(1,1000):
    n = 2*lst[-1] + lst[-2] + lst[-3]
    lst.append(n)
for i in no:
    print(lst[i-1])

"""
Output :-
2
3

5
13
"""