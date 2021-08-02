#include <iostream>
#include <cmath>
using namespace std;

class point
{
    int x,y;
public:
    void set(){x=y=0;}
    void set(int a,int b){x=a;y=b;}
    int getx(){return x;}
    int gety(){return y;}
    friend double distance(point p1);
    friend class point1;
};

class point1
{
    int x,y;
public:
    void set(point p1){x=p1.x*p1.x;y=p1.y*p1.y;}
    double d2()
    {
        return x+y;
    }
    int getx2()
    {
        return x;
    }

    int gety2()
    {
        return y;
    }

};

double distance(point p1)
{
    double d;
    d=sqrt(pow(p1.x,2)+pow(p1.y,2));
    return d;
}
int main()
{
    point p1;
    point1 p12;
    p1.set(3,4);
    cout<<distance(p1)<<endl;
    p12.set(p1);
    cout<<"("<<p12.getx2()<<","<<p12.gety2()<<")"<<endl;
    cout<<p12.d2()<<endl;
    return 0;
}