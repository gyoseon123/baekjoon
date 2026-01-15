#include <bits/stdc++.h>
#define ll long long
//#define int long long
const int inf = 1e9;

using namespace std;

int n,m;
int cnt;
int order[30303];
int cut[30303];
vector<int> graph[30303];

int dfs(int now){
    order[now] = cnt++;

    int ret = order[now];
    int child = 0;

    for (auto next : graph[now]){
        if (!order[next]){
            int low = dfs(next);
            ret = min(ret, low);
            child++;

            if (order[now] != 1 && low >= order[now]) cut[now] = 1;
            if (order[now] == 1 && child >= 2) cut[now] = 1;
        } else {
            ret = min(ret, order[next]);
        }
    }

    return ret;
}

void solve(){    
    cin >> n >> m;

    for (int i = 1; i <= n; i++){
        graph[i].clear();
        order[i] = 0;
        cut[i] = 0;
    }

    for (int i = 0; i < m; i++){
        int u,v; cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    
    for (int i = 1; i <= n; i++){
        if (!order[i]) {
            cnt = 1;
            dfs(i);
        }
    }
    
    int ans = 0;
    
    for (int i = 1; i <= n; i++){
        if (cut[i]) ans = 1;
    }
    
    if (ans) cout << "YES" << '\n';
    else cout << "NO" << '\n';
}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t; cin >> t;

    while (t--) solve();
    return 0;
}