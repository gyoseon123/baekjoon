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

int id = 1;
int parent[10101];
int v,e;
bool visit[10101];
stack<int> stk;
vector<int> graph[10101];
vector<vector<int>> ans_scc;

int dfs(int now){
    parent[now] = id++;
    stk.push(now);

    int par = parent[now];
    for (auto next : graph[now]){
        if (parent[next] == 0){
            par = min(par, dfs(next));
        } else if (!visit[next]){
            par = min(par, parent[next]);
        }
    }

    if (par == parent[now]){
        vector<int> scc;
        while (now){
            int next = stk.top();
            stk.pop();
            scc.push_back(next);
            visit[next] = 1;
            if (next == now) break;
        }
        sort(scc.begin(), scc.end());
        ans_scc.push_back(scc);
    }
    return par;
}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 
    cout.tie(NULL);

    cin >> v >> e;
    for (int i = 0; i < e; i++){
        int u,v; cin >> u >> v;
        graph[u].push_back(v);
    }

    for (int i = 1; i <= v; i++){
        if (parent[i] == 0) dfs(i);
    }

    sort(ans_scc.begin(), ans_scc.end(), [](vector<int> a, vector<int> b){
        return a[0] < b[0];
    });

    cout << ans_scc.size() << '\n';
    for (auto lst : ans_scc){
        for (int i = 0; i < lst.size(); i++){
            cout << lst[i] << ' ';
        }
        cout << -1 << '\n';
    }
    
    return 0;
}