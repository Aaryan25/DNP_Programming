"""
Chapter : 5
Problem : Primary Arithmatic
Roll No : 10
"""

tlist = []
lst = []
tno = []
while True:
	no = str(input())
	if no == "0 0":
		break
	else:
		lst = no.split(" ")
		tlist.append(lst)
tno = [[int(tlist[i][j]) for j in range(2)] for i in range(len(tlist))]

for i in range(len(tno)):
	count = 0
	carry = 0
	no1 = tno[i][0]
	no2 = tno[i][1]
	while no1 != 0 or no2 != 0: 
		temp = (no1%10) + (no2%10)
		if temp>=10:
			count += 1
			carry = 1 
		no1 = no1//10
		no2 = no2//10
	if count == 0:
		print("No carry operation.")
	else:
		print("{} carry operation.".format(count))

"""
Output :-
123 456
555 555
123 594
0 0

No carry operation.
3 carry operation.
1 carry operation.

"""
