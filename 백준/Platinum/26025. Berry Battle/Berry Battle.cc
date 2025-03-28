#include <bits/stdc++.h>
// #define ll long long
#define int long long
const int inf = 1e9;

using namespace std;

int n;
int mx;
int mx_node;
int visited[303030];
vector<int> graph[303030];

void dfs(int now, int dep){
    visited[now] = 1;

    if (dep > mx){
        mx = dep;
        mx_node = now;
    }
    
    for (auto next : graph[now]){
        if (!visited[next]){
            dfs(next, dep+1);
        }
    }
}

void dfs2(int now, int s){
    visited[now] = 1;

    for (auto next : graph[now]){
        if (!visited[next] && next != s){
            cout << next << ' ';
            dfs2(next, s);
        }
    }
}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n;
    for (int i = 0; i < n-1; i++){
        int u, v; cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    dfs(1, 0);
    mx = 0;
    memset(visited, 0, sizeof visited);
    dfs(mx_node, 0);

    if (mx < 3){
        cout << "NO";
        exit(0);
    }

    cout << "YES" << '\n';
    memset(visited, 0, sizeof visited);
    int next_node = graph[mx_node][0];
    sort(graph[next_node].begin(), graph[next_node].end(), [](int a, int b){
        return graph[a].size() < graph[b].size();
    });
    dfs2(next_node, mx_node);
    cout << graph[mx_node][0] << ' ' << mx_node;
    
    return 0;
}