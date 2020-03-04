//Aim :- Program to overload Unary operator using member function
//Practical No :- 4

#include<iostream>
using namespace std;

class complex
{
    int a, b, c;
    public:
        complex(){}
        void getvalue();
        void operator ++();
        void operator --();
        void display();
};
void complex::getvalue()
{
    cout << "Enter the Two Numbers  :-  ";
    cin >> a>>b;
}
void complex::operator ++()
{
    a = ++a;
    b = ++b;
}
void complex::operator --()
{
    a = --a;
    b = --b;
}
void complex::display()
{
    cout << a << "+" << b << "i" << "\n";
}

int main()
{
    complex obj;
    obj.getvalue();
    ++obj;
    cout << "Increment Complex Number  :-  ";
    obj.display();
    --obj;
    cout << "Decrement Complex Number  :-  ";
    obj.display();
    return 0;
}
/*
Output  :-

Enter the Two Numbers  :-  3 5
Increment Complex Number  :-  4+6i
Decrement Complex Number  :-  3+5i

*/
