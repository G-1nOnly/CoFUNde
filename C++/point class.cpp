#include <iostream>
#include <cmath>
using namespace std;

class point
{
    int x,y;
public:
    point(){x=y=0;}
    point(int a,int b){x=a;y=b;}
    point(const point &p1){x=p1.x;y=p1.y;}
    point operator + (const point &p1)
    {
        point p;
        p.x=this->x+p1.x;
        p.y=this->y+p1.y;
        return p;
    }
    point operator - (const point &p1)
    {
        point p;
        p.x=this->x-p1.x;
        p.y=this->y-p1.y;
        return p;
    }
    point operator -()
    {
        point p;
        p.x=-(this->x);
        p.y=-(this->y);
        return p;
    }
    double getd(const point&p1)
    {
        double d;
        d=sqrt(pow(x-p1.x,2)+pow(y-p1.y,2));
        return d;
    }
    void show()
    {
        cout<<"("<<x<<","<<y<<")"<<endl;
    }
    friend int getx(const point& p1);
    friend int gety(const point& p1);
};

int getx(const point& p1)
{
    return p1.x;
}

int gety(const point& p1)
{
    return p1.y;
}

int main()
{
    int a,b,c,d;
    printf("Input the coordinates of two points:");
    cin>>a>>b>>c>>d;
    point p1(a,b),p2(c,d);
    point p3=p1+p2,p4=p1-p2;
    point p5(-p1);
    point p6;
    cout<<"p1:";p1.show();
    cout<<"p2:";p2.show();
    cout<<"p3:";p3.show();
    cout<<"p4:";p4.show();
    cout<<"p5:("<<getx(p5)<<","<<gety(p5)<<")"<<endl;
    cout<<"p6:";p6.show();
    cout<<"The distance:"<<p1.getd(p2)<<endl;
    return 0;
}