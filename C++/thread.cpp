#include <iostream>
#include <thread>

static bool check_finished=true;

void dowork()
{
    using namespace std::literals::chrono_literals; //方便表示时间

    std::cout<<"Started thread id:"<<std::this_thread::get_id()<<std::endl;

    while(check_finished)
    {
        std::cout<<"working..."<<std::endl;
        std::this_thread::sleep_for(1s);
    }
}

int main()
{
    std::thread worker(dowork);

    std::cin.get();
    check_finished=false; //当按下回车后结束

    worker.join(); //main thread 等待 worker thread 结束
    std::cout<<"Finished"<<std::endl;
    std::cout<<"Started thread id:"<<std::this_thread::get_id()<<std::endl; //不同线程

    std::cin.get();
}

