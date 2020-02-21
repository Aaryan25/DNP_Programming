"""
Chapter : 5
Problem : One's
Roll No : 10
"""

lst = []
while True:
	no = str(input()) 
	if no == "":
		break
	else:
		lst.append(no)
		
for i in range(len(lst)):
	if int(lst[i])%2 == 0 or int(lst[i])%5 == 0:
		pass
	else:
		count = 1
		no1 = "1"
		while int(no1)%int(lst[i]) != 0:
			no1 = str(no1) + "1"
			count += 1
		print(count)
		
"""
Output :- 
3
7
9901

3
6
12

"""
