#include<stdio.h>
#include<conio.h>
#include<math.h>

void Queen(int,int);
int place(int,int);
int board[20],i;

int main()
{
    int n;
    clrscr();

    printf("\nEnter How Many Queen You Want To Place  :-  ");
    scanf("%d",&n);

    Queen(1,n);

    getch();
    return 0;
}
void Queen(int row ,int n)
{
    int column;

    for(column=1;column<=n;column++)
    {
        if(place(row,column))
        {
            board[row]=column;
            if(row==n)
            {
                printf("\nSolution  :-  ");
                for(i=1;i<=n;i++)
                {
                    printf("\t%d",board[i]);
                }
            }
            else
            {
                Queen(row+1,n);
            }
        }
    }
}

int place(int row,int column)
{
    for(i=1;i<row;i++)
    {
        if(board[i]==column)
        {
            return 0;
        }
        if(abs(board[i]-column)==abs(i-row))
        {
            return 0;
        }
    }
    return 1;
}

/*
Output Of NQueen Problem  :-

Enter How Many Queen You Want To Place  :-  4

Solution  :-    2       4       1       3
Solution  :-    3       1       4       2


Enter How Many Queen You Want To Place  :-  5

Solution  :-    1       3       5       2       4
Solution  :-    1       4       2       5       3
Solution  :-    2       4       1       3       5
Solution  :-    2       5       3       1       4
Solution  :-    3       1       4       2       5
Solution  :-    3       5       2       4       1
Solution  :-    4       1       3       5       2
Solution  :-    4       2       5       3       1
Solution  :-    5       2       4       1       3
Solution  :-    5       3       1       4       2

*/
