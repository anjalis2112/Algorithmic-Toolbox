#include<iostream>
using namespace std;

int main()
{
    long long arr[60];
    arr[0]=0;
    arr[1]=1;
    for(int i=2;i<60;i++)
    {
        arr[i]=arr[i-1]+arr[i-2];
        arr[i]=arr[i]%10;
    }

    long long n;
    cin>>n;
    long long a=arr[n%60];
    long long b=arr[(n+1)%60];
    cout<<(a*b)%10;


}

