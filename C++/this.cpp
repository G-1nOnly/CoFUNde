#include <iostream>
#include <string>
using namespace std;

class person
{
    string name;
    int age;
public:
    string setname(string name)
    {
        return this->name=name;
    }

    int setage(int age)
    {
        return this->age=age;
    }

    void show()
    {
       cout<<"name: "<<name<<endl;
       cout<<"age: "<<age<<endl;
    }
};

int main()
{
    string str;
    int a;
    printf("set your name: ");
    getline(cin,str);
    cout<<endl;
    printf("set your age: ");
    cin>>a;
    person p1;
    p1.setage(a);
    cout<<endl;
    p1.setname(str);
    p1.show();
    return 0;
}