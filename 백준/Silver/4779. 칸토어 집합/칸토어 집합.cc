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

void sol(int n){
    if (n == 0){
        cout << '-';
        return;
    }

    sol(n-1);
    for (int i = 0; i < (int)pow(3, n-1); i++){
        cout << ' ';
    }
    sol(n-1);
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    
    while (cin >> n){
        sol(n);
        cout << '\n';
    }

    return 0;
}