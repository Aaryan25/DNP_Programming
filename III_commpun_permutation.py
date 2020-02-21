lst = []
while True:
    a = [0 for i in range (128)]
    b = [0 for i in range (128)]
    string = ""

    word1 = str(input())
    word2 = str(input())

    if word1 == "" or word2 == "":
        break
    word1 = list(word1)
    word2 = list(word2)

    for i in range(len(word1)):
        a[ord(word1[i])] = a[ord(word1[i])] + 1

    for i in range(len(word2)):
        b[ord(word2[i])] = b[ord(word2[i])] + 1

    for i in range(97, 123):
        if a[i] > 0 and b[i] > 0:
            string = string + chr(i)
            a[i] = 0
            b[i] = 0
        if i == 122 and string != "":
            lst.append(string)

for i in lst:
    print(i)


"""
Output :-
pretty
women
walking
down
the
street


e
nw
et

"""
