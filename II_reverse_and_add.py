"""
Chapter : 5
Problem : Reverse and Add
Roll No : 10
"""

t = int(input())
lst = [str(input()) for i in range(t)]

for i in range(len(lst)):
	string = lst[i]
	rev = string[-1::-1]
	count = 0
	while string != rev:
		count += 1
		check = int(string) + int(rev)
		if str(check) == (str(check)[-1::-1]):
			print(str(count) + " " + str(check))
			break
		else:
			string = str(check)
			rev = (str(check)[-1::-1])
		if count>1000:
			break
		if check = 4294967295:
			break

"""
Output :-
3
195
265
750

4 9339
5 45254
3 6666

"""
