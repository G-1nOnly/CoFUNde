#include <iostream>

template <typename T,int N> //也可以用template <class T>
class Array
{
    T array[N];
public:
    int getsize() const {return N;}
    T& operator [] (int i)
    {
        return  array[i];
    }
};


int main()
{
    Array <int,5> a; //可指定类型和大小
    for (int i=0;i<a.getsize();i++)
    {
        a[i]=i;
    }

    for (int i=0;i<a.getsize();i++)
    {
        std::cout<<a[i]<<std::endl;
    }

    std::cout<<std::endl;
    std::cout<<a.getsize()<<std::endl;
    std::cin.get();
}


