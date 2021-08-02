#include <iostream>
using namespace std;

//mutable in class member
class p
{
    int x;
    mutable int y=3; //可以改变的const mutable
public:
    int gety()
    {
        return y;
    }
    void change(int a)
    {
        y=a;
    }
};
int main()
{
    p test;
    cout<<test.gety()<<endl;
    test.change(2);
    cout<<test.gety()<<endl;
    return 0;
}