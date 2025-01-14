#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <queue>
#include <stack>
#include <unordered_set>
#include <cmath>
#include <map>
// #define ll long long
#define int long long

using namespace std;

int n,m,k;
map <int, int> mp;

void change(int key, int val){
    auto iter = mp.lower_bound(key);
    int r = iter -> first;
    int l = (--iter) -> first;

    if (mp.find(r) == mp.end()){
        if (abs(l - key) <= k) mp[l] = val;
        return;
    }

    if (mp.find(r) == mp.begin()){
        if (abs(r - key) <= k) mp[r] = val;
        return;
    }

    if (abs(l - key) > k && abs(r - key) > k) return;

    if (abs(l - key) < abs(r - key)) mp[l] = val;
    if (abs(l - key) > abs(r - key)) mp[r] = val;

    return;
}

void find_query(int key){
    auto iter = mp.lower_bound(key);
    int r = iter -> first;
    int l = (--iter) -> first;

    if (mp.find(r) == mp.end()){
        if (abs(l - key) <= k) cout << mp[l] << '\n';
        else cout << -1 << '\n';
        return;
    }

    if (mp.find(r) == mp.begin()){
        if (abs(r - key) <= k) cout << mp[r] << '\n';
        else cout << -1 << '\n';
        return;
    }

    if (abs(l - key) == abs(r - key)){
        cout << '?' << '\n';
        return;
    }
    if (abs(l - key) > k && abs(r - key) > k){
        cout << -1 << '\n';
        return;
    }

    if (abs(l - key) < abs(r - key)) cout << mp[l] << '\n';
    else cout << mp[r] << '\n';

    return;
}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> n >> m >> k;
    for (int i = 0; i < n; i++){
        int a,b; cin >> a >> b;
        mp[a] = b;
    }

    for (int i = 0; i < m; i++){
        int q; cin >> q;
        if (q == 1){
            int a,b; cin >> a >> b;
            mp[a] = b;
        } else if (q == 2){
            int a,b; cin >> a >> b;
            change(a,b);
        } else {
            int a; cin >> a;
            find_query(a);
        }
    }

    return 0;
}