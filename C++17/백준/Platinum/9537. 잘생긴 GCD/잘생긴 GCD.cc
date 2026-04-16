#include <bits/stdc++.h>
#define ll long long
//#define int long long
const int inf = 1e9;

using namespace std;

int t;
int n;
ll a[1010101];

ll gcd(int a, int b){
    if (b == 0) return a;
    else return gcd(b, a%b);
}

ll go(int l, int r){
    if (l == r) return a[l];

    int mid = (l+r)/2;

    vector<pair<ll, int>> left_gcd;
    vector<pair<ll, int>> right_gcd;
    left_gcd.push_back({a[mid], mid});
    right_gcd.push_back({a[mid], mid});

    for (int i = mid-1; i >= l; i--){
        ll g = gcd(left_gcd.back().first, a[i]);
        if (g != left_gcd.back().first) left_gcd.push_back({g, i});
        else left_gcd.back().second = i;
    }

    for (int i = mid+1; i <= r; i++){
        ll g = gcd(right_gcd.back().first, a[i]);
        if (g != right_gcd.back().first) right_gcd.push_back({g, i});
        else right_gcd.back().second = i;
    }

    ll ret = a[mid];
    for (auto [gl, l_idx] : left_gcd){
        for (auto [gr, r_idx] : right_gcd){
            ret = max(ret, gcd(gl, gr) * (r_idx - l_idx + 1));
        }
    }

    return max(ret, max(go(l, mid), go(mid+1, r)));
}

void solve(){
    cin >> n;
    for (int i = 0; i < n; i++) cin >> a[i];
    cout << go(0, n-1) << '\n';
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> t;
    while (t--) solve();
    
    return 0;
}