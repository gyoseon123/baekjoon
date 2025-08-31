#include <bits/stdc++.h>
#define ll long long
// #define int long long
const int inf = 1e9;

using namespace std;
typedef array<int, 4> arr;

int N, M, K;
char board[1010][1010];
int dp[1010][1010][11][2];
int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0};

void bfs(){
    dp[0][0][0][0] = 1;
    queue<arr> q;
    q.push({0, 0, 0, 0});

    while (!q.empty()){
        auto [x, y, k, t] = q.front(); q.pop();
        int now = dp[x][y][k][t];

        if (now + 1 < dp[x][y][k][t^1]){
            dp[x][y][k][t^1] = now + 1;
            q.push({x,y,k,t^1});
        }
        for (int i = 0; i < 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (0 <= nx && nx < N && 0 <= ny && ny < M){
                if (board[nx][ny] == '1' && k+1 <= K && now + 1 < dp[nx][ny][k+1][t^1]){
                    dp[nx][ny][k+1][t^1] = now + 1;
                    q.push({nx, ny, k+1, t^1});
                }
                if (board[nx][ny] == '0' && now + 1 < dp[nx][ny][k][t^1]){
                    dp[nx][ny][k][t^1] = now + 1;
                    q.push({nx, ny, k, t^1});
                }
            }
        }
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M >> K;
    for (int i = 0; i < N; i++){
        for (int j = 0; j < M; j++){
            cin >> board[i][j];
        }
    }

    fill(&dp[0][0][0][0], &dp[0][0][0][0] + 1010*1010*11*2, inf);
    bfs();

    int ans = inf;

    for (int i = 0; i <= K; i++){
        ans = min(ans, min(dp[N-1][M-1][i][0], dp[N-1][M-1][i][1]));
    }

    if (ans == inf) cout << -1 << '\n';
    else cout << ans << '\n';
    
    return 0;
}