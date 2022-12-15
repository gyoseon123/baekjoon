#include <iostream>
using namespace std;

int main()
{
    int in_train[10], out_train[10];
    int a,b;
    for(int i = 0; i < 10; i++)
    {
        cin >> a >> b;
        out_train[i] = a;
        in_train[i] = b;
    }
    int m = 0;
    for(int i = 1; i < 10; i++)
    {
        in_train[i] += in_train[i-1] - out_train[i];
        if(in_train[i] > m) m = in_train[i];
    }
    cout << m;
}