#include <iostream>
using namespace std;

class Rational
{
public:
    int m,n;
    Rational add(Rational r2)
    {
        Rational r3;
        r3.m=m*r2.n+n*r2.m;
        r3.n=n*r2.n;
        return r3;
    }
};

int main()
{
    Rational r1,r2,r3;
    r1.m=1;r1.n=2;
    r2.m=1;r2.n=3;
    r3=r1.add(r2);
    cout<<r3.m<<"/"<<r3.n<<endl;
    return 0;
}