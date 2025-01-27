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

int n,m;
int id = 1;
int scc_cnt = 1;
vector<int> graph[20202];
vector<vector<int>> SCC;
pair<int, int> p[20202];
stack<int> stk;
int parent[20202];
int visit[20202];
int res[10101];

int oppo(int x){
    return (x&1) ? (x+1) : (x-1);
}

int find_scc(int now){
    int ret = parent[now] = id++;
    stk.push(now);

    for (auto next : graph[now]){
        if (parent[next] == 0) ret = min(ret, find_scc(next));
        else if (!visit[next]) ret = min(ret, parent[next]);
    }

    if (ret == parent[now]){
        vector<int> scc;
        while (1){
            int next = stk.top();
            stk.pop();
            scc.push_back(next);
            visit[next] = scc_cnt;
            if (next == now) break;
        }
        SCC.push_back(scc);
        scc_cnt++;
    }

    return ret;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 
    cout.tie(NULL);

    cin >> n >> m;
    for (int i = 0; i < m; i++){
        int a,b; cin >> a >> b;
        a = (a < 0) ? ((-a)*2) : (a*2-1);
        b = (b < 0) ? ((-b)*2) : (b*2-1);

        graph[oppo(a)].push_back(b);
        graph[oppo(b)].push_back(a);
    }

    for (int i = 1; i <= 2*n; i++){
        if (parent[i] == 0) find_scc(i);
    }

    int ans = 1;

    for (int i = 0; i < SCC.size(); i++){
        set<int> s;
        for (auto next : SCC[i]){
            if (s.count(oppo(next))) ans = 0;
            s.insert(next);
        }
    }

    if (!ans){
        cout << ans;
        return 0;
    }
    cout << ans << '\n';

    for (int i = 1; i <= n; i++) cout << (visit[i*2-1] < visit[i*2]) << ' ';
       
    return 0;
}