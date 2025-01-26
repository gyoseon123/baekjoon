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
#include <cmath>
// #define ll long long
#define int long long

using namespace std;

int ans = 0;
int n,m,s,p;
int id = 1, scc_cnt = 1;
vector<vector<int>> SCC;
vector<int> new_graph[505050];
vector<int> graph[505050];
stack<int> stk;
int visit[505050];
int indegree[505050];
int parent[505050];
int cost[505050];
int scc_cost[505050];
int rest[505050];
int new_rest[505050];
int dfs_visit[505050];

void dfs(int now, int cost){
    dfs_visit[now] = cost;
    if (new_rest[now]){
        ans = max(ans, cost);
    }

    for (auto next : new_graph[now]){
        if (!dfs_visit[next]){
            dfs(next, cost + scc_cost[next]);
        } else if (cost + scc_cost[next] > dfs_visit[next]){
            dfs(next, cost + scc_cost[next]);
        }
    }
}

int find_scc(int now){
    int ret = parent[now] = id++;
    stk.push(now);

    for (auto next : graph[now]){
        if (parent[next] == 0){
            ret = min(ret, find_scc(next));
        } else if (!visit[next]){
            ret = min(ret, parent[next]);
        }
    }

    if (ret == parent[now]){
        vector<int> sccc;
        while (1){
            int next = stk.top();
            stk.pop();
            sccc.push_back(next);
            visit[next] = scc_cnt;
            if (next == now) break;
        }
        SCC.push_back(sccc);
        scc_cnt++;
    }

    return ret;
}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 
    cout.tie(NULL);

    cin >> n >> m;
    for (int i = 0; i < m; i++){
        int u,v; cin >> u >> v;
        graph[u].push_back(v);
    }

    for (int i = 1; i <= n; i++) cin >> cost[i];

    cin >> s >> p;
    for (int i = 0; i < p; i++){
        int x; cin >> x;
        rest[x] = 1;
    }

    for (int i = 1; i <= n; i++){
        if (parent[i] == 0) find_scc(i);
    }

    for (int i = 1; i <= n; i++){
        scc_cost[visit[i]] += cost[i];
        new_rest[visit[i]] |= rest[i];
        for (auto next : graph[i]){
            if (visit[i] != visit[next]){
                new_graph[visit[i]].push_back(visit[next]);
            }
        }
    }

    dfs(visit[s], scc_cost[visit[s]]);

    cout << ans;

    return 0;
}