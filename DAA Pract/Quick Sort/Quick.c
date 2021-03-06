#include<stdio.h>
#include<conio.h>
#define max 100

void Quicksort(int[],int,int);
int PARTITION(int[],int,int);
int main()
{
    int a[max],n,i;
    clrscr();
    printf("\nEnter How Many Elements Do You Want To Enter  :-   ");
    scanf("%d",&n);

    for(i=0;i<n;i++)
    {
        printf("\nEnter Array[%d]  :-  ",i+1);
        scanf("%d",&a[i]);
    }

    Quicksort(a,0,(n-1));

    printf("\nSorted Array  :-  ");
    for(i=0;i<n;i++)
    {
        printf("\t\t%d ",a[i]);
    }

    printf("\n\n");
    getch();
    return 0;
}
void Quicksort(int a[],int p,int r)
{
    int q;
    if(p<r)
    {
        q=PARTITION(a,p,r);
        Quicksort(a,p,q-1);
        Quicksort(a,q+1,r);
    }

}

int PARTITION(int a[],int p,int r)
{
    int pivot=a[r];
    int i=p-1;
    int j,temp;
    for(j=p;j<r;j++)
    {
        if(a[j]<=pivot)
        {
            i++;
            temp=a[i];
            a[i]=a[j];
            a[j]=temp;
        }
    }
    temp=a[i+1];
    a[i+1]=a[r];
    a[r]=temp;
    return (i+1);
}

/*
Output Of Quick Sort :-
Enter How Many Elements Do You Want To Enter  :-   7
Enter Array[1]  :-  3
Enter Array[2]  :-  9
Enter Array[3]  :-  2
Enter Array[4]  :-  6
Enter Array[5]  :-  5
Enter Array[6]  :-  1
Enter Array[7]  :-  4
Sorted Array  :-          1       2       3       4       5       6      9

*/

