#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#define ll long long

using namespace std;

int n,m;
vector<ll> t;

bool check(ll x){
    ll ret = 0;
    for (int i = 0; i < n; i++){
        ret += x/t[i];
        if (ret >= m) return 1;
    }
    return 0;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 
    cout.tie(NULL);
    cin >> n >> m;

    for (int i = 0; i < n; i++){
        ll x; cin >> x; 
        t.push_back(x);
    }

    ll left = 0;
    ll right = (ll)1e18+1;

    while (left + 1 < right){
        ll mid = (left+right)/2;
        
        if (check(mid)) right = mid;
        else left = mid;
    }
    
    cout << right;

    return 0;
}