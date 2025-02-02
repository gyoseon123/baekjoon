#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#include <cstring>
#define ll long long
// #define int long long
#define MAX 4040
#define INF 1e9

using namespace std;

string a,b,ans;
int nxt_0[MAX][2];
int nxt_1[MAX][2];
int dp[MAX][MAX];
int n,m;

int cnt = 0;
int solve(int i, int j){
    if (i >= n && j >= m) return 0;

    int &ret = dp[i][j];

    if (ret != -1) return ret;

    return ret = min(solve(nxt_0[i][0], nxt_0[j][1]), solve(nxt_1[i][0], nxt_1[j][1])) + 1;
}

void trc(int i, int j){
    if (i >= n && j >= m) return;
    int zero = dp[nxt_0[i][0]][nxt_0[j][1]];
    int one = dp[nxt_1[i][0]][nxt_1[j][1]];

    if (zero <= one) ans += '0', trc(nxt_0[i][0], nxt_0[j][1]);
    else ans += '1', trc(nxt_1[i][0], nxt_1[j][1]);
}



signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 
    cout.tie(NULL);
    cin >> a;
    cin >> b;
    a = "0" + a;
    b = "0" + b;
    memset(dp, -1, sizeof dp);

    n = a.size();
    m = b.size();
    
    nxt_0[n][0] = nxt_1[n][0] = n;
    nxt_0[m][1] = nxt_1[m][1] = m;

    int now;

    now = n;
    for (int i = n-1; i >= 0; i--){
        nxt_0[i][0] = now;
        if (a[i] == '0') now = i;
    }

    now = n;
    for (int i = n-1; i >= 0; i--){
        nxt_1[i][0] = now;
        if (a[i] == '1') now = i;
    }

    now = m;
    for (int i = m-1; i >= 0; i--){
        nxt_0[i][1] = now;
        if (b[i] == '0') now = i;
    }
    now = m;
    for (int i = m-1; i >= 0; i--){
        nxt_1[i][1] = now;
        if (b[i] == '1') now = i;
    }

    solve(0,0);
    trc(0,0);

    cout << ans;
    
    return 0;
}