#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <queue>
#include <stack>
#include <unordered_set>
#include <cmath>
#define ll long long

using namespace std;

int a[13];

void sol(int n){
    if (n == 0){
        cout << '-';
        return;
    }

    sol(n-1);
    for (int i = 0; i < a[n-1]; i++){
        cout << ' ';
    }
    sol(n-1);
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    a[0] = 1;
    for (int i = 1; i < 13; i++){
        a[i] = a[i-1]*3;
    }

    int n;
    
    while (cin >> n){
        sol(n);
        cout << '\n';
    }

    return 0;
}