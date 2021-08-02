#include <iostream>
#include <string>
using namespace std;

class print
{
public:
    virtual string getname()=0; //虚函数  待子类编写 子类必须编写 才能实现函数引用
};

class entity:public print
{
public:
    string getname() override  //类中若含有改纯虚函数编写 则为子类
    {
        return ("entity");
    }
};

class player:public entity
{
private: string m_name;
public:
    player(const string& name)
    {
        m_name=name;
    }

    string getname() override //override
    {
        return m_name;
    }
};

void gets(print* p) //利用一个函数更好区分 均提取entity部分 (虚函数一般用指针操作)
{
    cout<<p->getname()<<endl;
}

int main()
{
    entity* e=new entity();
    player* p=new player("og");
    gets(e);
    gets(p);
    cin.get();
}