#include <bits/stdc++.h>
// #define ll long long
#define int long long

using namespace std;

int n;
int a[1010], trc[1010], dp[1010];

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 
    cout.tie(NULL);

    cin >> n;
    for (int i = 0; i < n; i++) cin >> a[i];

    memset(trc, -1, sizeof trc);
    fill_n(dp, 1010, 1);

    for (int i = 1; i < n; i++){
        int ret = 0;
        for (int j = 0; j < i; j++){
            if (a[j] < a[i] && ret < dp[j]){
                ret = dp[j];
            }
        }
        dp[i] = ret+1;
    }

    int max_dp = *max_element(dp, dp+n);
    cout << max_dp << '\n';
    vector<int> ans;

    int target = max_dp;
    for (int i = n-1; i >= 0; i--){
        if (dp[i] == target){
            ans.push_back(a[i]);
            target--;
            if (target == 0) break;
        }
    }

    reverse(ans.begin(), ans.end());

    for (auto i : ans) cout << i << ' ';

    return 0;
}