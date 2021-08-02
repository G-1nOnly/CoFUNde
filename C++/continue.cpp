#include <iostream>

void log(const char* str)
{
    std::cout<<str<<std::endl;
}

int main()
{
    int i=0;
    for (;i<5;i++)
    {
        if (i%2==0)
            continue; //若为偶数 则继续下一个遍历
            log("Hello, World!");
            std::cout<<i<<std::endl;
    }
    std::cin.get();
    return 0;
}
