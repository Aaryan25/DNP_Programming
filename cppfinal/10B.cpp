//Aim :- Program For Template Of Function
//Practical No  :- 10

#include <iostream>
using namespace std;

template<class t>
void show(t a)
{
       cout<<"\n You Enter  "<<a<<"\n";
}

int main()
{
    int a;
    cout<<"Enter Any No :-  ";
    cin >>a;
    show(a);

    char b;
    cout<<"Enter Any Char :-  ";
    cin >>b;
   show(b);

    float c;
    cout<<"Enter Any float :-  ";
    cin >>c;
    show(c);

   return 0;
}

/*
Output  :-

Enter Any No :-  5
You Enter  5

Enter Any Char :-  g
You Enter  g

Enter Any float :-  6.8
You Enter  6.8

*/
