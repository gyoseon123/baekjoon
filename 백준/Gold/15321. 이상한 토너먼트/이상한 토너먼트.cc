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
#include <math.h>
// #define ll long long
#define int long long

using namespace std;

int n;
int a[505];
int itv_max[505][505];
int dp[505][505];

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 
    cout.tie(NULL);

    cin >> n;
    for (int i = 0; i < n; i++) cin >> a[i];

    for (int i = 0; i < n; i++){
        int maxx = -1;
        for (int j = i; j < n; j++){
            maxx = max(maxx, a[j]);
            itv_max[i][j] = maxx;
        }
    }

    for (int itv = 1; itv < n; itv++){
        for (int i = 0; i < n-itv; i++){
            int j = i + itv;
            int ret = 1e9;
            for (int k = i; k < j; k++){
                ret = min(ret, dp[i][k] + dp[k+1][j] + abs(itv_max[i][k] - itv_max[k+1][j]));
            }
            dp[i][j] = ret;
        }
    }

    cout << dp[0][n-1];
    
    return 0;
}