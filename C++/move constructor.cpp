#include <iostream>

class point
{
    int x,y;
public:
    point()
    :x(0),y(0)
    {}

    point(int a ,int b)
    :x(a),y(b)
    {}

    point(const point && p) // && 处理右值
    {
        x = p.x;
        y = p.y;
    } //移动构造函数 (可替换拷贝构造函数)

    void show()
    {
        std::cout<<"("<<x<<","<<y<<")"<<std::endl;
    }

};
int main()
{
    point a(1,2);
    point b(point(3,4)); //直接创建右值
    point c(std::move(a)); //利用std::move 将左值转为右值(右值为匿名所在值)
    b.show();
    c.show();
    std::cin.get();
}