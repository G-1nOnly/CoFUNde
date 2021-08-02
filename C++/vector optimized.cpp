#include <iostream>
#include <vector>

using std::vector;
using std::cout;
using std::endl;

class vector2d
{
    int x,y;
public:
    vector2d()
    :x(0),y(0)
    {}

    vector2d(int a,int b)
    :x(a),y(b)
    {
        cout<<"copied"<<endl;
    }
};

int main()
{
    vector <vector2d> v0,v;

    v0.push_back(vector2d(11,12));
    v0.push_back(vector2d(13,14));
    v0.push_back(vector2d(15,16)); //未优化版本

    v.reserve(3); //预留三个空间 (在已知情况下可用此优化)
    v.emplace_back(1,2);
    v.emplace_back(3,4);
    v.emplace_back(5,6); //emplace_back相对于push_back是直接在vector中创建 是一个优化步骤

    v0.clear();
    v.clear();

    std::cin.get();
}

