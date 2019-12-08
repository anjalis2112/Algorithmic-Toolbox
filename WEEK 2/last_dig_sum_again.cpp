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

    long long n,m;
    cin>>m>>n;
    long long x=(n+2)%60;
    long long y=(m+1)%60;
    long long fin=arr[x]-arr[y];
    if(fin<0)
        cout<<10+fin;
    else
        cout<<fin;
}
