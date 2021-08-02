#include <iostream>

struct vector2
{
    float x,y;
};

struct vector4
{
    union //union 仅接受单一对象 故利用union+struct来处理
    //以其中一个占内存最大的变量的大小S就是该union所占内存的大小 意味着union联合体内所有变量共享这块内存S
    {
        struct
        {
            float x,y,z,w;
        };

        struct // 与前一对象占据空间一样
        {
            vector2 a,b; // a与x,y占有相同空间  b与z,w占有相同空间
        };
    };

};

void printvector2(const vector2& v)
{
    std::cout<<v.x<<","<<v.y<<std::endl;
}

int main()
{
    vector4 vector = {1.0f,2.0f,3.0f,4.0f};
    printvector2(vector.a);
    printvector2(vector.b);

    vector.z=500.0f;

    printvector2(vector.a);
    printvector2(vector.b);

    std::cin.get();
}