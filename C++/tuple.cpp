#include <iostream>
#include <string>
#include <tuple>

std::tuple<std::string,int> Person()
{
    return {"GAO",18};  //多返回值
};

int main()
{
    std::string name;
    int age;
    auto person = Person();
    std::cout<<std::get<0>(person)<<","<<std::get<1>(person)<<std::endl; //访问对象方法1

    std::tie(name,age) = Person();//访问对象方法2
    std::cout<<name<<","<<age<<std::endl;
    //auto [name,age] = Person(); c++17可以使用的structure binding

    std::cin.get();


}