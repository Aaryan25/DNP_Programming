keyboard = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=',
            'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\',
            'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', '\'',
            'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/']

while True:
    string = ""
    line = str(input())
    if line == "":
        break
    lst = list(line.upper())
    for i in lst:
        if i == " ":
            string += " "
        else:
            for k in range(len(keyboard)):
                if i == keyboard[k]:
                    string += keyboard[k-1]
                    break

    print(string)

"""
Output :-

O S, GOMR YPFSU/
I AM FINE TODAY.

"""
