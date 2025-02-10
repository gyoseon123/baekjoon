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
        int idx = -1;
        for (int j = 0; j < i; j++){
            if (a[j] < a[i] && ret < dp[j]){
                ret = dp[j];
                idx = j;
            }
        }
        if (idx != -1){
            dp[i] = ret+1;
            trc[i] = idx;
        }
    }

    int ret = 0;
    int idx = -1;
    for (int i = 0; i < n; i++){
        if (ret < dp[i]){
            ret = dp[i];
            idx = i;
        }
    }

    vector<int> ans;

    for (int i = idx; i != -1; i = trc[i]){
        ans.push_back(a[i]);
    }

    reverse(ans.begin(), ans.end());

    cout << ans.size() << '\n';
    for (int i = 0; i < ans.size(); i++) cout << ans[i] << ' ';
    
    return 0;
}