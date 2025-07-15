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

int k,n;
int block[10];
int a[606060];
vector<int> block_idx[10];
int ans[3][101010];
int use[10];

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 
    cout.tie(NULL);
    cin >> k >> n;

    for (int i = 0; i < k; i++) cin >> a[i*2];
    for (int i = 0; i < k; i++) cin >> a[i*2+1];

    for (int i = 0; i < k*2; i += 2){
        block[a[i]*a[i+1]]++;
        block_idx[a[i]*a[i+1]].push_back(i/2+1);
    }

    int idx = 0;
    for (auto now : block_idx[9]){ // 33 채우기
        for (int i = idx; i < idx+3; i++){
            ans[0][i] = now;
            ans[1][i] = now;
            ans[2][i] = now;
        }
        idx += 3;
    }

    for (auto now : block_idx[6]){ // 23채우기
        for (int i = idx; i < idx+2; i++){
            ans[0][i] = now;
            ans[1][i] = now;
            ans[2][i] = now;
        }
        idx += 2;
    }

    int up_start = idx; // 22채우기 시작할 인덱스


    for (auto now : block_idx[4]){
        for (int i = idx; i < idx+2; i++){
            ans[1][i] = now;
            ans[2][i] = now;
        }
        idx += 2;
    }

    int up_end = idx; // 22채우기 끝나는 인덱스

    if (up_start <= up_end - 2){
        for (auto now : block_idx[2]){
            for (int i = up_start; i < up_start+2; i++){
                ans[0][i] = now;
            }
            up_start += 2; // 얘는 결국 21끝나는 인덱스까지 감
            use[2]++;
            if (up_start == up_end) break;
        }
    }

    if (up_start <= up_end-3){
        for (auto now : block_idx[3]){
            for (int i = up_start; i < up_start+3; i++){
                ans[0][i] = now;
            }
            use[3]++;
            up_start += 3;
            if (up_start + 3 > up_end) break;
        }
    }

    if (up_start <= up_end-1){
        for (auto now : block_idx[1]){
            for (int i = up_start; i < up_start+1; i++){
                ans[0][i] = now;
            }
    
            use[1]++;
            up_start++;
            if (up_start + 1 > up_end) break;
        }
    }

    for (int i = use[3]; i < block_idx[3].size(); i++){
        ans[0][up_end] = block_idx[3][i];
        ans[1][up_end] = block_idx[3][i];
        ans[2][up_end] = block_idx[3][i];
        up_end++;
    }

    for (int i = use[2]; i+2 < block_idx[2].size(); i+=3){
        ans[0][up_end] = ans[0][up_end+1] = block_idx[2][i+0];
        ans[1][up_end] = ans[1][up_end+1] = block_idx[2][i+1];
        ans[2][up_end] = ans[2][up_end+1] = block_idx[2][i+2];
        up_end += 2;
        use[2] += 3;
    }

    int one_start = use[1];

    for (int i = use[2]; i < block_idx[2].size(); i++){
        ans[0][up_end] = ans[1][up_end] = block_idx[2][i];
        ans[2][up_end] = block_idx[1][one_start];
        one_start++;
        up_end++;
    }

    for (int i = one_start; i < block_idx[1].size(); i += 3){
        ans[0][up_end] = block_idx[1][i];
        ans[1][up_end] = block_idx[1][i+1];
        ans[2][up_end] = block_idx[1][i+2];
        up_end++;
    }


    for (int i = 0; i < n; i++){
        cout << ans[0][i] << ' ';
    }
    cout << '\n';
    for (int i = 0; i < n; i++){
        cout << ans[1][i] << ' ';
    }
    cout << '\n';
    for (int i = 0; i < n; i++){
        cout << ans[2][i] << ' ';
    }

    
    return 0;
}