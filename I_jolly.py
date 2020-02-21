
n=int(input("Enter How Many No You Want :- "))
no=[int(input("Enter No. :- ")) for i in range(n)]

def check():
    lst=[]
    for i in range(len(no)-1):
        value=abs(no[i]-no[i+1])
        if value==0 or value>len(no)-1 or value in lst:
            return False
        lst.append(value)
    return True

print("Jolly" if check() else "Not Jolly")