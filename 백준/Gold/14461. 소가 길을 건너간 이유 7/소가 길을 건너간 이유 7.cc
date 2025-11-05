#include <bits/stdc++.h>
#define ll long long
//#define int long long
const int inf = 1e9;

using namespace std;
typedef array<int, 4> arr;

int n,t;
int board[101][101];
int dist[101][101][3];
int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0};

void dijkstra(){
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            for (int k = 0; k < 3; k++){
                dist[i][j][k] = inf;
            }
        }
    }

    priority_queue<arr, vector<arr>, greater<>> pq;
    dist[0][0][0] = 0;
    pq.push({0, 0, 0, 0});

    while (!pq.empty()){
        auto [dis, x, y, stat] = pq.top(); pq.pop();

        if (dis > dist[x][y][stat]) continue;

        for (int i = 0; i < 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
            int cost = dist[x][y][stat] + t + (board[nx][ny]) * (stat == 2);
            if (cost < dist[nx][ny][(stat+1)%3]){
                dist[nx][ny][(stat+1)%3] = cost;
                pq.push({cost, nx, ny, (stat+1)%3});
            }
        }
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> t;
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            cin >> board[i][j];
        }
    }

    dijkstra();

    int ans = inf;
    for (int i = 0; i < 3; i++) ans = min(ans, dist[n-1][n-1][i]);

    cout << ans << '\n';
    
    return 0;
}