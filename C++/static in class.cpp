#include <iostream>
using namespace std;

class entity
{
public:
    static int x,y;

    void show()
    {
        cout<<x<<","<<y<<endl;
    }

};

int entity::x; //记得声明
int entity::y;

int main()
{
    entity p1,p2;
    p1.x=1,p1.y=2;
    p2.x=3,p2.y=4; //static 意味着其实只有一个x和y 即 entity::x=1,entity::y=2 后 entity::x=3,entity::y=4
    p1.show();
    p2.show();
    cin.get();
}