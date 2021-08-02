#include <iostream>

int main()
{
    int* array=new int[50]; //动态一维数组 指向int
    int** array2d = new int*[50]; //动态二维数组 指向(指向int的指针)
    for (int i=0;i<50;i++)
    {
        array2d[i]=new int[50]; //二维数组是指向指针的指针 故是对指针的操作
    }

    for (int j=0;j<50;j++)
    {
        delete[] array2d[j];  //二维数组需要遍历一个一个delete
    }
    delete[] array2d; //遍历后再delete

    std::cin.get();
}

