//Aim :- Program to overload binary operator using member function
//Practical No :- 5

#include<iostream>
using namespace std;

class complex
{
    int a, b;
    public:
        void getvalue();
        complex operator +(complex);
        complex operator -(complex ob);
        void display();
};
void complex::getvalue()
{
    cout << "Enter the value of Complex Numbers a,b :-  ";
    cin >> a>>b;
}
complex complex::operator +(complex ob)
{
    complex t;
    t.a = a + ob.a;
    t.b = b + ob.b;
    return (t);
}
complex complex::operator -(complex ob)
{
    complex t;
    t.a = a - ob.a;
    t.b = b - ob.b;
    return (t);
}
void complex::display()
{
    cout << a << "+" << b << "i" << "\n";
}
int main()
{
    complex obj1, obj2, result, result1;

    obj1.getvalue();
    obj2.getvalue();

    result = obj1 + obj2;
    result1 = obj1 - obj2;

    cout << "Input Values :-\n";
    obj1.display();
    obj2.display();

    cout << "Result  :-\n";
    result.display();
    result1.display();

    return 0;
}
/*
Output  :-
Enter the value of Complex Numbers a,b :- 5 3
Enter the value of Complex Numbers a,b :- 2 4

Input Values :-
5+3i
2+4i

Result  :-
7+7i
3+-1i

*/
