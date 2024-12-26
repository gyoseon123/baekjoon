#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>

using namespace std;

int n,m,r;
vector <int> graph[100001];
int visited[100001];
int cnt = 1;

void dfs(int now){
    visited[now] = cnt;
    cnt++;

    for (auto next : graph[now]){
        if (!visited[next]){
            dfs(next);
        }
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 
    cout.tie(NULL);

    cin >> n >> m >> r;
    for (int i = 0; i < m; i++){
        int u,v; cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    for (int i = 0; i < 100001; i++){
        sort(graph[i].begin(), graph[i].end());
    }

    dfs(r);

    for (int i = 1; i <= n; i++){
        cout << visited[i] << '\n';
    }

    return 0;
}