#include <iostream>

using namespace std;

int a[1010];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n; cin >> n;

    int mx = -1e9;
    int mn = 1e9;

    for (int i = 0; i < n; i++){
        cin >> a[i];
        mx = max(mx, a[i]);
        mn = min(mn, a[i]);
    }

    cout << (mx - mn) * 2; 
}