#include <bits/stdc++.h>
// #define ll long long
#define int long long

using namespace std;

int n,m;
vector<int> graph[101010];
int s[101010], e[101010];
int tree[101010];
int cnt;

void dfs(int now){
    s[now] = ++cnt;
    for (auto next : graph[now]) dfs(next);
    e[now] = cnt;
}

void update(int idx, int val){
    for (int i = idx; i <= n; i += (i&-i)) tree[i] += val;
}

int sum(int idx){
    int ret = 0;
    for (int i = idx; i > 0; i -= (i&-i)) ret += tree[i];
    return ret;
}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m;
    for (int i = 1; i <= n; i++){
        int x; cin >> x;
        if (x == -1) continue;
        graph[x].push_back(i);
    }

    dfs(1);

    for (int i = 0; i < m; i++){
        int op; cin >> op;
        if (op == 1){
            int a,b; cin >> a >> b;
            update(s[a], b); update(e[a]+1, -b);
        } else {
            int a; cin >> a;
            cout << sum(s[a]) << '\n';
        }
    }

    return 0;
}