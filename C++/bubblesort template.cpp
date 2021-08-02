#include <iostream>

template <typename T>
void swap(T&x,T&y)
{
    T temp = x;
    x = y;
    y = temp;
}

template <typename T>
void bubblesort(T a[],int n)
{
    int i = n-1;
    while(i>0)
    {
        int index = 0;
        for (int j = 0; j<i; j++)
        {
            if(a[j+1]<a[j]) {
                swap(a[j+1],a[j]);
                index = j;
            }
        }
        i = index;
    }
}

int main()
{
    int arr[9] = {1,3,5,4,9,8,2,7,6};
    bubblesort(arr,9);
    for (int i = 0;i < 9;i++)
    {
        std::cout<<arr[i]<<std::endl;
    }
    std::cin.get();
}