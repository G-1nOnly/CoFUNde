#include <iostream>
#include <iterator>
#include <algorithm>

double square (double x)
{
    return x*x;
}

int main()
{
    std::cout<<"Input a to exit !"<<std::endl;
    std::transform(std::istream_iterator<double>(std::cin), std::istream_iterator<double>(),
            std::ostream_iterator<double>(std::cout,"\n"), square);
    std::cout<<std::endl;
    std::cin.get();
}