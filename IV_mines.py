row = int(input())
col = int(input())
field=0
while row!=0 or col!=0:
	field += 1
	mat = [["0" for j in range(col+2)] for i in range(row+2)]
	solution = [[0 for j in range(col+2)] for i in range(row+2)]
	temp=[str(input()).split(" ") for i in range(row)]
	for r in range(1, row+1):
   	 for c in range(1, col+1):
   	     mat[r][c] = temp[r-1][c-1]

	for r in range(1, row+1):
		for c in range(1, col+1):
			if mat[r][c] == '*':
				solution[r-1][c-1] +=1
				solution[r-1][c] +=1
				solution[r-1][c+1] +=1
				solution[r][c-1] +=1
				solution[r][c+1] +=1
				solution[r+1][c-1] +=1
				solution[r+1][c] +=1
				solution[r+1][c+1] +=1
	print("\nField#",field)
	for r in range(1, row+1):
   	 for c in range(1, col+1):
   	     if mat[r][c] == '*':
   	         print("*", end=" ")
   	     else:
   	         print(solution[r][c], end=" ")
   	 print("")
   	 
	row = int(input())
	col = int(input())
	
"""
Output :-

4
4
* . . .
. . . .
. * . .
. . . .

Field# 1
* 1 0 0 
2 2 1 0 
1 * 1 0 
1 1 1 0 

3
5
* * . . .
. . . . .
. * . . .

Field# 2
* * 1 0 0 
3 3 2 0 0 
1 * 1 0 0 

0
0

"""

