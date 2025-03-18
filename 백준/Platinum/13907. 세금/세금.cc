#include <bits/stdc++.h>
// #define ll long long
#define int long long
const int inf = 1e18;

using namespace std;

int n,m,k;
int s,d;
vector<pair<int, int>> graph[1010];
int dist[1010][1010];

void dijkstra(int start){
    typedef array<int, 3> arr;
    priority_queue<arr, vector<arr>, greater<>> pq;
    dist[start][0] = 0;
    pq.push({0, start, 0});

    while(!pq.empty()){
        auto [dis, now, cnt] = pq.top();
        pq.pop();

        if (dis > dist[now][cnt]) continue;

        for (auto [next, cst] : graph[now]){
            int cost = dist[now][cnt] + cst;
            if (cost < dist[next][cnt+1]){
                dist[next][cnt+1] = cost;
                pq.push({cost, next, cnt+1});
            }
        }
    }
}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    
    cin >> n >> m >> k;
    cin >> s >> d;
    for (int i = 0; i < m; i++){
        int a,b,c; cin >> a >> b >> c;
        graph[a].push_back({b,c});
        graph[b].push_back({a,c});
    }

    for (int i = 0; i <= n; i++){
        for (int j = 0; j <= n; j++){
            dist[i][j] = inf;
        }
    }

    dijkstra(s);

    int ans = inf;
    for (int i = 1; i < n; i++){
        ans = min(ans, dist[d][i]);
    }
    cout << ans << '\n';

    int w = 0;
    for (int i = 0; i < k; i++){
        int x; cin >> x;
        w += x;
        int ans = inf;
        for (int j = 1; j < n; j++){
            ans = min(ans, dist[d][j] + j*w);
        }
        cout << ans << '\n';
    }


    return 0;
}