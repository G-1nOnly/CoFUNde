#include <iostream>
using namespace std;

int main()
{
    const int* p;
    int a=1;
    p=&a;//p地址可以改变 指针指了之后*p不变 （e.g.*p=*p+1 无法运算）
    cout<<*p<<endl;
    int b=1;
    int* const pu=&b;//p地址不变 *p的值可以改变
    cout<<*pu+1<<endl;
    return 0;
}