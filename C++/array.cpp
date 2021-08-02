#include <iostream>
#include <array>

//类似vector的容器 功能与array类似 用于替代c—style array
int main()
{
    std::array<int,5> data;
    for (int i=0;i<data.size();i++)
    {
        data[i]=i;
    }

    data[4]=100;

    for (int i=0;i<data.size();i++)
    {
        std::cout<<data[i];
    }

    std::cin.get();

}