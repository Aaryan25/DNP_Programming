#include <stdio.h>
#include<conio.h>
int main()
{
	int i,j,k,n,a[10][10],indeg[10],flag[10],count=0;
    clrscr();

	printf("Enter the no of vertices  :-  ");
	scanf("%d",&n);

	printf("Enter the adjacency matrix :- \n");
	for(i=0;i<n;i++)
    {
		printf("Enter row %d  :-  ",i+1);
		for(j=0;j<n;j++)
		{
		    scanf("%d",&a[i][j]);
		}
	}

	for(i=0;i<n;i++)
    {
        indeg[i]=0;
        flag[i]=0;
    }

    for(i=0;i<n;i++)
    {
         for(j=0;j<n;j++)
         {
            indeg[i]=indeg[i]+a[j][i];
         }
    }
    printf("\nThe topological order is:");

    while(count<n)
    {
        for(k=0;k<n;k++)
        {
            if((indeg[k]==0) && (flag[k]==0))
            {
                printf("%d ",(k+1));
                flag [k]=1;
            }

            for(i=0;i<n;i++)
            {
                if(a[i][k]==1)
                {
                    indeg[k]--;
                }
            }
        }
        count++;
    }
    getch();
    return 0;
}

/*
Output Of Topological Order :-

Enter the no of vertices  :-  5

Enter the adjacency matrix :-

Enter row 1  :-  0 0 1 0 1
Enter row 2  :-  1 0 0 1 0
Enter row 3  :-  0 0 0 1 1
Enter row 4  :-  0 0 0 0 0
Enter row 5  :-  0 0 0 0 0

The topological order is:2 1 3 4 5

*/

