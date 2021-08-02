#include <iostream>
#include <cmath>
using namespace std;

class point
{
    int x,y;
public:
    point(){x=y=0;}
    point(int a,int b){x=a;y=b;}
    int getx(){return x;}
    int gety(){return y;}
    void show()
    {
        cout<<"("<<x<<","<<y<<")"<<endl;
    }
    double getd()
    {
        double d;
        d=sqrt(x*x+y*y);
        return d;
    }
    point operator+(const point& p1)
    {
        point p;
        p.x=this->x+p1.x;
        p.y=this->y+p1.y;
        return p;
    }

    point operator-(const point& p1)
    {
        point p;
        p.x=this->x-p1.x;
        p.y=this->y-p1.y;
        return p;
    }

};

int main()
{
    int a,b,c,d;
    cin>>a>>b>>c>>d;
    point p1(a,b);
    point p2(c,d);
    point p3=p1+p2;
    point p4=p1-p2;
    p1.show();
    p2.show();
    p3.show();
    p4.show();
    cout<<p3.getd()<<endl;
    return 0;
}