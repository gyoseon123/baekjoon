#include <bits/stdc++.h>
#define ll long long
//#define int long long
const int inf = 1e9;

using namespace std;

int n,m;
int cnt = 1;
int order[10101];
int cut[10101];
vector<int> graph[10101];

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
        } else {
            ret = min(ret, order[next]);
        }
    }
    
    if (order[now] == 1 && child >= 2) cut[now] = 1;
    
    return ret;
}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m;
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

    vector<int> ans;

    for (int i = 1; i <= n; i++){
        if (cut[i]) ans.push_back(i);
    }

    cout << ans.size() << '\n';
    for (auto v : ans) cout << v << ' ';
    
    return 0;
}