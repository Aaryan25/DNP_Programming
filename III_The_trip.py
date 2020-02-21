n=int(input())
total_lst=[]

while n!=0:
	lst=[float(input()) for i in range(n)]
	avg=sum(lst)/n

	p_diff=n_diff=0.0

	for i in lst:
		if i>=avg:
			p_diff=p_diff+round((i-avg),2)
		else:
			n_diff=n_diff+round((avg-i),2)

	min_diff=0.0
	
	if p_diff>n_diff:
		min_diff=n_diff
	else:
		min_diff=p_diff
	
	total_lst.append(min_diff)
	n=int(input())

for i in total_lst:
	print("$",i)
	
"""
Output :-

3
10.00
20.00
30.00
4
15.00
15.01
3.00
3.01
0

$ 10.0
$ 11.99

"""
