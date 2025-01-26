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
#define ll long long
// #define int long long

using namespace std;

int t,n,m;
int id = 1;
int scc = 1;
vector<vector<int>> ans_scc;
vector<int> graph[101010];
stack<int> stk;
int parent[101010];
int visit[101010];
int indegree[101010];

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
        vector<int> SCC;
        while (1){
            int next = stk.top();
            stk.pop();
            SCC.push_back(next);
            visit[next] = scc;
            if (next == now) break;
        }
        sort(SCC.begin(), SCC.end());
        ans_scc.push_back(SCC);
        scc++;
    }

    return ret;
}

void solve(){
    cin >> n >> m;
    for (int i = 1; i <= n; i++) graph[i].clear();
    memset(parent, 0, sizeof parent);
    memset(visit, 0, sizeof visit);
    memset(indegree, 0, sizeof indegree);
    ans_scc.clear();
    id = 1;
    scc = 1;

    for (int i = 0; i < m; i++){
        int u,v; cin >> u >> v;
        u++;
        v++;
        graph[u].push_back(v);
    }

    for (int i = 1; i <= n; i++){
        if (parent[i] == 0) find_scc(i);
    }

    for (int i = 1; i <= n; i++){
        for (auto next : graph[i]){
            if (visit[i] != visit[next]) indegree[visit[next]]++;
        }
    }

    int ans = 0;

    for (int i = 1; i < scc; i++){
        if (!indegree[i]) ans++;
    }

    if (ans == 1){
        for (int i = 1; i < scc; i++){
            if (!indegree[i]){
                for (auto next : ans_scc[i-1]){
                    cout << next-1 << '\n';
                }
            }
        }
    } else {
        cout << "Confused" << '\n';
    }

    cout << '\n';
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 
    cout.tie(NULL);

    cin >> t;
    while (t--) solve();
    
    return 0;
}