#include <iostream>
#include <algorithm>
#include <vector>

int main()
{
    std::vector<int> v={2,5,4,1,3};
    std::sort(v.begin(),v.end(),[](int a,int b){return a>b;});
    //最后lambda返回的是bool 类型 即若true a调整至b前 若false a调整至b后
    for (int value:v) //value只是v中一个迭代器遍历
    {
        std::cout<<value<<std::endl;
    }

    std::cin.get();
}

