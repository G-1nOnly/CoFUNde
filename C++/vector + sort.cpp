#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
    vector <int> v;
    int a,i,ret;
    while(1)
    {
        cin>>a;
        if(a==0) break;
        else v.push_back(a);
    }
    sort(v.begin(),v.end());
    for(i=1;i<v.size()-1;i++)
    {
        if(v[i]!=v[i-1]&&v[i]!=v[i+1]) ret=v[i];
        else if (v[0]!=v[1]) ret=v[0];
        else if (v[v.size()-1]!= v[v.size()-2]) ret=v[v.size()];
    }
    cout<<ret<<endl;
}