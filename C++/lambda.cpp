#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    int a=5,b=6;
    auto lambda = [=](int v){std::cout <<a<<","<<v<< std::endl;}; //利用auto声明简化
    //[]capture 用于处理外界输入变量  []不输入  =全部均可  // this 以引用形式输入当前变量

    auto lambda1 = [a,&b](int v){std::cout<<a+b<<","<< v<< std::endl;};// &引用 a,&b a 复制一遍a输入 b引用输入

    auto lambda2 = [=](int v) mutable{a=6;std::cout <<a<<","<<v<< std::endl;}; //添加mutable后可以更改

    lambda(0);
    lambda1(1);
    lambda2(0);

    std::vector <int> v={1,5,4,2,3};
    auto it=std::find_if(v.begin(),v.end(),[](int value){return value>3;}); //find_if与lambda结合
    //find_if 返回符合条件的第一个值
    std::cout<<*it<<std::endl;
    std::cin.get();
}
