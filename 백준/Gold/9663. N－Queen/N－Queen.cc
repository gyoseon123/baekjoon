#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <queue>
#include <stack>
#include <unordered_set>
#include <cmath>
#define ll long long

using namespace std;

int N;
int ans = 0;
int queen[15];

void solve(int cnt){
    if (cnt == N){
        ans++;
        return;
    }

    for (int i = 0; i < N; i++){
        bool flg = 1;
        for (int j = 0; j < cnt; j++){
            if (queen[j] != -1 && (queen[j] == i || abs(queen[j]-i) == abs(j-cnt) || abs(queen[j]-i) == -abs(j-cnt))) flg = 0;
            }
        if (flg){
            queen[cnt] = i;
            solve(cnt+1);
        }
    }
}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    memset(queen, -1, sizeof(queen));
    cin >> N;
    solve(0);
    cout << ans;

    return 0;
}