#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>

using namespace std;




int n,m,k;
int inf = (int)1e9;
vector <vector<pair<int, int>>> graph (20001);
int dist[20001];
priority_queue <pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> q;

int dijkstra(int start_node){
    dist[start_node] = 0;
    q.push({0,start_node});
    while (!q.empty()){
        int dis = q.top().first;
        int v = q.top().second;
        q.pop();

        if (dis > dist[v]) continue;
        for (int i = 0; i < graph[v].size(); i++){
            int next_node = graph[v][i].first;
            int d = graph[v][i].second;
            int cost = dist[v] + d;
            if (cost < dist[next_node]){
                dist[next_node] = cost;
                q.push({cost, next_node});
            }
        }
    }
    return 0;
}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    fill(dist, dist + 20001, inf);
    cin >> n >> m;
    cin >> k;
    for (int i = 0; i < m; i++){
        int a,b,c;
        cin >> a >> b >> c;
        graph[a].push_back({b,c});  
    }
    dijkstra(k);
    for (int i = 1; i < n+1; i++){
        if (dist[i] != inf) cout << dist[i] << '\n';
        else cout << "INF\n";
    }
    return 0;
}

