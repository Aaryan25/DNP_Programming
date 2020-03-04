//Aim :- Single Inheritance
//Practical No. :- 6

#include <iostream>
using namespace std;
class A
{
    public:
        A()
        {
            cout<<"Constructor of A class"<<endl;
        }
};
class B: public A
{
    public:
        B()
        {
            cout<<"Constructor of B class";
        }
};
int main()
{
   B obj;
   return 0;
}
/*
Output  :-
Constructor of A class
Constructor of B class
*/
