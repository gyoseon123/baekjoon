#include <iostream>
#include <vector>
#include <string.h>
using namespace std;

// int main(){
//     int c,n;
//     cin >> c;
//     while (c--){
//         cin >> n;
//         vector<vector<int>> board (n, vector<int>(n));
//         for (int i = 0; i < n; i++){
//             for (int j = 0; j < n; j++){
//                 cin >> board[i][j];
//             }
//         }
//         vector<vector<int>> dp (n, vector<int>(n,0));
//         dp[0][0] = 1;
//         for (int x = 0; x < n; x++){
//             for (int y = 0; y < n; y++){
//                 int nx = x + board[x][y];
//                 int ny = y + board[x][y];
//                 if (nx >= 0 && nx < n) dp[nx][y] += dp[x][y];
//                 if (ny >= 0 && ny < n) dp[x][ny] += dp[x][y];
//             }
//         }
//         if (dp[n-1][n-1] != 0) cout << "YES" << "\n";
//         else cout << "NO" << "\n";
//     }
// }


int n, board[100][100];
int cache[100][100];
int isAbleJump(int x, int y){
    if (x >= n || y >= n) return 0;
    if (x == n-1 && y == n-1) return 1;
    int& ret = cache[x][y];
    if (ret != -1) return ret;
    int jumpSize = board[x][y];
    return ret = (isAbleJump(x + jumpSize, y) || isAbleJump(x, y + jumpSize));
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int c; 
    cin >> c;
    while (c--){
        memset(cache, -1, sizeof(cache));
        cin >> n;
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                cin >> board[i][j];
            }
        }
        if (isAbleJump(0,0)) cout << "YES" << "\n";
        else cout << "NO" << "\n";
    }
    return 0;
}