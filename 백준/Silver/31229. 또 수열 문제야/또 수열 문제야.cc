#include <iostream>

using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n; cin >> n;

    for (int i = 1; i <= n*2; i += 2){
        cout << i << ' ';
    }
}