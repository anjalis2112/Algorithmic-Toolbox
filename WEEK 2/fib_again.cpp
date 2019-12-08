#include<iostream>
using namespace std;


long long pisano(long long m) {

    long long a=0,b=1,c=a+b;

    for (int i=0;i<m*m;i++)
        {
            c=(a+b)%m;
            a=b;
            b=c;

            if(a==0&&b==1)
            return i+1;


        }

}

void fib_again(long long n, long long m)
{
    long long rem=n%pisano(m);
    int count=0;
    long long first=0;
    long long second=1;
    long long res;
    if(rem>1){
    for(int i=1;i<rem;i++)
    {
        res=(first+second)%m;
        first=second;
        second=res;

    }

    cout<<res;
    }

    else
    cout<<rem;

}

int main()
{
    long long n,m;
    cin>>n>>m;
    fib_again(n,m);

}
