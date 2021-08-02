#include <iostream>
#include <chrono>
#include <thread>

int main()
{
    using namespace std::literals::chrono_literals;

    auto start = std::chrono::high_resolution_clock::now();

    std::this_thread::sleep_for(1s);// 更换此处则可测试任意过程

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<float> duration = end-start;
    std::cout<<duration.count()<<"s"<<std::endl;

    std::cin.get();
}

