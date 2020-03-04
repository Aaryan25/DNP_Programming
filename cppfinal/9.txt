//Aim :- Program For Dynamic Binding Using Virtual Function
//Practical No. :- 9
#include <iostream>

using namespace std;

class sample
{
    int a1;
    int a2;

    public:
        sample()
        {
             cout<<"\nEnter Base Class Member  :- \n";
             cin >> a1 >> a2;
        }
        virtual void compute()
        {
            a1 = -a1;
            a2 = -a2;
        }
        virtual void display()
        {
            cout<<"\nBase Class Member  :- ";
            cout << a1 << " " << a2 << endl;
        }
};
class num :public sample {
    int n1;
    int n2;
public:
    num()
    {
        cout<<"\nEnter Derived Class Member  :- \n";
        cin >> n1 >> n2;
    }
    void compute()
    {
        n1 = -n1;
        n2 = -n2;
    }
    void display()
    {
        cout<<"\nDerived Class Member  :- ";
        cout << n1 << " " << n2;
    }
};

int main()
{
    sample *ptr, ob1;
    num ob2;

    ptr = &ob1;
    ptr->compute();
    ptr->display();

    ptr = &ob2;
    ptr->compute();
    ptr->display();

    return 0;
}
/*
Output  :-

Enter Base Class Member  :-
50
100

Enter Base Class Member  :-
60
80

Enter Derived Class Member  :-
20
30

Base Class Member  :- -50 -100
Derived Class Member  :- -20 -30

*/
