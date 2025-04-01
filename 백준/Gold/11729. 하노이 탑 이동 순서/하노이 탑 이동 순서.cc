#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int n;

void f(int n, int a, int b, int c){
    if (n == 1){
        cout << a << ' ' << c << '\n';
        return;
    }

    f(n-1, a, c, b);
    f(1, a, b, c);
    f(n-1, b, a, c);
}

int main(){

    cin >> n;

    cout << (1<<n)-1 << '\n';
    f(n, 1, 2, 3);

    return 0;
}