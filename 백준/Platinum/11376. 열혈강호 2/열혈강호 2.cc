#include <bits/stdc++.h>
// #define ll long long
#define int long long

using namespace std;

int n,m;
vector<int> graph[1010];
int A[1010], B[1010], visited[1010];

int dfs(int now){
    visited[now] = 1;

    for (auto next : graph[now]){
        if (B[next] == -1 || !visited[B[next]] && dfs(B[next])){
            A[now] = next;
            B[next] = now;
            return 1;
        }
    }

    return 0;
}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 
    cout.tie(NULL);

    cin >> n >> m;

    
    for (int i = 1; i <= n; i++){
        int x; cin >> x;
        for (int j = 0; j < x; j++){
            int y; cin >> y;
            graph[i].push_back(y);
        }
    }
    
    int ans = 0;
    memset(A, -1, sizeof A);
    memset(B, -1, sizeof B);
    
    for (int i = 1; i <= n; i++){
        if (A[i] == -1){
            memset(visited, 0, sizeof visited);
            if (dfs(i)) ans++;
            A[i] = -1;
            memset(visited, 0, sizeof visited);
            if (dfs(i)) ans++;
        }
    }
    
    // memset(A, -1, sizeof A);
    // for (int i = 1; i <= n; i++){
    //     if (A[i] == -1){
    //         memset(visited, 0, sizeof visited);
    //         if (dfs(i)) ans++;
    //     }
    // }

    cout << ans;
    
    return 0;
}