#include <iostream>
#include <iterator>
#include <vector>
#include <algorithm>
#include <deque>
int main()
{
    std::cout<<"Input a to stop!"<<std::endl;
    std::istream_iterator<int> i1(std::cin), i2;
    std::vector<int> v(i1,i2);
    std::deque<int> d;
    sort(v.begin(),v.end(),[](int a,int b){return a>b;});
    auto iter = v.begin();
    for (;iter != v.end();iter++)
    {
        if(*iter%2==0)
            d.push_back(*iter);
        else
            d.push_front(*iter);
    }
    std::copy(d.begin(),d.end(),std::ostream_iterator<int>(std::cout,"\n"));
    std::cin.get();
}