#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <queue>
#include <stack>
#include <set>
#include <unordered_set>
#include <cmath>
#include <map>
#define ll long long
// #define int long long

using namespace std;

int n,m,v;
int visit[1010];
vector<int> graph[1010];

void bfs(int start){
    queue<int> q;
    q.push(start);
    visit[start] = 1;

    while (!q.empty()){
        int now = q.front();
        q.pop();
        cout << now << ' ';

        for (auto next : graph[now]){
            if (!visit[next]){
                visit[next] = 1;
                q.push(next);
            }
        }
    }
}

void dfs(int now){
    visit[now] = 1;
    cout << now << ' ';
    
    for (auto next : graph[now]){
        if (!visit[next]) dfs(next);
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> m >> v;

    for (int i = 0; i < m; i++){
        int u,v; cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    for (int i = 1; i <= n; i++) sort(graph[i].begin(), graph[i].end());

    dfs(v);
    memset(visit, 0, sizeof visit);
    cout << '\n';
    bfs(v);
    

    return 0;
}