#include <iostream>
using std::cout;
using std::endl;

class entity
{
public:
    entity()
    {
        cout<<"created"<<endl;
    }

    ~entity()
    {
        cout<<"destroyed"<<endl;
    }
};

class scopeptr
{
    entity* ptr;
public:
    scopeptr(entity* p)
    {
        ptr=p;
    }

    ~scopeptr()
    {
        delete  ptr;
    }
};

int main()
{
    entity* e =new entity();//不会出现析构函数 自动清除 利用scopepointer来解决
    scopeptr e1 =new entity();
    std::cin.get();  //调用了delete
}