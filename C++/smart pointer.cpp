#include <iostream>
#include <memory>
using std::cout;
using std::endl;

class entity
{
public:
    entity()
    {
        cout<<"created"<<endl;
    }

    ~entity()
    {
        cout<<"destroyed"<<endl;
    }
};

int main()
{
    //unique pointer 一种scope pointer 出了scope{}后即被删除
    {
        std::unique_ptr<entity> e = std::make_unique<entity>(); //保险创建 防止exception
        //一般用std::unique_ptr <entity> e(new entity())  无法用e=new entity()  创建
    }

    //shared pointer 只有所有shared pointer结束后 该shared pointer才被删除
    std::shared_ptr <entity> e1;
    {
        std::shared_ptr <entity> sharedPtr = std::make_shared <entity>();
        e1=sharedPtr;
    }

    std::weak_ptr <entity> weakPtr;
    //每将一个shared pointer 赋予另一个shared pointer ref count就会增加 但将其赋予weak pointer 则不会增加
    {
        std::shared_ptr <entity> sharedPtr2 =std::make_shared <entity> ();
        weakPtr = sharedPtr2;
    }//出了该scope后sharedPtr即被删除

    std::cin.get();
}