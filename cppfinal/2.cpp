//Aim :- Program to overload Constructor
//Practical No. :- 2

#include<iostream>
using namespace std;

class bank
{
    char *name,*type;
    int deposit;
    public:
        bank();
        bank(bank&);
        bank(char*,char*,int);
        void display();
};
bank::bank()
{
    name="Mayur";
    type="Saving";
    deposit=500;
}
bank::bank(bank &obj)
{
    name=obj.name;
    type=obj.type;
    deposit=obj.deposit;
}
bank::bank(char *pname,char *ptype,int pdep)
{
    name=pname;
    type=ptype;
    deposit=pdep;
}
void bank::display()
{
    cout<<endl<<name<<"\t"<<type<<"\t"<<deposit<<endl;
}
int main()
{
    bank obj;
    bank obj1(obj);
    bank obj2("Mayur","saving",500);
    cout<<"\n\nUsing Blank or Default Constructor\n";
    obj.display();
    cout<<"\n\nUsing Copy Constructor\n";
    obj1.display();
    cout<<"\n\nUsing Parameterized Constructor\n";
    obj2.display();

    return 0;
}

/*
Output  :-

Using Blank or Default Constructor
Mayur   Saving  500


Using Copy Constructor
Mayur   Saving  500


Using Parameterized Constructor
Mayur   saving  500

*/
