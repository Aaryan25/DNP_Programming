"""
Chapter : 5
Problem : multiplication Game
Roll No : 10
"""

t = (2,9)
n = []
while True:
	no = str(input()) 
	if no == "":
		break
	else:
		n.append(int(no))

for i in range(len(n)):
	temp = 1
	win = 1
	count = 0 
	while temp<n[i]:
		if win == 1:
			temp = temp*max(t)
			win = 0
		else:
			temp = temp*min(t)
			win = 1
		count += 1
	if count%2:
		print("Stan wins.")
	else:
		print("Ollie wins.")
	
"""
Output :-
162
17
34012226

Stan wins.
Ollie wins.
Stan wins.

"""
