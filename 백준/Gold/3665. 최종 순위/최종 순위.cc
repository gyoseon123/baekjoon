#include <bits/stdc++.h>
#define ll long long
// #define int long long
const int inf = 1e9;

using namespace std;

int t;
int n, m;
int arr[505];
int indegree[505];
int graph[505][505];

void solve(){
    cin >> n;
    for (int i = 1; i <= n; i++){
        cin >> arr[i];
        indegree[i] = 0;
        for (int j = 1; j <= n; j++){
            graph[i][j] = 0;
        }
    }

    for (int i = 1; i <= n; i++){
        for (int j = i+1; j <= n; j++){
            graph[arr[j]][arr[i]] = 1;
            indegree[arr[i]]++;
        }
    }

    cin >> m;
    for (int i = 0; i < m; i++){
        int a, b; cin >> a >> b;
        if (!graph[a][b]) swap(a,b);
        graph[a][b] = 0;
        graph[b][a] = 1;
        indegree[b]--;
        indegree[a]++;
    }

    // for (int i = 1; i <= n; i++){
    //     for (int j = 1; j <= n; j++){
    //         cout << graph[i][j] << ' ';
    //     }
    //     cout << '\n';
    // }

    // for (int i = 1; i <= n; i++){
    //     cout << indegree[i] << ' ';
    // }
    // cout << '\n';

    vector<int> ans;
    for (int _ = 0; _ < n; _++){
        int find = 0;
        int node = 0;
        for (int i = 1; i <= n; i++){
            if (indegree[i] == 0){
                if (find){
                    cout << "?" << '\n';
                    return;
                }
                find = 1;
                node = i;
            }
        }

        if (find) ans.push_back(node);
        indegree[node] = -1;
        for (int i = 1; i <= n; i++){
            if (i == node) continue;
            if (graph[node][i]){
                graph[node][i] = 0;
                indegree[i]--;
            }
        }
    }

    if (ans.size() != n){
        cout << "IMPOSSIBLE" << '\n';
    } else {
        for (int i = n-1; i >= 0; i--) cout << ans[i] << ' ';
        cout << '\n';
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> t;
    while (t--) solve();
    
    return 0;
}