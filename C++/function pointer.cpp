#include <iostream>
#include <vector>

void hhh(int a)
{
    std::cout<<"hhhhhh value:"<<a<<std::endl;
}

void f(const std::vector<int>& v,void (*hhh)(int)) // 函数类型+（*函数名）（填入的类型）
    {
    for (int i=0;i<v.size();i++)
    {
        hhh(v[i]);
    }
}

int main()
{
    auto func = hhh; //相当于 auto func=&hhh 获得一个地址 (函数指针) 本质上是void(*func)(int)=hhh 可用typedef 声明后简化
    func(0); //可调用 类似于将函数赋予一个变量
    func(1);

    std::cout<<std::endl;

    std::vector <int> v={1,5,2,4,3};
    f(v,hhh); //利用函数指针将函数嵌入另一函数中 可用lambda替代 f(v,[](int a){std::cout<<"hhhhhh value:"<<a<<std::endl;});
    std::cin.get();
}