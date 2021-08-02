#include <iostream>
#include <string>
using namespace std;

//member initializer list 防止构造函数多次构造
class entity
{
    int a;
    string str;
public:
    entity()
    :a(0),str("entity")
    {}

    entity(int x, string name)
    :a(x),str(name)
    {}

    void show()
    {
        cout<<a<<" "<<str<<endl;
    }
};


int main()
{
    entity e;
    entity e1(1,"abc");
    e.show();
    e1.show();
    cin.get();
}