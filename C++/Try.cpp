#include <iostream>

double divide(double x,double y)
{
    if(y==0)
        throw x;
    return x/y;
}

int main()
{
    double a,b;
    std::cout<<"Input the first number: "<<std::endl;
    std::cin>>a;
    std::cout<<"Input the second number: "<<std::endl;
    std::cin>>b;
    try{
        std::cout<<a<<" / "<<b<<" = "<<divide(a,b)<<std::endl;
    }catch(double e){
        std::cout<<"Error!\n"<<e<<" is divided by 0"<<std::endl;
    }
    std::cout<<"Division Finished"<<std::endl;

    std::cin.get();
}
