#include <bits/stdc++.h>
#define ll long long
#define ld long double
//#define int long long
const ll inf = 1e18;

using namespace std;

int n,m,k;
ll dist1[202020];
ll distn[202020];
ld p[202020];
vector<pair<int, int>> graph[202020];

void dijkstra(int start, ll dist[]){
    for (int i = 0; i <= n; i++) dist[i] = inf;
    
    dist[start] = 0;
    priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<>> pq;
    pq.push({0, start});
    
    while (!pq.empty()){
        auto [dis, now] = pq.top(); pq.pop();

        if (dis > dist[now]) continue;

        for (auto [next, cst] : graph[now]){
            ll cost = dist[now] + cst;
            if (cost < dist[next]){
                dist[next] = cost;
                pq.push({cost, next});
            }
        }
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m >> k;

    for (int i = 0; i < m; i++){
        int u,v,c; cin >> u >> v >> c;
        graph[u].push_back({v,c});
        graph[v].push_back({u,c});
    }

    int flg = 0;
    for (int i = 0; i < k; i++){
        int u;
        ld pr;
        cin >> u >> pr;
        p[u] = pr;
        if (abs(p[u] - 1) < 1e-10) flg = 1;
    }

    if (!flg) {
        cout << "impossible" << '\n';
        exit(0);
    }

    dijkstra(1, dist1);
    dijkstra(n, distn);

    vector<pair<ll, int>> store;
    for (int i = 1; i <= n; i++){
        if (p[i] != 0){
            store.push_back({dist1[i] + distn[i], i});
        }
    }

    sort(store.begin(), store.end());

    ld ans = 0;
    ld pr = 1;
    for (auto [d, node] : store){
        ans += (pr*p[node]*d);
        pr *= (1 - p[node]);
    }

    cout << fixed;
    cout.precision(30);
    cout << ans << '\n';
    
    return 0;
}