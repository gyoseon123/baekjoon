#include <bits/stdc++.h>
// #define ll long long
// #define int long long
const int inf = 1e9;

using namespace std;

vector<string> strs;
int alp[26];
int used[10];
vector<char> able;
int d[26];
int flg;

int check(){
    vector<int> nums;
    for (int i = 0; i < 3; i++){
        int res = 0;
        for (int j = 0; j < strs[i].size(); j++){
            res *= 10;
            res += d[strs[i][j] - 'A'];
        }
        nums.push_back(res);
    }
    return (nums[0] + nums[1] == nums[2]);
}

void dfs(int cnt){
    if (flg) return;
    if (cnt == able.size()){
        if (check()) flg = 1;
        return;
    }

    for (int i = 0; i < 10; i++){
        if (!used[i]){
            used[i] = 1;
            d[able[cnt] - 'A'] = i;
            dfs(cnt+1);
            used[i] = 0;
        }
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    for (int i = 0; i < 3; i++){
        string s; cin >> s;
        strs.push_back(s);
    }

    for (int i = 0; i < 3; i++){
        for (int j = 0; j < strs[i].size(); j++){
            alp[strs[i][j] - 'A'] = 1;
        }
    }

    for (int i = 0; i < 26; i++){
        if (alp[i]) able.push_back(i + 'A');
    }

    if (able.size() > 10){
        cout << "NO" << '\n';
        return 0;
    }

    dfs(0);

    if (flg) cout << "YES" << '\n';
    else cout << "NO" << '\n';

    return 0;
}