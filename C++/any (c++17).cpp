#include <iostream>
#include <any>

//any c++17才有

int main()
{
    std::any data; //data可以为任意类型 也可以用std::make_any <typename> (value)初始化
    data = 1;
    std::cout << std::any_cast<int>(data) << '\n'; //cast 确定类型
    //修改时可用 data.reset()清空

    data.reset();
    data = std::string("Hello");
    std::cout << std::any_cast<std::string>(data) << '\n';
    std::any_cast<std::string&>(data) ="Hi!";
    std::cout << std::any_cast<std::string>(data) << '\n'; //若要修改该值需要使用该类型引用

    data = 'a';
    std::cout << std::any_cast<char>(data) << '\n';

    std::cin.get();
}