//Aim :- Multiple Inheritance
//Practical No. :- 6

#include <iostream>
using namespace std;
class A
{
    public:
        A()
        {
            cout<<"Base Class A"<<endl;
        }
};
class B
{
    public:
        B()
        {
            cout<<"Base Class B"<<endl;
        }
};
class C: public A, public B
{
    public:
        C()
        {
            cout<<"Derived Class C From Base Class A & B"<<endl;
        }
};
int main()
{
   C obj;
   return 0;
}

/*
Output  :-
Base Class A
Base Class B
Derived Class C From Base Class A & B
*/
