#include <iostream>
using namespace std;
inline int func(int x)
{
    return (x*x+x);
}
int main()
{
    int a=3;
    cout<<func(3)*2<<endl;
    return 0;
}