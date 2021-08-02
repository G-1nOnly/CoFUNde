#include <iostream>
#include <string>
using namespace std;

//用引用处理虚函数
class entity
{
public:
    virtual const string getname() const
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

    const string getname() const override //override
    {
        return m_name;
    }
};

void gets(const entity& p)
{
    cout<<p.getname()<<endl;
}

int main()
{
    entity e;
    player p("gjn");
    gets(e);
    gets(p);
    cin.get();
}