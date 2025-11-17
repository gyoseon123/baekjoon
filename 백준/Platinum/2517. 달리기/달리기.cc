#include <bits/stdc++.h>
#define ll long long
//#define int long long
const int inf = 1e9;

using namespace std;

int n;
int new_[505050];
int tree[2020202];

void update(int node, int start, int end, int idx, int diff){
    if (idx < start || end < idx) return;
    if (start == end){
        tree[node] += diff;
        return;
    }

    int mid = (start+end)/2;
    update(node*2, start, mid, idx, diff);
    update(node*2+1, mid+1, end, idx, diff);
    tree[node] = tree[node*2] + tree[node*2+1];
}

int sum_qry(int node, int start, int end, int left, int right){
    if (right < start || end < left) return 0;
    if (left <= start && end <= right) return tree[node];

    int mid = (start+end)/2;
    int l = sum_qry(node*2, start, mid, left, right);
    int r = sum_qry(node*2+1, mid+1, end, left, right);
    return l + r;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<pair<int, int>> a;
    cin >> n;
    
    for (int i = 0; i < n; i++){
        int x; cin >> x;
        a.push_back({x, i});
    }

    sort(a.begin(), a.end());
    
    int range = 0;
    for (int i = 0; i < n; i++){
        if (i > 0 && a[i].first != a[i-1].first) range++;
        new_[i] = range;
    }

    for (int i = 0; i < n; i++) a[i].first = new_[i];
    
    sort(a.begin(), a.end(), [](pair<int, int> a, pair<int, int> b){
        return a.second < b.second;
    });

    for (auto [val, idx] : a){
        int s = sum_qry(1, 0, 505050, val+1, 505050);
        cout << s + 1 << '\n';
        update(1, 0, 505050, val, 1);
    }

    return 0;
}