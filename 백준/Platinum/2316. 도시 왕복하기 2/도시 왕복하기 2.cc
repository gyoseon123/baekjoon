#include <bits/stdc++.h>
// #define ll long long
#define int long long

using namespace std;

int n,p;
vector<int> graph[808];
int f[808][808], c[808][808], d[808];

int flow(int start, int end){
    int ret = 0;

    while (1){
        memset(d, -1, sizeof d);
        queue<int> q;
        q.push(start);
        while (!q.empty()){
            int now = q.front();
            q.pop();
            for (auto next : graph[now]){
                if (c[now][next] - f[now][next] > 0 && d[next] == -1){
                    d[next] = now;
                    q.push(next);
                    if (next == end) break;
                }
            }
        }

        if (d[end] == -1) break;

        int flow = 1e9;
        for (int i = end; i != start; i = d[i]){
            flow = min(flow, c[d[i]][i] - f[d[i]][i]);
        }

        for (int i = end; i != start; i = d[i]){
            f[d[i]][i] += flow;
            f[i][d[i]] -= flow;
        }

        ret += flow;
    }

    return ret;
}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 
    cout.tie(NULL);
    
    cin >> n >> p;
    for (int i = 0; i < p; i++){
        int a,b; cin >> a >> b;
        int a_in = a*2-1;
        int a_out = a*2;
        int b_in = b*2-1;
        int b_out = b*2;
        graph[a_in].push_back(a_out);
        graph[b_in].push_back(b_out);
        graph[a_in].push_back(b_out);
        graph[b_in].push_back(a_out);
        graph[a_out].push_back(b_in);
        graph[b_out].push_back(a_in);
        c[a_in][a_out] = c[b_in][b_out] = c[a_out][b_in] = c[b_out][a_in] = 1;
    }

    c[1][2] = 1e9;
    c[3][4] = 1e9;

    cout << flow(1,4);
    
    return 0;
}