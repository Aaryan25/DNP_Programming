//Aim :- Program For File Handling
//Practical No, :- 7

#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ofstream fout;
    ifstream fin;
    string line;
    char ch,choice='y';

    while(choice=='y' || choice=='Y')
    {

        cout<<"\n1 For Write Data";
        cout<<"\n1 For Read Data";
        cout<<"\nEnter Your Choice :-  ";
        cin>>ch;
        switch(ch)
        {
            case '1':
                fout.open("sample.txt", ios::app );
                while (fout)
                {
                    getline(cin, line);
                    if (line == "-1")
                        break;
                    fout<< line << endl;
                }
                fout.close();
                break;
            case '2':
                fin.open("sample.txt");
                while (fin)
                {
                    getline(fin, line);
                    cout << line << endl;
                }
                fin.close();
                break;
            default:
                cout<<"\nWrong Choice";
        }
        cout<<"\nDo You Want To Perform More Operations :-  ";
        cin>>choice;
    }

    return 0;
}
/*
Output  :-

1 For Write Data
1 For Read Data
Enter Your Choice :-  1
Mayur
-1

Do You Want To Perform More Operations :-  y

1 For Write Data
1 For Read Data
Enter Your Choice :-  2

Mayur

Do You Want To Perform More Operations :-  y

1 For Write Data
1 For Read Data
Enter Your Choice :-  1
Jain
-1

Do You Want To Perform More Operations :-  y

1 For Write Data
1 For Read Data
Enter Your Choice :-  2

Mayur
Jain

Do You Want To Perform More Operations :-  n

*/
