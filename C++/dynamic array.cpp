#include <iostream>
using namespace std;

class myArr
{
    int *pV;
public:
    myArr(){pV=NULL;};
    myArr(int n){pV=new int [n];}
    ~myArr(){if (pV!=NULL) delete []pV;}
    int& operator[](int i)
    {
        return pV[i];
    }
};

int main()
{
    int n=12;
    myArr arr(n);
    for (int i=0;i<n;i++){arr[i]=i;}
    for (int i=0;i<n;i++)
        cout<<"arr ["<<i<<"] = "<<arr[i]<<endl;
    return 0;
}