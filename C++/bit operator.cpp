#include <iostream>

using namespace std;

void swap(int& a, int& b)
//异或运算
{
    a = a^b;
    b = a^b;
    a = a^b;
}

int abs(int n)
{
    if (n>=0)
        return n;
    else
        return ~n+1; //取反后复原
}

int main()
{
    int a,b,num;
    cout<<"Please input two numbers to be swapped."<<endl;
    cin>>a>>b;
    cout<<"Before: "<<a<<" "<<b<<endl;
    swap(a,b);
    cout<<"After: "<<a<<" "<<b<<endl;
    cout<<endl;
    cout<<"Please input a number to obtain its absolute value."<<endl;
    cin>>num;
    cout<<num<<" 's absolute value is "<<abs(num)<<"."<<endl;
    cin.get();
}