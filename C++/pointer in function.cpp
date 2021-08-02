#include <iostream>

void split(float n,int* a,float* b)
{
    *a = (int)n;
    *b = n - *a;
}

int main()
{
    float x,frac;
    int intpart;
    std::cout<<"input a number"<<std::endl;
    std::cin>>x;
    split(x, &intpart, &frac);
    std::cout<<intpart<<" "<<frac<<std::endl;
    std::cin.get();
}