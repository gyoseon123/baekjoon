#include <bits/stdc++.h>
// #define ll long long
// #define int long long

const int inf = 1e9;
using namespace std;

int n,m;
int dist[101][101];

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 
    cout.tie(NULL);

    fill_n(&dist[0][0], 101*101, inf);

    cin >> n;
    cin >> m;

    for (int i = 0 ; i < m; i++){
        int a,b,c; cin >> a >> b >> c;
        if (c < dist[a][b]) dist[a][b] = c;
    }

    for (int i = 1; i <= n; i++) dist[i][i] = 0;

    for (int k = 1; k <= n; k++){
        for (int i = 1; i <= n; i++){
            for (int j = 1; j <= n; j++){
                int cost = dist[i][k] + dist[k][j];
                if (cost < dist[i][j]) dist[i][j] = cost;
            }
        }
    }
    
    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= n; j++){
            cout << ((dist[i][j] != inf) ? dist[i][j] : 0) << ' ';
        }
        cout << '\n';
    }
    
    return 0;
}