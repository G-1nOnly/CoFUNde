#include <iostream>

//#if 1 true #if 0 false
#if 0
int main()
{
    std::cout << "Hello, World!" << std::endl;
    std::cin.get();
    return 0;
}
#endif

#if 1
int main()
{
    std::cin.get();
    return 0;
}
#endif
