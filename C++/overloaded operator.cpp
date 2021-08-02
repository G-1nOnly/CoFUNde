#include <iostream>

class vector2d
{
public:
    int x,y;

    vector2d(){x=y=0;}

    vector2d(int a,int b){x=a,y=b;}

    vector2d operator+(const vector2d& other)
    {
        return vector2d(x+other.x,y+other.y);
    }
};

std::ostream& operator <<(std::ostream& stream, const vector2d& other)
{
    stream<<other.x<<","<<other.y<<std::endl;
    return stream;
} //overloaded <<

int main()
{
    vector2d v1(1,2);
    vector2d v2(3,4);
    vector2d v3=v1+v2;
    std::cout<<v3<<std::endl;
    std::cin.get();
}