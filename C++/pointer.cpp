#include <iostream>
using namespace std;
int* bar()
{
    static int winky = 5;
    cout << "winky = " << winky << endl;
    return(&winky);
}
int main()
{
    int *pinky;
    pinky = bar();
    cout << "*pinky = " << *pinky << endl;
    *pinky = 6;
    bar();
    return 0;
}
