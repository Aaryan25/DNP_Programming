//Aim :- Program For Exception Handling
//Practical No. :- 8

#include <iostream>
#include <exception>

using namespace std;

class NegativeValException : public exception
{
    public:
        virtual const char* what() const throw()
        {
            return "A Negative value";
        }
};

int main()
{
    int i;
    cout<<"\nEnter Any Number  :-  ";
    cin >>i;

    try
    {
        if (i < 0)
            throw NegativeValException();
        else
            cout << i << " is a +ve value";
    }
    catch (NegativeValException e)
    {
        cout << e.what() << endl;
    }
    return 0;
}

/*
Output  :-

Enter Any Number  :-  10
10 is a +ve value

Enter Any Number  :-  -5
A Negative value

*/
