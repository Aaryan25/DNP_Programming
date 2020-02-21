"""
Chapter : 4
Problem : Shoemaker’s Problem
Roll No : 10
"""

class shoe:
    def __init__(self,id,day,panalty):
        self.id = id
        self.day = day
        self.panalty = panalty

    def __lt__(self, other):
        return self.day * other.panalty < other.day * self.panalty

    def __repr__(self):
        return str(self.id)

n = int(input())
jobs = []

while n > 0:
    job = int(input())
    for i in range(job):
        line = [int(x) for x in str(input()).split()]
        jobs.append(shoe(1 + i, line[0], line[1]))
    print(' '.join([str(e) for e in sorted(jobs)]))
    n -= 1

"""
Output :-
1
4
3 4
1 1000
2 2
5 5

2 1 3 4

"""