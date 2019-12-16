#include<iostream>
using namespace std;

void change(int n)
{


    int count=0;


        while(n>=10)
        {
            n=n-10;
            count++;
        }

        while(n>=5)
        {
            n=n-5;
            count++;
        }

        while(n>=1)
        {
            n=n-1;
            count++;
        }

        cout<<count;
        return;

}

int main()
{
    int n;
    cin>>n;
    change(n);
}
