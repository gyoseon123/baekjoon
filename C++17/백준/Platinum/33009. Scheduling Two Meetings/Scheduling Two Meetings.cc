#include <bits/stdc++.h>
#define ll long long
//#define int long long
const int inf = 1e9;

using namespace std;

pair<int, int> comp(pair<int, int> a, pair<int, int> b){
    if (a.first == b.first) return (a.second < b.second ? a : b);
    return max(a, b);
}

int n,m;
pair<int, int> dp[(1 << 20)];
int a[202020];

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m;

    for (int i = 0; i < (1 << m); i++){
        dp[i] = {-1, inf};
    }

    int all_one = -1;
    for (int i = 1; i <= n; i++){
        string s; cin >> s;
        int x = 0;
        for (int j = 0; j < m; j++){
            if (s[j] == 'Y') x |= (1 << j);
        }
        dp[x] = {__builtin_popcount(x), i};
        a[i] = x;
        if (all_one == -1 && x == (1 << m) - 1){
            all_one = i;
        }
    }

    if (all_one != -1){
        int max_bit = -1;
        for (int i = 1; i <= n; i++){
            if (i != all_one){
                max_bit = max(max_bit, __builtin_popcount(a[i]));
            }
        }

        for (int i = 1; i <= n; i++){
            if (__builtin_popcount(a[i]) == max_bit && i != all_one){
                if (i < all_one) cout << i << ' ' << all_one << '\n';
                else cout << all_one << ' ' << i << '\n';
                return 0;
            }
        }
    }


    for (int i = (1 << m)-1; i >= 0; i--){
        for (int j = 0; j < m; j++){
            dp[i] = comp(dp[i], dp[i|(1 << j)]);
        }
    }

    int max_bit = -1;
    for (int i = 1; i <= n; i++){
        int now = a[i];
        int nxt = (1 << m) - 1 - now;
        pair<int, int> super = dp[nxt];
        max_bit = max(max_bit, super.first - __builtin_popcount(nxt));
    }

    pair<int, int> ans = {inf, inf};
    for (int i = 1; i <= n; i++){
        int now = a[i];
        int nxt = (1 << m) - 1 - now;
        pair<int, int> super = dp[nxt];
        pair<int, int> tmp;
        if (super.second < i) tmp = {super.second, i};
        else tmp = {i, super.second};

        int val = super.first - __builtin_popcount(nxt);
        if (max_bit == val){
            ans = min(ans, tmp);
        }
    }

    if (ans.first == inf) cout << "No" << '\n';
    else cout << ans.first << ' ' << ans.second << '\n';
    
    return 0;
}