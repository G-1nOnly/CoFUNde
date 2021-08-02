#include <iostream>
#include <string>

int main()
{
    std::string line;
    std::cout<<"Type a line terminated by 't'"<<std::endl;
    std::getline(std::cin,line,'t');
    std::cout<<line<<std::endl;
    std::cin.get();
}