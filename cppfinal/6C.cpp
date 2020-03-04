//Aim :- Hierarchical Inheritance
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
            cout<<"Constructor of B class"<<endl;
        }
};
class C: public A
{
    public:
        C()
        {
            cout<<"Constructor of C class"<<endl;
        }
};
int main()
{
   C obj;
   return 0;
}
/*
Output  :-

Constructor of A class
Constructor of C class

*/
