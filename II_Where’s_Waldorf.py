m = int(input())
n = int(input())

samp = [list(str(input()).lower()) for i in range(m)]
grid = [['0' for i in range(n+1)] for j in range(m+1)]
grid = [[samp[i-1][j-1] for j in range(1,n+1)] for i in range(1,m+1)]

no = int(input())
words = [str(input()).lower() for i in range(no)]
flag = 0 
direction = [[0,1],[1,0],[1,1],[-1,0],[-1,1],[-1,-1],[0,-1],[1,-1]]

for k in range(len(words)):
	flag = 0
	for row in range(m):
		for col in range(n):
			temp = 0
			if grid[row][col] == words[k][temp]:
				temp += 1
				i = main_x = row
				j = main_y = col
				for l in range(8):
					x = direction[l][0]
					y = direction[l][1]
					if words[k][temp] == grid[i+x][j+y]:
						i = i+x
						j = j+y
						for le in range(len(words[k])-3):	
							i = i+x
							j = j+y
							temp += 1
							if temp == len(words[k]):
								if flag == 1:
									print(main_x+1,main_y+1)
									break
							elif words[k][temp] == grid[i][j]:
								flag = 1
							else:
								break
						if flag == 1:
								print(main_x+1,main_y+1)
								break
				if flag == 1:
						break
		if flag == 1:
			break	     
                        	
"""
Output :-
1

8
11
abcDEFGhigg
hEbkWaldorf
FtyAwaldORm
FtsimrLqsrc
byoArbeDeyv
Klcbqwikomk
strEBGadhrb
yUiqlxcnBjf
4
Waldorf
Bambi
Betty
Dagbert

2 5
2 3
1 2
7 8

"""                 

