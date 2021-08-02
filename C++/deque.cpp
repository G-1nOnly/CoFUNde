#include <iostream>
#include <deque>

int main()
{
    std::deque <int> s;
    while (true)
    {
        int a;
        std::cin>>a;
        if (a == 0)
            break;
        else
            s.emplace_front(a); //push_front也可
    }

    for (int value : s)
    {
        std::cout<<value<<std::endl;
    }
    std::cin.get();
}
