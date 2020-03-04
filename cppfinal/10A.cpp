//Aim :- Program For Template Of Class
//Practical No  :- 10

#include <iostream>
using namespace std;

template<class t>
class samp
{
    public:
        void showdata(t x);
};
template<class t>
void samp<t>::showdata(t x)
{
 cout<<"\n You Enter  "<<x<<"\n";
}

int main()
{
    samp<int> obj;
    samp<char> obj1;
    samp<float> obj2;

    obj.showdata(5);
    obj1.showdata('A');
    obj2.showdata(5.5);

   return 0;
}

/*
Output :-

 You Enter  5
 You Enter  A
 You Enter  5.5

 */
