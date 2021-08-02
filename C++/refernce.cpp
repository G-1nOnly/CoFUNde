#include <iostream>
using namespace std;

int main()
{
    int a = 1,b = 3;
    int& ref=a;
    ref=b; // a=b, reference is just an address
    cout<<a<<endl;
    cout<<b<<endl;
    cin.get();
}

