n = int(input())
word = [str(input()) for i in range(n)]
tencrypt = []
while True:
	encrypt = []
	msg = str(input())
	if msg == "":
		break
	encrypt = msg.split(" ")
	length=len(encrypt)
	tencrypt.append(encrypt)
lst = []
lst1 = []
d = {}
for i in range(len(tencrypt)):
	for j in range(len(tencrypt[i])):
		for k in word:
			if len(k) == len(tencrypt[i][j]):
				if k in lst or tencrypt[i][j] in lst1:
					pass
				else:
					lst.append(k)		
					lst1.append(tencrypt[i][j])		
					for char in range(len(k)):
						if k[char] in d:
							pass
						else:
							d[k[char]] = tencrypt[i][j][char]
flist=[]
for i in range(len(tencrypt)):
	for j in range(len(tencrypt[i])):
		string=""
		for k in range(len(tencrypt[i][j])):
			for key,value in d.items():
				if tencrypt[i][j][k] == value:
					string +=key 
		flist.append(string)
		if string == "":
			flist.append(tencrypt[i][j])
for j in range(len(flist)):
	if flist[j] in word:
		print(flist[j],end=" ")
	else:
		print("*"*len(flist[j]),end=" ")
	if j==length-1:
		print("")
		
print("\n")
