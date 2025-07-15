#include <bits/stdc++.h>
// #define ll long long
#define int long long
const int inf = 1e9;

using namespace std;

int n,h,q;
vector<pair<int, int>> line;
vector<int> itv;
vector<int> itv_s;
int nows = 0, nowe = 0;


int bs(int target){
    int left = -1;
    int right = itv.size();

    while (left + 1 < right){
        int mid = (left + right)/2;
        if (target <= itv[mid]) right = mid;
        else left = mid;
    }

    return right;
}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> h;

    for (int i = 0; i < n; i++){
        int a,b; cin >> a >> b;
        line.push_back({a,b});
    }

    sort(line.begin(), line.end());

    for (auto [s, e] : line){
        if (nowe < s){
            itv.push_back(s - nowe - 1);
            nows = s;
            nowe = e;
        }
        if (e > nowe) nowe = e;
    }

    itv.push_back(h - nowe);
    sort(itv.begin(), itv.end());

    itv_s.push_back(0);
    for (int i = 0; i < itv.size(); i++){
        itv_s.push_back(itv[i]);
    }

    for (int i = 0; i < itv.size(); i++){
        itv_s[i+1] += itv_s[i];
    }

    cin >> q;

    for (int i = 0; i < q; i++){
        int ti; cin >> ti;
        int start = bs(ti);
        int a = itv.size() - start;
        int b = itv_s[itv_s.size()-1] - itv_s[start] - a*ti;
        cout << a + b << '\n';
    }

    return 0;
}