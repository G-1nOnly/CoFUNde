#include <iostream>

// singleton 单一实例

class singleton
{
private:
    singleton () {}

    float F = 0.5f;
public:
    singleton (const singleton& s) = delete; //去除拷贝构造函数

    static singleton& get()
    {
        static singleton s_instance; //简化代码 不然就需要利用 singleton::singleton s_instance 声明
        return s_instance;
    }

    float Float (){return F;}

    static float IFloat () {return  get().Float();}

};

int main()
{
    singleton& s = singleton::get();
    // 实现将singleton视为单一实例 如其他类型般操作 注意用&引用 不然会创建新的实例
    std::cout<<s.Float()<<std::endl; // 或float a = singleton::get().Float();

    float number = singleton::IFloat(); //若Float()为private 则利用该函数访问
    std::cout<<number<<std::endl;
    std::cin.get();
}