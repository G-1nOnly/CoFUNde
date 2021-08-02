#include <iostream>

struct  entity
{
    int x,y;

    int* gets()
    {
        return &x;
    }
};

int main()
{
    entity e= {1,2};
    int a = *(int*)(&e); //第一种形式
    std::cout<<a<<std::endl;

    int* b = e.gets(); //第二种形式
    b[0]=3,b[1]=4;
    std::cout<<b[0]<<" "<<b[1]<<std::endl;

    std::cin.get();
}