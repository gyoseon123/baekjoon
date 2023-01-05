#include <iostream>

using namespace std;

int main(){
    int n,k;
    cin >> n >> k;
    int dp[n+1][k+1];
    int W[n];
    int V[n];
    for (int i = 0; i < n; i++){
        int w,v;
        cin >> w >> v;
        W[i] = w;
        V[i] = v;
    }
    for (int i = 0; i < n; i++){
        for (int j = 0; j < k; j++){
            if (i == 0 || j == 0) dp[i][j] = 0;
            else if (j - W[i-1] >= 0){
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-W[i-1]]+V[i-1]);
            }
            else dp[i][j] = dp[i-1][j];
        }
    }
    cout << dp[n][k];
}