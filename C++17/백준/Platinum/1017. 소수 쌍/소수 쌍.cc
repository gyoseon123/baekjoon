#include <bits/stdc++.h>
// #define ll long long
#define int long long

using namespace std;

int n;
vector<int> graph[55];
int arr[55];
int p[2020];
int visited[55];
int A[55];
int B[55];

void find_p(int x){
    fill_n(p, 2020, 1);
    p[0] = p[1] = 0;

    for (int i = 2; i*i <= x; i++){
        if (p[i]){
            for (int j = i*i; j <= x; j += i) p[j] = 0;
        }
    }
}

int dfs(int now){
    visited[now] = 1;

    for (auto next : graph[now]){
        if (B[next] == -1 || !visited[B[next]] && B[next] != 0 && dfs(B[next])){
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

    cin >> n;
    for (int i = 0; i < n; i++) cin >> arr[i];

    find_p(2000);

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            if (p[arr[i] + arr[j]]){
                graph[i].push_back(j);
            }
        }
    }

    vector<int> ans;
    
    for (auto x : graph[0]){
        memset(A, -1, sizeof A);
        memset(B, -1, sizeof B);
        int match = 1;
        A[0] = x;
        B[x] = 0;
        for (int i = 1; i < n; i++){
            if (A[i] == -1){
                memset(visited, 0, sizeof visited);
                visited[0] = 1;
                if (dfs(i)) match++;
            }
        }
        if (match == n) ans.push_back(arr[x]);
    }

    if (ans.empty()){
        cout << -1;
        return 0;
    }

    sort(ans.begin(), ans.end());

    for (auto x : ans) cout << x << ' ';

    return 0;
}