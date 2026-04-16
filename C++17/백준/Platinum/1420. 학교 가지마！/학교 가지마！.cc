#include <bits/stdc++.h>
#define ll long long
// #define int long long
const int inf = 1e9;

using namespace std;

template<typename FlowType, size_t _Sz, FlowType _Inf> struct Dinic {
    struct Edge { int v, dual; FlowType c; };
    int Level[_Sz], Work[_Sz];
    vector<Edge> G[_Sz];
    void clear() { for (int i = 0; i < _Sz; i++) G[i].clear(); }
    void AddEdge(int s, int e, FlowType x) {
        G[s].push_back({ e, (int)G[e].size(), x });
        G[e].push_back({ s, (int)G[s].size() - 1, 0 });
    }
    bool BFS(int S, int T) {
        memset(Level, 0, sizeof Level);
        queue<int> Q; Q.push(S); Level[S] = 1;
        while (Q.size()) {
            int v = Q.front(); Q.pop();
            for (const auto& i : G[v]) {
                if (!Level[i.v] && i.c) Q.push(i.v), Level[i.v] = Level[v] + 1;
            }
        }
        return Level[T];
    }
    FlowType DFS(int v, int T, FlowType tot) {
        if (v == T) return tot;
        for (int& _i = Work[v]; _i < G[v].size(); _i++) {
            Edge& i = G[v][_i];
            if (Level[i.v] != Level[v] + 1 || !i.c) continue;
            FlowType fl = DFS(i.v, T, min(tot, i.c));
            if (!fl) continue;
            i.c -= fl;
            G[i.v][i.dual].c += fl;
            return fl;
        }
        return 0;
    }
    FlowType MaxFlow(int S, int T) {
        FlowType ret = 0, tmp;
        while (BFS(S, T)) {
            memset(Work, 0, sizeof Work);
            while ((tmp = DFS(S, T, _Inf))) ret += tmp;
        }
        return ret;
    }
    tuple<FlowType, vector<int>, vector<int>, vector<pair<int, int>>> MinCut(int S, int T) {
        FlowType fl = MaxFlow(S, T);
        vector<int> a, b;
        vector<pair<int, int>> edges;
        const int Bias = 1e9;
        queue<int> Q; Q.push(S); Level[S] += Bias;
        while (Q.size()) {
            int v = Q.front(); Q.pop();
            for (const auto& i : G[v]) {
                if (!Level[i.v]) edges.emplace_back(v, i.v);
                else if (Level[i.v] < Bias) Q.push(i.v), Level[i.v] += Bias;
            }
        }
        for (int i = 0; i < _Sz; i++) {
            if (Level[i]) a.push_back(i);
            else b.push_back(i);
        }
        return make_tuple(fl, a, b, edges);
    }
};

int n,m;
int s,e;
string board[101];

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m;
    for (int i = 0; i < n; i++){
        cin >> board[i];
        for (int j = 0; j < m; j++){
            if (board[i][j] == 'K') s = (i * m + j)*2+1;
            if (board[i][j] == 'H') e = (i * m + j)*2;
        }
    }

    Dinic<int, 20202, inf> dinic;
    for (int i = 0; i < n*m; i++){
        dinic.AddEdge(i*2, i*2+1, 1);
    }

    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            if (board[i][j] != '#'){
                if (i+1 < n && board[i+1][j] != '#'){
                    int now = i * m + j;
                    int nxt = (i+1) * m + j;
                    int now_in = now*2;
                    int now_out = now*2+1;
                    int nxt_in = nxt*2;
                    int nxt_out = nxt*2+1;
                    dinic.AddEdge(now_out, nxt_in, inf);
                    dinic.AddEdge(nxt_out, now_in, inf);
                }
                if (j+1 < m && board[i][j+1] != '#'){
                    int now = i*m + j;
                    int nxt = i*m + (j+1);
                    int now_in = now*2;
                    int now_out = now*2+1;
                    int nxt_in = nxt*2;
                    int nxt_out = nxt*2+1;
                    dinic.AddEdge(now_out, nxt_in, inf);
                    dinic.AddEdge(nxt_out, now_in, inf);
                }
            }
        }
    }

    int ans = dinic.MaxFlow(s, e);

    if (ans >= inf) cout << -1 << '\n';
    else cout << ans << '\n';

    return 0;
}