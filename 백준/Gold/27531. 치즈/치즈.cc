#include <bits/stdc++.h>
// #define ll long long
#define int long long
const int inf = 1e9;

using namespace std;

int n;
vector<pair<int, int>> graph[202020];
int visited[202020];
int cost[202020];
vector<int> a;

int sol(vector<int> arr){
    int ret = 0;
    int sum = 0;

    int m = arr.size();
    if (m == 0) return 0;
    if (m == 1) return arr[0];
    if (m == 2) return min(arr[0], arr[1]);
    if (m == 3) return arr[0] + arr[1] + arr[2] - max(arr[0], max(arr[1], arr[2]));
    int dp[m];
    dp[0] = arr[0];
    dp[1] = arr[1];
    dp[2] = arr[0] + arr[2];
    for (int i = 3; i < m-1; i++){
        dp[i] = max(dp[i-2], dp[i-3]) + arr[i];
    }

    for (int i = 0; i < m-1; i++){
        ret = max(ret, dp[i]);
        dp[i] = 0;
        sum += arr[i];
    }
    sum += arr[m-1];

    dp[1] = arr[1];
    dp[2] = arr[2];
    for (int i = 3; i < m; i++){
        dp[i] = max(dp[i-2], dp[i-3]) + arr[i];
    }

    for (int i = 1; i < m; i++){
        ret = max(ret, dp[i]);
    }
    
    return sum - ret;
}

void dfs(int now){
    for (auto [next, idx] : graph[now]){
        if (!visited[idx]){
            visited[idx] = 1;
            a.push_back(cost[idx]);
            dfs(next);
        }
    }
}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);


    cin >> n;
    int ans = 0;
    for (int i = 0; i < n; i++){
        int a, b, p; cin >> a >> b >> p;
        cost[i] = p;
        graph[a].push_back({b,i});
        graph[b].push_back({a,i});
    }

    for (int i = 1; i <= n; i++){
        a.clear();
        dfs(i);
        ans += sol(a);
    }
    
    cout << ans;

    return 0;
}