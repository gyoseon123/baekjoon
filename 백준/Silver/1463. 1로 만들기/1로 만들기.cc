#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <queue>
#include <stack>
#include <set>
#include <unordered_set>
#include <cmath>
#include <map>
#include <array>
// #define ll long long
#define int long long

using namespace std;

int n;
int dp[1010101];

int solve(int x){
    if (x == 1) return 0;

    int &ret = dp[x];
    if (ret != -1) return ret;

    int ans = 1e9;
    if (x%3 == 0) ans = min(ans, solve(x/3));
    if (x%2 == 0) ans = min(ans, solve(x/2));
    ans = min(ans, solve(x-1));

    return ret = ans + 1;
}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    memset(dp, -1, sizeof dp);
    cin >> n;
    cout << solve(n);

    return 0;
}