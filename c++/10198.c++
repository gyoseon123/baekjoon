#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
using namespace std;

int solve(){
    int L,C,N;
    cin >> L >> C >> N;
    vector <int> rock(N);
    for (int i = 0; i < N; i++) cin >> rock[i];
    sort(rock.begin(), rock.end());
    rock.push_back(L);
    vector <int> interval;
    int max_interval = 0;
    for (int i = 0; i < N; i++){
        for (int j = i+1; j < N; j++){
            int ivl = rock[j] - rock[i];
            interval.push_back(ivl);
            if (j-i == 1){
                max_interval = ivl > max_interval? ivl : max_interval;
            }
        }
    }
    
    // long long int ans = (long long int)1e18;
    for (int i = 0; i < interval.size(); i++){
        int jump_cnt = 0;
        int now = 0;
        int jump_len = interval[i];
        if (jump_len < max_interval) continue;

        cout << "-----" << jump_len << '\n'; 
        for (int j = 0; j < (N+1); j++){
            int now_point = rock[j];
            if (now + jump_len > L){
                cout << jump_len*jump_len + jump_cnt*C;

            }
            if (now_point - now <= jump_len) continue;
            else {
                now = rock[j-1];
                jump_cnt ++;
            }
            cout << now << '\n';

        }
        // int cost = jump_len*jump_len + jump_cnt*C;
        // ans = cost < ans? cost : ans;
    }
    // cout << ans;
}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    solve();
    return 0;
}