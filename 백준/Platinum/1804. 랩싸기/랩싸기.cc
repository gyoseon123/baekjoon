#include <bits/stdc++.h>
#define ll long long
//#define int long long
const int inf = 1e9;

using namespace std;


int n,k,b;
int dp[1010][1010][4];
int ori_x[1010];
int new_X[1010];
int board[2][1010];
vector<pair<int, int>> points;

int go(int i, int j, int stat){
    if (j == -1) return inf;
    if (i == 0) return 0;
    if (j == 0) return inf;

    int &ret = dp[i][j][stat];
    if (ret != -1) return ret;

    int tmp = inf;
    if (board[0][i] == 1 && board[1][i] == 1){
        if (stat == 0){
            tmp = min(tmp, go(i-1, j, 0) + (ori_x[i] - ori_x[i-1])*2);
            for (int k = 0; k < 4; k++) tmp = min(tmp, go(i-1, j-1, k) + 2);
        } 
        else if (stat == 1) {
            tmp = min(tmp, go(i-1, j, 1) + (ori_x[i] - ori_x[i-1])*2);
            tmp = min(tmp, go(i-1, j-1, 1) + (ori_x[i] - ori_x[i-1] + 1));
            tmp = min(tmp, go(i-1, j-1, 2) + (ori_x[i] - ori_x[i-1] + 1));
            tmp = min(tmp, go(i-1, j-1, 3) + (ori_x[i] - ori_x[i-1] + 1));
            for (int k = 0; k < 4; k++) tmp = min(tmp, go(i-1, j-2, k) + 2);
        }
        else tmp = inf;
    } else if (board[0][i] == 0 && board[1][i] == 1){
        if (stat == 0) {
            tmp = min(tmp, go(i-1, j, 0) + (ori_x[i] - ori_x[i-1])*2);
            for (int k = 0; k < 4; k++) tmp = min(tmp, go(i-1, j-1, k) + 2);
        }
        else if (stat == 1) {
            tmp = min(tmp, go(i-1, j, 1) + (ori_x[i] - ori_x[i-1])*2);
            tmp = min(tmp, go(i-1, j-1, 1) + (ori_x[i] - ori_x[i-1] + 1));
            tmp = min(tmp, go(i-1, j-1, 2) + (ori_x[i] - ori_x[i-1] + 1));
            tmp = min(tmp, go(i-1, j-1, 3) + (ori_x[i] - ori_x[i-1] + 1));
            for (int k = 0; k < 4; k++) tmp = min(tmp, go(i-1, j-2, k) + 2);
        }
        else if (stat == 2) {
            tmp = min(tmp, go(i-1, j, 1) + ori_x[i] - ori_x[i-1]);
            tmp = min(tmp, go(i-1, j, 2) + ori_x[i] - ori_x[i-1]);
            for (int k = 0; k < 4; k++) tmp = min(tmp, go(i-1, j-1, k) + 1);
        }
        else tmp = inf;
    } else {
        if (stat == 0) {
            tmp = min(tmp, go(i-1, j, 0) + (ori_x[i] - ori_x[i-1])*2);
            for (int k = 0; k < 4; k++) tmp = min(tmp, go(i-1, j-1, k) + 2);
        }
        else if (stat == 1) {
            tmp = min(tmp, go(i-1, j, 1) + (ori_x[i] - ori_x[i-1])*2);
            tmp = min(tmp, go(i-1, j-1, 1) + (ori_x[i] - ori_x[i-1] + 1));
            tmp = min(tmp, go(i-1, j-1, 2) + (ori_x[i] - ori_x[i-1] + 1));
            tmp = min(tmp, go(i-1, j-1, 3) + (ori_x[i] - ori_x[i-1] + 1));
            for (int k = 0; k < 4; k++) tmp = min(tmp, go(i-1, j-2, k) + 2);
        }
        else if (stat == 3) {
            tmp = min(tmp, go(i-1, j, 1) + ori_x[i] - ori_x[i-1]);
            tmp = min(tmp, go(i-1, j, 3) + ori_x[i] - ori_x[i-1]);
            for (int k = 0; k < 4; k++) tmp = min(tmp, go(i-1, j-1, k) + 1);
        }
        else tmp = inf;
    }

    return ret = tmp;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    memset(dp, -1, sizeof dp);
    cin >> n >> k >> b;
    for (int i = 0; i < n; i++){
        int x,y; cin >> x >> y;
        points.push_back({x,y});
    }

    sort(points.begin(), points.end(), [](pair<int, int> a, pair<int, int> b){
        return a.second < b.second;
    });

    int range = 1;
    for (int i = 0; i < n; i++){
        if (i > 0 && points[i].second != points[i-1].second) range++;
        ori_x[range] = points[i].second;
        new_X[i] = range;
    }
    range++;
    ori_x[0] = ori_x[1]-1;

    for (int i = 0; i < n; i++) points[i].second = new_X[i];
    for (auto [x,y] : points) board[x-1][y] = 1;

    if (board[0][1] == 1 && board[1][1] == 1){
        dp[1][1][0] = 2;
        dp[1][2][0] = 2;
        dp[1][2][1] = 2;
    } else if (board[0][1] == 0 && board[1][1] == 1){
        dp[1][1][0] = 2;
        dp[1][1][2] = 1;
        dp[1][2][0] = 2;
        dp[1][2][1] = 2;
        dp[1][2][2] = 1;
    } else {
        dp[1][1][0] = 2;
        dp[1][1][3] = 1;
        dp[1][2][0] = 2;
        dp[1][2][1] = 2;
        dp[1][2][3] = 1;
    }
    
    for (int i = 0; i <= k; i++){
        for (int j = 0; j < 4; j++){
            if (dp[1][i][j] == -1) dp[1][i][j] = inf;
        }
    }

    // for (int i = 0; i < range; i++) cout << board[0][i] << ' ';
    // cout << '\n';
    // for (int i = 0; i < range; i++) cout << board[1][i] << ' ';
    // cout << '\n';

    // go(1, 1, 0);
    int ans = inf;
    for (int i = 0; i < 4; i++) ans = min(ans, go(range-1, k, i));

    cout << ans << '\n';

    // for (int i = 0; i < range; i++) cout << dp[i][1][0] << ' ';
    // cout << '\n';
    // for (int i = 0; i < range; i++) cout << dp[i][1][1] << ' ';
    // cout << '\n';
    // for (int i = 0; i < range; i++) cout << dp[i][1][2] << ' ';
    // cout << '\n';
    // for (int i = 0; i < range; i++) cout << dp[i][1][3] << ' ';
    // cout << '\n';
    // cout << '\n';
    
    // for (int i = 0; i < range; i++) cout << dp[i][2][0] << ' ';
    // cout << '\n';
    // for (int i = 0; i < range; i++) cout << dp[i][2][1] << ' ';
    // cout << '\n';
    // for (int i = 0; i < range; i++) cout << dp[i][2][2] << ' ';
    // cout << '\n';
    // for (int i = 0; i < range; i++) cout << dp[i][2][3] << ' ';
    // cout << '\n';
    // cout << '\n';
    
    
    // for (int i = 0; i < range; i++) cout << dp[i][3][0] << ' ';
    // cout << '\n';
    // for (int i = 0; i < range; i++) cout << dp[i][3][1] << ' ';
    // cout << '\n';
    // for (int i = 0; i < range; i++) cout << dp[i][3][2] << ' ';
    // cout << '\n';
    // for (int i = 0; i < range; i++) cout << dp[i][3][3] << ' ';
    // cout << '\n';
    
    return 0;
}