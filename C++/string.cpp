#include <iostream>
#include <string>
using namespace std;

//字符串加合

int main()
{
    string str="hello "; //
    str+="gjn"; //分行处理
    cout<<str<<endl;
    str=string(str)+" !!!"; //表明类型
    cout<<str<<endl;

    string str2="how are"s+" you?";  //加上s也可以加和字符串
    cout<<str2<<endl;

    string s;
    s="l\n"
      "o\n"
      "v\n"
      "e\n";
    cout<<s<<endl; //实现分行输出 直接换行即可

    s=R"(123
    456
    789)";
    cout<<s<<endl; //利用R"()"也可
    cin.get();
}