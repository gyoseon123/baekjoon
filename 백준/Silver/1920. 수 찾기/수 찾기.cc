#include <bits/stdc++.h>
// #define ll long long
#define int long long
const int inf = 1e9;

using namespace std;

int n, m;
int a[101010];

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n;
    for (int i = 0; i < n; i++) cin >> a[i];
    sort(a, a+n);
    cin >> m; 
    for (int i = 0; i < m; i++){
        int x; cin >> x;
        int left = lower_bound(a, a+n, x) - a;
        int right = upper_bound(a, a+n, x) - a;
        cout << !(!(right - left)) << '\n';
    }   

    return 0;
}