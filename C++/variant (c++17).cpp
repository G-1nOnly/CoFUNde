#include <iostream>
#include <variant>

//variant c++17才有 multiple data types
int main()
{
    std::variant<std::string,int> data; // variant 拥有存储全部类型的内存
    data = "cherno";
    std::cout<<std::get<std::string>(data)<<std::endl;
    std::cout<<data.index()<<std::endl; //index 0:string 1:int
    auto* value = std::get_if<std::string>(&data); //get_if判断是不是该类型 返回值为指针 非该类型 返回nullptr

    //故可以用下式判断
    if ( auto value1 = std::get_if<std::string>(&data))
    {
        std::cout<<*value1<<std::endl;
    }

    data = 10;
    std::cout<<std::get<int>(data)<<std::endl;
    std::cout<<data.index()<<std::endl;

    std::cin.get();
}
