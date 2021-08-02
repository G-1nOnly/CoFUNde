#include <iostream>
using namespace std;

class myclass
{
public:
    int a,b,c,d;
    myclass(){a=b=0,c=d=1;}
    myclass(int x,int y){a=x;b=y;c=x+y;d=x-y;}
};
int main()
{
    myclass *p1=new myclass;
    myclass *p2=new myclass(1,2);
    cout<<p1->c<<endl;
    cout<<p1->d<<endl;
    cout<<p2->c<<endl;
    cout<<p2->d<<endl;
    delete p1,delete p2;
    return 0;
}