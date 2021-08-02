#include <iostream>
#include <string>
#include <cstdio>
using namespace std;

class MyComplex
{
    double real, imag;
public:
    // constructors
    MyComplex() {real = imag = 0;}
    MyComplex(double re, double im)
    { real = re; imag = im;}
    MyComplex(string str);
    MyComplex(MyComplex* pc)
    {real = pc->real; imag = pc->imag;}
    // Equal
    void Equal(MyComplex c2)
    {real = c2.real; imag = c2.imag;}

    string ToStr(); // for cout

    // Add
    MyComplex Add(MyComplex c2);
    // Minus
    MyComplex Minus(MyComplex c2);
    MyComplex Multiply(MyComplex c2);
    MyComplex Divide(MyComplex c2);

};

string MyComplex::ToStr()
{
    char str2[255];
    if (imag > 0)
        sprintf(str2, "%lf + %lfi", real, imag);
    else if (imag < 0)
        sprintf(str2, "%lf - %lfi", real, -imag);
    else
        sprintf(str2, "%lf", real);
    string str = str2;
    return str;
}

MyComplex MyComplex::Add(MyComplex c2)
{
    return MyComplex(real + c2.real, imag + c2.imag);
}

MyComplex MyComplex::Minus(MyComplex c2)
{
    return MyComplex(real - c2.real, imag - c2.imag);
}

MyComplex MyComplex::Multiply(MyComplex c2)
{
    return MyComplex(real * c2.real-imag*c2.imag, imag*c2.real + real*c2.imag);
}

MyComplex MyComplex::Divide(MyComplex c2)
{
    return MyComplex((real * c2.real+imag*c2.imag)/(c2.imag*c2.imag+c2.real*c2.real),
                     (imag*c2.real - real*c2.imag)/(c2.imag*c2.imag+c2.real*c2.real));
}

MyComplex::MyComplex(string str)
{
    int pos;
    // 1: erase spaces
    while ((pos = str.find(' ')) != string::npos)
        str.erase(pos, 1);
    // 2: erase i
    while ((pos = str.find('i')) != string::npos)
        str.erase(pos, 1);
    // 3: find '+', then real and imag
    pos = str.find('+');
    real = stod(str.substr(0, pos));
    imag = stod(str.substr(pos+1));
}

int main()
{
    MyComplex c0, c1(0, 1), c2("3+4i"), c3(&c1);
    cout << "c0 = " << c0.ToStr() << endl;
    cout << "c1 = " << c1.ToStr() << endl;
    cout << "c2 = " << c2.ToStr() << endl;
    cout << "c3 = " << c3.ToStr() << endl;
    c3.Equal(c1.Add(c2));
    cout << "c3 = c1 + c2 = " << c3.ToStr() << endl;
    c3.Equal(c1.Minus(c2));
    cout << "c3 = c1 - c2 = " << c3.ToStr() << endl;
    c3.Equal(c1.Multiply(c2));
    cout << "c3 = c1 * c2 = " << c3.ToStr() << endl;
    c3.Equal(c1.Divide(c2));
    cout << "c3 = c1 / c2 = " << c3.ToStr() << endl;
    return 0;
}
