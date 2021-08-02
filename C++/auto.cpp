#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int i;
    vector <int> v;
    for (i=0;i<10;i++)
    {
        v.push_back(i);
    }

    auto it =v.begin(); //auto = std::vector <int> ::iterator
    for(; it != v.end(); it++)
    {
        cout<<*it<<' ';
    }
    cout<<endl;
    return 0;

}