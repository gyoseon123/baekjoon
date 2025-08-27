#include <bits/stdc++.h>
// #define ll long long
#define int long long
const int inf = 1e9;

using namespace std;

// Tree tree(n, graph) 형태로 선언. graph 형식은 vector<int> graph[], vector<pair<int, int>> graph[], vector<vector<int>> graph, vector<vector<pair<int, int>> graph 지원
// 가중치 없는 graph 넣으면 가중치 1로 알아서 세팅해줌
// 트리지름 O(N), 지름위의 노드찾기 O(N), 노드 v에서 모든곳으로의 거리 O(N), LCA O(NlogN) + 쿼리당 O(logN), 두 정점사이의 거리 O(NlogN) + 쿼리당 O(logN) 지원
class Tree{
private: 
    vector<vector<pair<int, int>>> graph;
    vector<vector<int>> table;
    vector<vector<int>> dist;
    vector<int> diameterNodes;
    vector<int> depth;

    int n;
    int diameter;

    pair<int, pair<int, vector<int>>> Bfs(int start){
        vector<int> dist(n+1, -1);
        queue<int> q;
        q.push(start);
        dist[start] = 0;
        int farNode = start;

        while (!q.empty()){
            int now = q.front(); q.pop();
            for (auto [next, cost] : graph[now]){
                if (dist[next] == -1){
                    dist[next] = dist[now] + cost;
                    q.push(next);
                    if (dist[next] > dist[farNode]){
                        farNode = next;
                    }
                }
            }
        }

        return {farNode, {dist[farNode], dist}};
    }

    void Dfs(int now, int dep){
        depth[now] = dep;
    
        for (auto [next, cost] : graph[now]){
            if (depth[next] == -1){
                table[next][0] = now;
                dist[next][0] = cost;
                Dfs(next, dep+1);
            }
        }
    }
public:
    Tree(int n, vector<int> g[]){
        this->n = n;
        this->graph.resize(n+1);
        for (int i = 1; i <= n; i++){
            for (auto node : g[i]){
                this->graph[i].push_back({node, 1});
            }
        }
    }

    Tree(int n, vector<pair<int, int>> g[]){
        this->n = n;
        this->graph.resize(n+1);
        for (int i = 1; i <= n; i++){
            for (auto [node, cost] : g[i]){
                this->graph[i].push_back({node, cost});
            }
        }
    }

    Tree(int n, vector<vector<int>> g){
        this->n = n;
        this->graph.resize(n+1);
        for (int i = 1; i <= n; i++){
            for (auto node : g[i]){
                this->graph[i].push_back({node, 1});
            }
        }
    }

    Tree(int n, vector<vector<pair<int, int>>> g){
        this->n = n;
        this->graph.resize(n+1);
        for (int i = 1; i <= n; i++){
            for (auto [node, cost] : g[i]){
                this->graph[i].push_back({node, cost});
            }
        }
    }

    // 트리의 지름 세팅
    void FindDiameter(){
        auto u = Bfs(1);
        auto v = Bfs(u.first);
        this->diameter = v.second.first;

        auto e = Bfs(v.first);
        vector<int> d1 = v.second.second;
        vector<int> d2 = e.second.second;
        for (int i = 1; i <= n; i++){
            if (d1[i] + d2[i] == this->diameter){
                diameterNodes.push_back(i);
            }
        }
    }
    
    // 트리의 지름 반환. FindDiameter 먼저 쓸것
    int GetDiameter(){ 
        return this->diameter;
    }
    
    // 트리의 지름위의 노드들 반환. FindDiameter 먼저 쓸것
    vector<int> GetDiameterNodes(){
        return this->diameterNodes;
    }
    
    // start로부터 모든 노드들간의 거리 반환
    vector<int> GetDistToNode(int start){
        auto u = Bfs(start);
        return u.second.second;
    }

    // LCA 세팅
    void FindLca(int root){
        this->table.resize(n+1, vector<int>(21));
        this->dist.resize(n+1, vector<int>(21));
        this->depth.resize(n+1);
        fill(this->depth.begin(), this->depth.end(), -1);
        Dfs(root, 0);
        for (int k = 1; k <= 20; k++){
            for (int i = 1; i <= n; i++){
                table[i][k] = table[table[i][k-1]][k-1];
                dist[i][k] = dist[i][k-1] + dist[table[i][k-1]][k-1];
            }
        }
    }

    // a,b의 LCA 반환. FindLca 먼저 쓸것
    int GetLca(int a, int b){
        if (depth[a] < depth[b]) swap(a,b);
    
        for (int i = 20; i >= 0; i--){
            if ((depth[a] - depth[b]) >= (1 << i)){
                a = table[a][i];
            }
        }
    
        if (a == b) return a;
    
        for (int i = 20; i >= 0; i--){
            if (table[a][i] != table[b][i]){
                a = table[a][i];
                b = table[b][i];
            }
        }
    
        return table[a][0];
    }
    
    // a,b 사이의 거리 반환. FindLca 먼저 쓸것
    int GetDistAtoB(int a, int b){
        int ret = 0;
    
        if (depth[a] < depth[b]) swap(a,b);
    
        for (int i = 20; i >= 0; i--){
            if ((depth[a] - depth[b]) >= (1 << i)){
                ret += dist[a][i];
                a = table[a][i];
            }
        }
    
        if (a == b) return ret;
    
        for (int i = 20; i >= 0; i--){
            if (table[a][i] != table[b][i]){
                ret += dist[a][i] + dist[b][i];
                a = table[a][i];
                b = table[b][i];
            }
        }
    
        ret += dist[a][0];
        ret += dist[b][0];
    
        return ret;
    }
};

vector<pair<int, int>> graph[10101];

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int u,v,c;
    int n = 10000;
    while (cin >> u >> v >> c){
        graph[u].push_back({v,c});
        graph[v].push_back({u,c});
    }

    Tree t(n, graph);
    t.FindDiameter();

    cout << t.GetDiameter() << '\n';

    return 0;
}