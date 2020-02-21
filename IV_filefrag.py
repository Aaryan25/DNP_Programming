t= int(input())
while t>0:
    tfrag = []
    while True:
        frag = str(input())
        if frag == "":
            break
        else:
            tfrag.append(frag)
    lst = [int(i, 2) for i in tfrag]
    max = bin(max(lst)).replace("0b","")

    for i in range(len(tfrag)):
        flag = 0
        for k in range(2):
            count = 0
            if flag == 0:
                check = tfrag[i] + max
            else:
                check = max + tfrag[i]
            for j in tfrag:
                if check.find(j, 0, len(tfrag[i])):
                    count += 1
                elif check.find(j, (len(check)-len(tfrag[i])), len(check)):
                    count += 1
                else:
                    break
            if count == len(tfrag):
                print(check)
                break
            else:
                flag = 1
        if count == len(tfrag):
            break
    t -= 1

""" 
Output :-
1

011
0111
01110
111
10111

01110111

"""