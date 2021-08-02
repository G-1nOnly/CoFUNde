#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct Person
{
    string name;
    int age;
};
int main()
{
  int size=0;
  vector <string> vs;
  vector <int> va;
  string s;
  int a,i,n,cn;
  while(true)
  {
    printf("Type your command number( 0 or 1 ):");
    cin>>cn;
    cout<<endl;
    if(cn==0) break;
    else
    {
      size=size+1;
      printf("Input your name:");
      cin>>s;
      cout<<endl;
      printf("Input your age:");
      cin>>a;
      cout<<endl;
      vs.push_back(s);
      va.push_back(a);
    }
  }
  n=vs.size();
  Person *person =new Person[size];
  for (i=0;i<n;i++)
  {
    person[i].name=vs[i];
    person[i].age=va[i];
  }
  for(i=0;i<n;i++)
  {
    cout<<"Name: "<<person[i].name<<endl;
    cout<<"Age: "<<person[i].age<<endl;
    cout<<endl;
  }
  delete [] person;
  return 0;
}