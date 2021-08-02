#include <iostream>
using namespace std;
int isprime(int x)
{
    int i;
    for (i=2;i<x;i++)
    {if(x%i==0) return 0;}
    return 1;
}
int main()
{
    int arr[100],n=0,x=0;
    for (int j=2;j<100;j++)
    {if(isprime(j)==1)
        arr[n]=j,n++;}
            for ( x=0;x<=20;x++)
            { int y=arr[x]*arr[x+1],z=arr[x]*arr[x];
                if(z<100) cout<<z<<endl;
                if(y<100) cout<<y<<endl;}
    return 0;
}