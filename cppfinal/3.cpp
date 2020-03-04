//Aim :- Program for function overloading
//Practical No. :- 3

#include<iostream>
#include<stdlib.h>

using namespace std;
class shape
{
    public:
      int area(int,int);
      float area(int,int,int);
      float area(int,float);
};
int shape::area(int no1,int no2)
{
    return no1*no2;
}
float shape::area(int no1,int no2,int half)
{
    return float(no1)*float(no2)*0.5F;
}
float shape::area(int no1,float pi)
{
    return no1*no1*pi;
}
int main()
{
    int no1,no2,r;

    shape obj;
    int ch=0;

    while(ch!=4)
    {
        //clrscr();
        cout<<"\n1 for Area Of Rectangle";
        cout<<"\n2 for Area Of Triangle";
        cout<<"\n3 for Area Of Sphere";
        cout<<"\n4 for Exit";
        cout<<"\nEnter Your Choice  :-  ";
        cin>>ch;

        switch(ch)
        {
            case 1:
                cout<<"\nEnter length :-  ";
                cin>>no1;
                cout<<"\nEnter breadth :-  ";
                cin>>no2;
                cout<<"\nArea Of Rectangle  :-  "<<obj.area(no1,no2);
                break;
            case 2:
                cout<<"\nEnter base :-  ";
                cin>>no1;
                cout<<"\nEnter height :-  ";
                cin>>no2;
                cout<<"\nArea Of Triangle  :-  "<<obj.area(no1,no2,0.5F);
                break;
            case 3:
                cout<<"\nEnter Radius :-  ";
                cin>>r;
                cout<<"\nArea Of Sphere  :-  "<<obj.area(r,3.14F);
                break;
            case 4:
                exit(0);
            default:
                cout<<"\nWrong Choice";
        }
        cout<<"\n";
    }
    return 0;
}

/*
Output :-

1 for Area Of Rectangle
2 for Area Of Triangle
3 for Area Of Sphere
4 for Exit
Enter Your Choice  :-  1

Enter length :-  5
Enter breadth :-  6

Area Of Rectangle  :-  30

1 for Area Of Rectangle
2 for Area Of Triangle
3 for Area Of Sphere
4 for Exit
Enter Your Choice  :-  2

Enter base :-  6
Enter height :-  7

Area Of Triangle  :-  21

1 for Area Of Rectangle
2 for Area Of Triangle
3 for Area Of Sphere
4 for Exit
Enter Your Choice  :-  4

*/
