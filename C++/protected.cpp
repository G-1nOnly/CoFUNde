#include <iostream>
#include <cmath>
using namespace std;

class point
{
protected:
    int x,y;
public:
    void set(){x=y=0;}
    void set(int a,int b){x=a,y=b;}
    int getx(){return x;}
    int gety(){return y;}
    void show()
    {
        cout<<"("<<x<<","<<y<<")"<<endl;
    }
};

class p :public point
{
public:
    double distance(point p1)
    {
        double d;
        d=sqrt(pow(x-p1.getx(),2)+pow(y-p1.gety(),2));
        return d;
    }

    double c(point p2,point p3)
    {
        double c;
        double d=sqrt(pow(p3.getx()-p2.getx(),2)+pow(p3.gety()-p2.gety(),2));
        c=distance(p2)+distance(p3)+d;
        return c;
    }

};

int main()
{
    p p1,p2,p3;
    int a,b,x,y;
    printf("Input your p2(x2,y2) & p3(x3,y3): ");
    cin>>a>>b>>x>>y;
    cout<<endl;
    p1.set();
    p2.set(a,b);
    p3.set(x,y);
    p1.show();
    p2.show();
    p3.show();
    cout<<p1.distance(p2)<<endl;
    cout<<p1.distance(p3)<<endl;
    cout<<p1.c(p2,p3)<<endl;
    return 0;
}