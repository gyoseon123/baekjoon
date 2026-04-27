#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <cstring>

#define ll long long

using namespace std;

int n;
int a,b;
vector <int> graph[200002];
int dist[200002];
bool visited[200002];

void dfs(int now, int dep){
    visited[now] = true;
    dist[now] = dep;

    for (auto next : graph[now]){
        if (!visited[next]){
            dfs(next, dep+1);
        }
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    memset(dist, 0, sizeof(dist));
    memset(visited, false, sizeof(visited));

    cin >> n;
    for (int i = 0; i < n-1; i++){
       cin >> a >> b;
       graph[a].push_back(b);
       graph[b].push_back(a);
    }

    dfs(0, 0);

    for (int i = n-1; i >= 1; i--){
        cout << (((n - 1 - dist[i])&1) ? 1 : 0);
    }

    return 0;
}