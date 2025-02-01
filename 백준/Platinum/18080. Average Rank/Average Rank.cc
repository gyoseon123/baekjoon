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
#include <cmath>
// #define ll long long
#define int long long

using namespace std;

int n,w,k;
pair<int, int> rank_sum[1010101]; // 각 점수가 받는 랭크 패널티
int rnk[303030]; // 이걸 rank_sum에 더해줘야됨, 얘는 현재 rank를 빠져나간 개수
int now_score[303030];
int ans[303030];

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 
    cout.tie(NULL);
    
    cin >> n >> w;

    for (int i = 0; i < w; i++){
        cin >> k;
        for (int j = 0; j < k; j++){
            int x; cin >> x;
            int now = now_score[x];
            ans[x] += rank_sum[now].first + (i - rank_sum[now].second) * rnk[now];
            rank_sum[now] = {rank_sum[now].first + (i - rank_sum[now].second) * rnk[now], i};
            rnk[now]++;
            now_score[x]++;
            ans[x] -= rank_sum[now+1].first + (i - rank_sum[now+1].second) * rnk[now+1];
        }
    }

    cout.precision(10);
    cout << fixed;

    for (int i = 1; i <= n; i++){
        int now = now_score[i];
        cout << (double)(ans[i] + rank_sum[now].first + (w - rank_sum[now].second) * rnk[now] + w)/(long double)w << '\n';
    }
    
    return 0;
}