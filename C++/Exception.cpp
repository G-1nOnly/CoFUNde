#include <iostream>
#include <cmath>
#include <stdexcept>

double area(double a,double b, double c) noexcept(false)
//当为true表示不抛出异常，false则有可能抛出异常。如果直接写上noexcept则表示不抛出异常
{
    if(a<=0 || b<=0 || c<=0)
        throw std::invalid_argument("The side length should be positive!");
    if(a+b <= c || a+c <= b || b+c <= a )
        throw std::invalid_argument("The side length should fit the triangle equation!");
    double s = (a+b+c)/2;
    return sqrt(s*(s-a)*(s-b)*(s-c));
}

int main()
{
    double a,b,c;
    std::cout<<"Input the side lengths of a triangle: "<<std::endl;
    std::cin>>a>>b>>c;
    try{
        double s = area(a,b,c);
        std::cout<<"S = "<<s<<std::endl;
    }catch(std::exception &e){
        std::cout<<"Error: "<<e.what()<<std::endl;
    }

    std::cin.get();
}