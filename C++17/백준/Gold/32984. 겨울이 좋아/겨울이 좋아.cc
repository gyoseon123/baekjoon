#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>

#define ll long long

using namespace std;

ll n;
ll a[200001];
ll b[200001];
ll c[200001];

ll check(ll x){
    ll ret = 0;

    for (int i = 0; i < n; i++){
        ret += max(0ll, c[i] - x);
    }

    return ret <= x;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    cin >> n;
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < n; i++) cin >> b[i];
    for (int i = 0; i < n; i++) c[i] = (a[i] + b[i] - 1)/b[i];

    ll left = 0;
    ll right = *max_element(c, c+n) + 1;

    while (left + 1 < right){
        ll mid = (left + right)/2;

        if (check(mid)) right = mid;
        else left = mid;
    }

    cout << right;

    return 0;
}