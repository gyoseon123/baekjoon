#include <bits/stdc++.h>
#define ll long long
//#define int long long
const int inf = 1e9;

using namespace std;

ll dp[22][202];
vector<int> digits;

void find_digits(ll x){
    digits.clear();
    while (x){
        digits.push_back(x%10);
        x /= 10;
    }
}

ll go(int cnt, ll sum, int lim){
    if (cnt == -1) return sum;

    ll &cache = dp[cnt][sum];
    if (cache != -1 && !lim) return cache;

    ll ret = 0;
    int bound = (lim ? digits[cnt] : 9);

    for (int i = 0; i <= bound; i++){
        ret += go(cnt - 1, sum + i, lim&&(i == bound));
    }

    if (!lim) cache = ret;

    return ret;
}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t = 1;
    while (t--){
        ll a,b; cin >> a >> b;
        memset(dp, -1, sizeof dp);
        find_digits(a-1);
        ll lower = go(digits.size()-1, 0, 1);
        memset(dp, -1, sizeof dp);
        find_digits(b);
        ll upper = go(digits.size()-1, 0, 1);
        
        cout << upper - lower << '\n';
    }
    
    return 0;
}