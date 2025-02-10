#include <bits/stdc++.h>
// #define ll long long
#define int long long
const int inf = 1e9;

using namespace std;

int n,m;
vector<array<int, 3>> edges;
int dist[505];

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 
    cout.tie(NULL);

    fill_n(dist, 505, inf);
    dist[1] = 0;

    cin >> n >> m;
    for (int i = 0; i < m; i++){
        int a,b,c; cin >> a >> b >> c;
        edges.push_back({a,b,c});
    }

    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            auto [now, next, cost] = edges[j];
            if (dist[now] != inf && dist[next] > dist[now] + cost){
                dist[next] = dist[now] + cost;
                if (i == n-1){
                    cout << -1;
                    return 0;
                }
            }
        }
    }

    for (int i = 2; i <= n; i++){
        cout << ((dist[i] == inf) ? -1 : dist[i]) << '\n';
    }

    return 0;
}