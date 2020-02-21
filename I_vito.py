"""
Chapter : 4
Problem : Vito's Family
Roll No : 10
"""

n = int(input())
lst = []
while n>0:
	line = str(input())
	if line == "":
		break
	else:
		total = 0
		no = [int(i) for i in line if i != " "]
		for i in range(1,len(no)):
			for j in range(i,len(no)):
				if no[i]>no[j]:
					temp=no[i]
					no[i]=no[j]
					no[j]=temp
		if no[0]%2:
			avg = no[(len(no)//2)]
			for i in range(1,len(no)):
				total = total + abs(no[i]-avg)
		else:
			avg = (no[(len(no)//2)] + no[(len(no)//2) + 1] ) //2
			for i in range(1,len(no)):
				total = total + abs(no[i]-avg)
		lst.append(total)
	n=n-1
	
for i in lst:
	print(i)
	
"""
Output :-
2

2 2 4
3 2 6 4

2
4

"""
