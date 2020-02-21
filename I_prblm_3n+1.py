"""
Chapter : 1
Problem : 3n+1
Roll No : 10 

"""
while True:
	no = str(input(""))
	if no == "":
		break
	else:
		t_count=1
		no1,no2=no.split(" ")
		no1 = int(no1)
		no2 = int(no2)
		x=[no1,no2]
		while no1<=no2:
			i=no1
			count=1
			while i!=1:
				if i % 2:
					i = 3 * i + 1
				else:
					i = i // 2
				count = count + 1
				if count>t_count:
					t_count=count
			no1=no1+1
		x.append(t_count)
		for i in x:
			print(i,end=" ")
		print("")
"""
INPUT  : 1 10
OUTPUT : 1 10 20 
INPUT  : 100 200
OUTPUT : 100 200 125 
INPUT  : 201 210
OUTPUT : 201 210 89 
INPUT  : 900 1000
OUTPUT : 900 1000 174
 
"""
		
