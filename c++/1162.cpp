#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <tuple>



using namespace std;

long long n,m,k;
long long inf = (long long)1e18;
vector <vector<pair<long long, long long>>> graph (10001);
long long dist[10001][21];
priority_queue <tuple<long long, long long, long long>, vector<tuple<long long, long long, long long>>, greater<tuple<long long, long long, long long>>> q;

int dijkstra(int start_node){
    dist[start_node][0] = 0;
    q.push(make_tuple(0, start_node, 0)); 
    while (!q.empty()){
        long long dis = get<0>(q.top());
        long long v = get<1>(q.top());
        long long depth = get<2>(q.top());
        q.pop();

        if (dis > dist[v][depth]) continue;
        for (long long i = 0; i < graph[v].size(); i++){
            long long next_node = graph[v][i].first;
            long long d = graph[v][i].second;
            long long cost = dist[v][depth] + d;
            if (cost < dist[next_node][depth]){
                dist[next_node][depth] = cost;
                q.push(make_tuple(cost, next_node, depth));
            }
            if (depth < k && cost-d < dist[next_node][depth+1]){
                dist[next_node][depth+1] = cost-d;
                q.push(make_tuple(cost-d, next_node, depth+1));
            }
        }
    }
    return 0;
}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    fill(&dist[0][0], &dist[10000][20]+1, inf);
    cin >> n >> m >> k;
    for (int i = 0; i < m; i++){
        int a,b,c;
        cin >> a >> b >> c;
        graph[a].push_back({b,c});  
        graph[b].push_back({a,c});
    }
    dijkstra(1);
    long long p_m = inf;
    for (int i = 0; i < k+1; i++) p_m = min(p_m, dist[n][i]);
    cout << p_m;
    return 0;
}

