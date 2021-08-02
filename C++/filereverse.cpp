#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
    vector <string> vs;
    string  s;
    ifstream in("test.txt");
    while (getline(in,s))
    {vs.push_back(s);}
    reverse(vs.begin(),vs.end());
    ofstream out("test1.txt");
    for (int i=0;i<vs.size();i++)
    {
        out<<vs[i]<<endl;
    }
    return 0;
}