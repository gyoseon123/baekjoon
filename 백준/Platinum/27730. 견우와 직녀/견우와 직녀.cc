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

int n,m;
vector <pair<int, int>> graph1[100001];
vector <pair<int, int>> graph2[100001];
int subtree1[100001];
int subtree2[100001];
int visit1[100001];
int visit2[100001];
int ans[2];
int ans_idx[2];

int find_sub(vector<pair<int, int>> graph[], int sub[], int visit[], int now){
    int ret = 1;
    visit[now] = 1;
    
    for (auto info : graph[now]){
        int next = info.first;
        if (!visit[next]) ret += find_sub(graph, sub, visit, next);
    }

    return sub[now] = ret;
}

int find_sum(vector<pair<int, int>> graph[], int sub[], int visit[], int now, int s){
    int ret = s;
    visit[now] = 1;

    for (auto info : graph[now]){
        int next = info.first;
        int cost = info.second;
        if (!visit[next]) ret += find_sum(graph, sub, visit, next, cost*sub[next]);
    }

    return ret;
}

int solve(vector<pair<int, int>> graph[], int sub[], int visit[], int now, int s, int idx, int N){
    if (s < ans[idx]){
        ans_idx[idx] = now;
        ans[idx] = s;
    }
    visit[now] = 1;

    for (auto info : graph[now]){
        int next = info.first;
        int cost = info.second;
        if (!visit[next]) solve(graph, sub, visit, next, s + cost*(N - sub[next]*2), idx, N);
    }

    return 0;
}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 
    cout.tie(NULL);

    cin >> n;
    for (int i = 0; i < n-1; i++){
        int u,v,c; cin >> u >> v >> c;
        graph1[u].push_back({v,c});
        graph1[v].push_back({u,c});
    }
    cin >> m;
    for (int i = 0; i < m-1; i++){
        int u,v,c; cin >> u >> v >> c;
        graph2[u].push_back({v,c});
        graph2[v].push_back({u,c});
    }
    ans[0] = ans[1] = 1e18;

    find_sub(graph1, subtree1, visit1, 1);
    memset(visit1, 0, sizeof(visit1));
    int s1 = find_sum(graph1, subtree1, visit1, 1, 0);
    memset(visit1, 0, sizeof(visit1));
    solve(graph1, subtree1, visit1, 1, s1, 0, n);

    find_sub(graph2, subtree2, visit2, 1);
    memset(visit2, 0, sizeof(visit2));
    int s2 = find_sum(graph2, subtree2, visit2, 1, 0);
    memset(visit2, 0, sizeof(visit2));
    solve(graph2, subtree2, visit2, 1, s2, 1, m);

    cout << ans_idx[0] << ' ' << ans_idx[1] << '\n';
    cout << n*ans[1] + m*ans[0] + n*m;

    return 0;
}