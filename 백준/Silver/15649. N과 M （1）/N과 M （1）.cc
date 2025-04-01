#include <bits/stdc++.h>
// #define ll long long
#define int long long
const int inf = 1e9;

using namespace std;

int n, m;
vector<int> ans;
bool visited[10];

void f(int cnt){
    if (cnt == m){
        for (int i = 0; i < m; i++){
            cout << ans[i] << ' ';
        }
        cout << '\n';
        return;
    }

    for (int i = 1; i <= n; i++){
        if (!visited[i]){
            visited[i] = true;
            ans.push_back(i);
            f(cnt+1);
            ans.pop_back();
            visited[i] = false;
        }
    }
}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m;
    f(0);

    return 0;
}