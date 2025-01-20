#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#include <cstring>
// #define ll long long
#define int long long

using namespace std;

int n,m;
vector<pair<int, int>> graph[101010];
int table[101010][21];
int dist[101010][21];
int depth[101010];

void dfs(int now, int dep){
    depth[now] = dep;

    for (auto info : graph[now]){
        int next = info.first;
        int cost = info.second;
        if (depth[next] == -1){
            table[next][0] = now;
            dist[next][0] = cost;
            dfs(next, dep+1);
        }
    }
}

int cost_q(int a, int b){
    int ret = 0;

    if (depth[a] < depth[b]) swap(a,b);

    for (int i = 20; i >= 0; i--){
        if ((depth[a] - depth[b]) >= (1 << i)){
            ret += dist[a][i];
            a = table[a][i];
        }
    }

    if (a == b) return ret;

    for (int i = 20; i >= 0; i--){
        if (table[a][i] != table[b][i]){
            ret += dist[a][i] + dist[b][i];
            a = table[a][i];
            b = table[b][i];
        }
    }

    ret += dist[a][0];
    ret += dist[b][0];

    return ret;
}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 
    cout.tie(NULL);

    memset(depth, -1, sizeof depth);
    cin >> n;
    for (int i = 0; i < n-1; i++){
        int u,v,c; cin >> u >> v >> c;
        graph[u].push_back({v,c});
        graph[v].push_back({u,c});
    }

    dfs(1, 0);

    for (int k = 1; k <= 20; k++){
        for (int i = 1; i <= n; i++){
            table[i][k] = table[table[i][k-1]][k-1];
            dist[i][k] = dist[i][k-1] + dist[table[i][k-1]][k-1];
        }
    }

    cin >> m;
    for (int i = 0; i < m; i++){
        int a,b; cin >> a >> b;
        cout << cost_q(a,b) << '\n';
    }
    
    return 0;
}