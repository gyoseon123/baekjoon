#include <bits/stdc++.h>
// #define ll long long
#define int long long
const int inf = 1e9;

using namespace std;

int n;
stack<pair<int, int>> stk;
int ans[1010101];

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    memset(ans, -1, sizeof ans);
    cin >> n;
    for (int i = 0 ; i < n; i++){
        int x; cin >> x;
        while (!stk.empty() && stk.top().first < x){
            ans[stk.top().second] = x;
            stk.pop();
        }
        stk.push({x, i});
    }

    for (int i = 0; i < n; i++) cout << ans[i] << ' ';

    return 0;
}