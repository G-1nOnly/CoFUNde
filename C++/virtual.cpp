#include <iostream>
#include <string>
using namespace std;

class entity
{
public:
    virtual string getname()
    {
        return "entity";
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

void gets(entity* e) //利用一个函数更好区分 均提取entity部分
{
    cout<<e->getname()<<endl;
}

int main()
{
    entity* e=new entity();
    player* p=new player("og");
    gets(e);
    gets(p);
    cin.get();
}