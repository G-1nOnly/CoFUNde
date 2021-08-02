#include <iostream>
#include <utility>
#include <map>
#include <string>

int main()
{
    std::map<std::string,int> test;
    test.insert(std::make_pair("Course A",1)); //映射关系 make——pair不需要声明变量类型
    test.insert(std::make_pair("Course B",2)); //也可以使用 pair<a,b> a与b为类型
    test.insert(std::make_pair("Course C",3));
    auto iter = test.begin();
    for (;iter != test.end();iter++)
    {
        std::cout<<iter->first<<"  "<<iter->second<<std::endl;
    }
    //输出方法，利用迭代器遍历 first即第一个元素 second即第二个

    std::cin.get();
}
