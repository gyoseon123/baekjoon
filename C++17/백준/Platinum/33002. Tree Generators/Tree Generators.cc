#include <bits/stdc++.h>
// #define ll long long
#define int long long
const int inf = 1e9;
const int mod = 998244353;

using namespace std;

int cnt;
int pos1[707070];
int pos2[707070];
pair<int, int> itv1[707070];
pair<int, int> itv2[707070];

void init(string s, int pos[]){
    stack<int> stk;
    int n = 1;
    for (int i = 0; i < s.size(); i++){
        if (s[i] == '('){
            stk.push(i);
        } else if (s[i] == ')') {
            pos[stk.top()] = i;
            pos[i] = stk.top();
            stk.pop();
        } else {
            pos[i] = n++;
        }
    }
}

pair<int, int> solve(int l, int r, string &s, pair<int, int> itv[], int pos[]){
    if (r - l == 1){
        itv[++cnt] = {pos[l], pos[r]};
        return itv[cnt];
    }

    if (s[l] != '(' && s[l] != ')'){
        int tmp = ++cnt;
        pair<int, int> right = solve(l+2, r-1, s, itv, pos);
        itv[tmp] = {pos[l], right.second};
        return itv[tmp];
    } else if (s[r] != '(' && s[r] != ')'){
        pair<int, int> left = solve(l+1, r-2, s, itv, pos);
        itv[++cnt] = {left.first, pos[r]};
        return itv[cnt];
    } else {
        pair<int, int> left = solve(l+1, pos[l]-1, s, itv, pos);
        int tmp = ++cnt;
        pair<int, int> right = solve(pos[r]+1, r-1, s, itv, pos);
        itv[tmp] = {left.first, right.second};
        return itv[tmp];
    }
}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s1, s2;
    cin >> s1;
    cin >> s2;

    if (s1.size() == 1){
        cout << 1 << '\n';
        exit(0);
    }

    init(s1, pos1);
    init(s2, pos2);

    int n = 0;
    for (int i = 0; i < s1.size(); i++){
        if (s1[i] == '1') n++;
    }

    cnt = 0;
    solve(1, s1.size()-2, s1, itv1, pos1);
    cnt = 0;
    solve(1, s2.size()-2, s2, itv2, pos2);

    int ans = 1;
    for (int i = 1; i < n; i++){
        ans *= ((i - max(itv1[i].first, itv2[i].first) + 1) * (min(itv1[i].second, itv2[i].second) - i)) % mod;
        ans %= mod; 
    }

    cout << ans << '\n';
    
    return 0;
}