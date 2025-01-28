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

int n;
vector<int> graph[3030];
int visit[3030];
int start;
int in_cycle[3030];
int ans[3030];

int is_cycle(int now, int pre){
    int ret = 0;
    visit[now] = 1;

    for (auto next : graph[now]){
        if (pre != start && next == start) return ret = 1;
        if (!visit[next]) ret |= is_cycle(next, now);
    }

    return ret;
}

void dfs(int now, int dep){
    ans[now] = dep;
    visit[now] = 1;

    for (auto next : graph[now]){
        if (!in_cycle[next] && !visit[next]){
            dfs(next, dep+1);
        }
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 
    cout.tie(NULL);

    cin >> n; 
    for (int i = 0; i < n; i++){
        int a,b; cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    for (int i = 1; i <= n; i++){
        memset(visit, 0, sizeof visit);
        start = i;
        if (is_cycle(i, -1)) in_cycle[i] = 1;
    }

    for (int i = 1; i <= n; i++){
        memset(visit, 0, sizeof visit);
        if (in_cycle[i]) dfs(i, 0);
    }

    for (int i = 1; i <= n; i++) cout << ans[i] << ' ';

    
    return 0;
}