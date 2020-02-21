"""
Chapter : 1
Problem : LCD Display
Roll No : 10 

"""
def clearLcd():
    for i in range(nLines):
        for j in range(nColumns):
            lcdNumber[i][j] = ' '

def drawLine(lineNumber):
    for j in range(1, nColumns-1):
        lcdNumber[lineNumber][j] = '-'

def drawFirstLine():
    drawLine(0)

def drawMiddleLine():
    drawLine(nLines // 2)

def drawLastLine():
    drawLine(nLines - 1)

def drawFirstColumn(columnNumber):
    for i in range(1, nLines // 2):
        lcdNumber[i][columnNumber] = '|'

def drawLastColumn(columnNumber):
    for i in range((nLines // 2) + 1, nLines - 1):
        lcdNumber[i][columnNumber] = '|'

def drawFirstLeftColumn():
    drawFirstColumn(0)

def drawLastLeftColumn():
    drawLastColumn(0)

def drawFirstRightColumn():
    drawFirstColumn(nColumns - 1)

def drawLastRightColumn():
    drawLastColumn(nColumns - 1)

def printLcd(position):
    for i in range(nLines):
        for j in range(nColumns):
            lcdNumbers[position][i][j] = lcdNumber[i][j]
    return  lcdNumbers
def printZero(position):
    clearLcd()
    drawFirstLine()
    drawFirstLeftColumn()
    drawFirstRightColumn()
    drawLastLeftColumn()
    drawLastRightColumn()
    drawLastLine()
    return printLcd(position)

def printOne(position):
    clearLcd()
    drawFirstRightColumn()
    drawLastRightColumn()
    return printLcd(position)

def printTwo(position):
    clearLcd()
    drawFirstLine()
    drawFirstRightColumn()
    drawMiddleLine()
    drawLastLeftColumn()
    drawLastLine()
    return printLcd(position)

def printThree(position):
    clearLcd()
    drawFirstLine()
    drawFirstRightColumn()
    drawMiddleLine()
    drawLastRightColumn()
    drawLastLine()
    return printLcd(position)

def printFour(position):
    clearLcd()
    drawFirstLeftColumn()
    drawFirstRightColumn()
    drawMiddleLine()
    drawLastRightColumn()
    return printLcd(position)

def printFive(position):
    clearLcd()
    drawFirstLine()
    drawFirstLeftColumn()
    drawMiddleLine()
    drawLastRightColumn()
    drawLastLine()
    return printLcd(position)

def printSix(position):
    clearLcd()
    drawFirstLine()
    drawFirstLeftColumn()
    drawMiddleLine()
    drawLastLeftColumn()
    drawLastRightColumn()
    drawLastLine()
    return printLcd(position)

def printSeven(position):
    clearLcd()
    drawFirstLine()
    drawFirstRightColumn()
    drawLastRightColumn()
    return printLcd(position)

def printEight(position):
    clearLcd()
    drawFirstLine()
    drawFirstLeftColumn()
    drawFirstRightColumn()
    drawMiddleLine()
    drawLastLeftColumn()
    drawLastRightColumn()
    drawLastLine()
    return printLcd(position)

def printNine(position):
    clearLcd()
    drawFirstLine()
    drawFirstLeftColumn()
    drawFirstRightColumn()
    drawMiddleLine()
    drawLastRightColumn()
    drawLastLine()
    lcdNumbers = printLcd(position)
    return lcdNumbers
def printNumber(n, position):
    lst = [printZero, printOne,
           printTwo, printThree,printFour,
           printFive, printSix, printSeven,
           printEight, printNine]

    lcdNumbers = lst[n](position)
    return lcdNumbers

size = int(input("\nEnter Size :- "))
nLines = 0
nColumns = 0
no = str(input("\nEnter Number :- "))


while size != 0 or int(no) != 0:

    lcdNumber = [[" " for j in range(size + 2)] for i in range(size * 2 + 3)]
    lcdNumbers = [[[" " for j in range(size + 2)] for i in range(size * 2 + 3)] for k in range(len(no))]

    nLines = 2 * size + 3
    nColumns = size + 2

    length = len(no)
    for i in range(length):
        n = int(no[i])
        lcdNumbers = printNumber(n, i)
    print(" ",end="")
    for i in range(size * 2 + 3):
        for n in range(len(no)):
            for j in range(size + 2):
                print(lcdNumbers[n][i][j], end=" ")

        if (n < length - 1):
            print(" ", end=" ")
        print("\n", end=" ")
    print("\n", end=" ")

    size = int(input("\nEnter Size :- "))
    no = str(input("\nEnter Number :- "))
    
"""
Output :-

Enter Size :- 2
Enter Number :- 12345
           - -     - -             - -   
       |       |       | |     | |       
       |       |       | |     | |       
           - -     - -     - -     - -   
       | |             |       |       | 
       | |             |       |       | 
           - -     - -             - -   
 
 
Enter Size :- 3
Enter Number :- 67890
   - - -     - - -     - - -     - - -     - - -   
 |                 | |       | |       | |       | 
 |                 | |       | |       | |       | 
 |                 | |       | |       | |       | 
   - - -               - - -     - - -             
 |       |         | |       |         | |       | 
 |       |         | |       |         | |       | 
 |       |         | |       |         | |       | 
   - - -               - - -     - - -     - - -   
 
 
Enter Size :- 0
Enter Number :- 0
"""
