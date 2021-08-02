#include <iostream>
using namespace std;

enum selection
{
    a=1,b,c,d,e
};

int main()
{
    int n;
    cin>>n;
    switch(n)
    {
        case a:
            printf("a");
            break;
        case b:
            printf("b");
            break;
        case c:
            printf("c");
            break;
        case d:
            printf("d");
            break;
        case e:
            printf("e");
            break;
        default:
            printf("Invalid input!");
    }
    cin.get();
}