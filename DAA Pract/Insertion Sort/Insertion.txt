#include<stdio.h>
#include<conio.h>
#define max 100
int main()
{
    int a[max],n,i,j,key;
    clrscr();

    printf("\nEnter How Many Elements Do You Want To Add  :-  ");
    scanf("%d",&n);

    for(i=0;i<n;i++)
    {
        printf("\nEnter Array[%d]  :-  ",i+1);
        scanf("%d",&a[i]);
    }

    for(i=1;i<n;i++)
    {
        key=a[i];
        j=i-1;
        while(j>=0 && a[j]>key)
        {
                a[j+1]=a[j];
                j--;
        }
        a[j+1]=key;
    }

    printf("\nSorted Array  :-  \n");
    for(i=0;i<n;i++)
    {
        printf("\t\t %d ",a[i]);
    }
    printf("\n\n");

    getch();
    return 0;
}

/*
Output Of Insertion Sort  :-
Enter How Many Elements Do You Want To Add  :-  5
Enter Array[1]  :-  7
Enter Array[2]  :-  2
Enter Array[3]  :-  5
Enter Array[4]  :-  1
Enter Array[5]  :-  3
Sorted Array  :-
        1               2               3               5               7
*/
