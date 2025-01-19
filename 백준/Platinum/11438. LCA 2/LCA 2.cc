#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <queue>
#include <stack>
#include <unordered_set>
#include <cmath>
#include <map>
// #define ll long long
#define int long long

using namespace std;

int n,m;
vector<int> graph[101010];
int table[101010][20]; // i번째 노드의 2^j번째 조상노드
int depth[101010];

int find_lca(int a, int b){
    if (depth[a] < depth[b]) swap(a,b);

    for (int i = 19; i >= 0; i--){
        if ((depth[a] - depth[b]) >= (1 << i)){
            a = table[a][i];
        }
    }

    if (a == b) return a;

    for (int i = 19; i >= 0; i--){
        if (table[a][i] != table[b][i]){
            a = table[a][i];
            b = table[b][i];
        }
    }

    return table[a][0];
}

void dfs(int now, int d){
    depth[now] = d;

    for (auto next : graph[now]){
        if (depth[next] == -1){
            table[next][0] = now;
            dfs(next, d+1);
        }
    }
}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    memset(depth, -1, sizeof depth);

    cin >> n;
    for (int i = 0; i < n-1; i++){
        int a,b; cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    dfs(1, 0);
    for (int k = 1; k < 20; k++){
        for (int i = 1; i <= n; i++){
            table[i][k] = table[table[i][k-1]][k-1];
        }
    }

    cin >> m;
    for (int i = 0; i < m; i++){
        int u,v; cin >> u >> v;
        cout << find_lca(u, v) << '\n';
    }


    return 0;
}