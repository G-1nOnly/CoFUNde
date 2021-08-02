#include <iostream>
#include <string>
using namespace std;

int cmp(string s1,string s2) {
    int n = min(s1.size(), s2.size());
    int i = -1, f = 0;
    while (i < n-1) {
        i=i+1;
        if (s1[i] < s2[i])
        {
            f=1;
            break;
        }

    }
    return f;
}

void swap(string& s1,string& s2)
{
    string temp;
    temp=s1;
    s1=s2;
    s2=temp;
}

int main()
{
    string s1,s2;
    cin>>s1;
    cin>>s2;
    if (cmp(s1,s2)==0) swap(s1,s2);
    cout<<s1<<endl;
    cout<<s2<<endl;
    return 0;
}