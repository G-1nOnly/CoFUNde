#include <iostream>
using namespace std;

class point
{
    int x,y;
public:
    point(){x=y=0;}
    point(int a,int b){x=a;y=b;}
    point (const point &p1){x=p1.x;y=p1.y;}//非默认拷贝构造函数 若不写 则有默认拷贝构造函数
    void show()
    {
        cout<<x<<" "<<y<<endl;
    }
};

int main()
{
    int a,b;
    printf("Input the coordinate for the p1:");
    cin>>a>>b;
    point p1(a,b);
    point p2(p1);
    p2.show();
    return 0;
}